from src.protocode import transmision_pb2
from src.protocode import transmision_pb2_grpc
from src.service.WhisperService import transcribirWhisper
from src.service.Archivo import guardarAudioBytes

class AudioService(transmision_pb2_grpc.AudioServiceServicer):
    def RouteStreamAudio(self, request_iterator, context):
        peer = context.peer()
        print(f"Nueva conexión del cliente: {peer}")
        for request in request_iterator:
            print(request.usuario)
            print(request.audio_chunk[:10])
            #guardarAudioBytes(request.audio_chunk, request.frecuencia)
            # Procesamiento de audio con whiper
            try:
               resWhisper = transcribirWhisper(request.audio_chunk, request.frecuencia) 
               print("Transcripcion exitosa")
            except Exception as e:
                print(f"Error inesperado: {e}")
            yield transmision_pb2.AudioReply(transcripcion=resWhisper.texto)