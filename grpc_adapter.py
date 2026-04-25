import grpc
from concurrent import futures
import sys
import os

# 1. Get the path to the 'schema' folder
schema_path = os.path.join(os.path.dirname(__file__), 'schema')

# 2. Add it to Python's search list
if schema_path not in sys.path:
    sys.path.append(schema_path)

import agent_pb2
import agent_pb2_grpc

class AgentServicer(agent_pb2_grpc.AgentServiceServicer):
    def CallTool(self, request, context):
        print(f"--- gRPC received request for tool: {request.tool_name} ---")
        
        # Mock logic: In reality, this would call the MCP server
        if request.tool_name == "get_breaker_status":
            result = "Breaker A1 is currently OFF."
        else:
            result = "Tool not found."
            
        return agent_pb2.ToolResponse(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agent_pb2_grpc.add_AgentServiceServicer_to_server(AgentServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()