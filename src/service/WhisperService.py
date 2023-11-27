import grpc

from src.protocode import transcribir_pb2
from src.protocode import transcribir_pb2_grpc

def transcribirWhisper(audio, frecuencia):
    # Conectarse al servidor
    channel = grpc.insecure_channel("35.247.232.121:50051")
    stub = transcribir_pb2_grpc.GreeterStub(channel)

    # Crear la solicitud
    request = transcribir_pb2.TranscribirRequest(
        modelo="small", 
        tamLote=16, 
        tipoComputo="float16", 
        dispositivo="cuda", 
        audio=audio,
        frecuencia=frecuencia)

    # Enviar la solicitud
    response = stub.RouteTranscribir(request)
    return response
