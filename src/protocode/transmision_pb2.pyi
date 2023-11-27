from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AudioRequest(_message.Message):
    __slots__ = ["usuario", "audio_chunk", "frecuencia"]
    USUARIO_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CHUNK_FIELD_NUMBER: _ClassVar[int]
    FRECUENCIA_FIELD_NUMBER: _ClassVar[int]
    usuario: str
    audio_chunk: bytes
    frecuencia: int
    def __init__(self, usuario: _Optional[str] = ..., audio_chunk: _Optional[bytes] = ..., frecuencia: _Optional[int] = ...) -> None: ...

class AudioReply(_message.Message):
    __slots__ = ["transcripcion"]
    TRANSCRIPCION_FIELD_NUMBER: _ClassVar[int]
    transcripcion: str
    def __init__(self, transcripcion: _Optional[str] = ...) -> None: ...
