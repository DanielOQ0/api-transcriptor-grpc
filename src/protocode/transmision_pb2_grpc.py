# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from src.protocode import transmision_pb2 as transmision__pb2


class AudioServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RouteStreamAudio = channel.stream_stream(
                '/transmision.AudioService/RouteStreamAudio',
                request_serializer=transmision__pb2.AudioRequest.SerializeToString,
                response_deserializer=transmision__pb2.AudioReply.FromString,
                )


class AudioServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def RouteStreamAudio(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AudioServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RouteStreamAudio': grpc.stream_stream_rpc_method_handler(
                    servicer.RouteStreamAudio,
                    request_deserializer=transmision__pb2.AudioRequest.FromString,
                    response_serializer=transmision__pb2.AudioReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'transmision.AudioService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AudioService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def RouteStreamAudio(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/transmision.AudioService/RouteStreamAudio',
            transmision__pb2.AudioRequest.SerializeToString,
            transmision__pb2.AudioReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
