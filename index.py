import grpc
from concurrent import futures
from src.protocode import transmision_pb2_grpc
from src.service.AudioTransmisionService import AudioService

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    transmision_pb2_grpc.add_AudioServiceServicer_to_server(AudioService(), server)
    server.add_insecure_port("0.0.0.0:50052")
    server.start()
    print("Server started. Listening on port 50052.")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()