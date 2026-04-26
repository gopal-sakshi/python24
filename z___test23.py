import grpc
import sys
import os

schema_path = os.path.join(os.path.dirname(__file__), 'schema')
if schema_path not in sys.path:
    sys.path.append(schema_path)
import agent_pb2
import agent_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = agent_pb2_grpc.AgentServiceStub(channel)
        
        # Test 1: Should trigger the 'search' (MongoDB) route
        print("Testing Search Route...")
        response = stub.CallTool(agent_pb2.ToolRequest(arguments="How do I fix the breaker?"))
        print(f"Response: {response.result}\n")

        # Test 2: Should trigger the 'mcp' route
        print("Testing MCP Route...")
        response = stub.CallTool(agent_pb2.ToolRequest(arguments="What is the live status?"))
        print(f"Response: {response.result}")

if __name__ == "__main__":
    run()