from typing import Annotated, TypedDict, Literal
from langgraph.graph import StateGraph, START, END
import sys
import os
# 1. Get the path to the 'schema' folder
schema_path = os.path.join(os.path.dirname(__file__), 'schema')

# 2. Add it to Python's search list
if schema_path not in sys.path:
    sys.path.append(schema_path)

import grpc
import agent_pb2
import agent_pb2_grpc

# 1. Update State to include a flag for where we went
class AgentState(TypedDict):
    query: str
    retrieved_info: str
    response: str
    source: str # To track if we used MCP or MongoDB

# --- Node 1: MongoDB Search ---
def retrieve_node(state: AgentState):
    print("--- LOG: Accessing MongoDB Knowledge Base ---")
    return {"retrieved_info": "Manual: Reset the breaker by flipping switch A1.", "source": "MongoDB"}

# --- Node 2: MCP Tool (Mocked) ---
# def mcp_tool_node(state: AgentState):
#     print("--- LOG: Accessing MCP Tool (Live Telemetry) ---")
#     # This mocks a real MCP call to a technician tool
#     return {"retrieved_info": "Sensor Data: Voltage is 220V, Status: NOMINAL", "source": "MCP Tool"}

def mcp_tool_node(state: AgentState):
    # This is the "Who is calling it" part!
    channel = grpc.insecure_channel('localhost:50051')
    stub = agent_pb2_grpc.AgentServiceStub(channel)
    
    # Send the request over the network to the adapter
    response = stub.CallTool(agent_pb2.ToolRequest(
        tool_name="get_breaker_status", 
        arguments="A1"
    ))
    
    return {"retrieved_info": response.result, "source": "Real gRPC Tool"}


# --- Node 3: Generator ---
def mock_llm_node(state: AgentState):
    answer = f"[{state['source']}] Result: {state['retrieved_info']}"
    return {"response": answer}

# --- ROUTER FUNCTION ---
def router(state: AgentState) -> Literal["search", "mcp"]:
    if "status" in state["query"].lower() or "live" in state["query"].lower():
        return "mcp"
    return "search"

# --- Build the Graph ---
builder = StateGraph(AgentState)

builder.add_node("search", retrieve_node)
builder.add_node("mcp_tools", mcp_tool_node)
builder.add_node("generate", mock_llm_node)

# LOGIC: Start -> Router -> (either search OR mcp_tools) -> generate
builder.add_conditional_edges(
    START, 
    router, 
    {"search": "search", "mcp": "mcp_tools"}
)

builder.add_edge("search", "generate")
builder.add_edge("mcp_tools", "generate")
builder.add_edge("generate", END)

app = builder.compile()