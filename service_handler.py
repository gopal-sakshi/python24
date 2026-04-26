import grpc
import agent_pb2
import agent_pb2_grpc
from graph23 import app

class AgentServiceHandler(agent_pb2_grpc.AgentServiceServicer):
    # Handles incoming gRPC requests by passing them intothe LangGraph workflow.
    def CallTool(self, request, context):
        print(f"--- gRPC Request Received ---")
        print(f"Tool: {request.tool_name} | Query: {request.arguments}")
        
        # Prepare the input for LangGraph; We use request.arguments as the 'query' defined in AgentState
        inputs = {"query": request.arguments}
        
        try:
            result = app.invoke(inputs)                 # 1. Invoke the graph
            final_answer = result.get("response", "No response generated.")# 2. Extract the final response from 'generate' node
            return agent_pb2.ToolResponse(result=final_answer)
            
        except Exception as e:
            print(f"Error during Graph Execution: {e}")
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"Graph execution failed: {str(e)}")
            return agent_pb2.ToolResponse()