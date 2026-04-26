import grpc
from concurrent import futures
import sys
import os

schema_path = os.path.join(os.path.dirname(__file__), 'schema')
if schema_path not in sys.path:
    sys.path.append(schema_path)

import agent_pb2_grpc
from service_handler import AgentServiceHandler

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    agent_pb2_grpc.add_AgentServiceServicer_to_server(              # Register the handler from our separate file
        AgentServiceHandler(), 
        server
    )

    port = "50052"
    server.add_insecure_port(f"[::]:{port}")    
    print(f"LangGraph gRPC Server is live on port {port}")
    
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()