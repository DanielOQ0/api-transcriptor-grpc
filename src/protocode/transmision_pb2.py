# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transmision.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11transmision.proto\x12\x0btransmision\"H\n\x0c\x41udioRequest\x12\x0f\n\x07usuario\x18\x01 \x01(\t\x12\x13\n\x0b\x61udio_chunk\x18\x02 \x01(\x0c\x12\x12\n\nfrecuencia\x18\x03 \x01(\x05\"#\n\nAudioReply\x12\x15\n\rtranscripcion\x18\x01 \x01(\t2Z\n\x0c\x41udioService\x12J\n\x10RouteStreamAudio\x12\x19.transmision.AudioRequest\x1a\x17.transmision.AudioReply(\x01\x30\x01\x42/\n\x13\x63om.fcv.transmisionB\x10TransmisionProtoP\x01\xa2\x02\x03RTGb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'transmision_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.fcv.transmisionB\020TransmisionProtoP\001\242\002\003RTG'
  _globals['_AUDIOREQUEST']._serialized_start=34
  _globals['_AUDIOREQUEST']._serialized_end=106
  _globals['_AUDIOREPLY']._serialized_start=108
  _globals['_AUDIOREPLY']._serialized_end=143
  _globals['_AUDIOSERVICE']._serialized_start=145
  _globals['_AUDIOSERVICE']._serialized_end=235
# @@protoc_insertion_point(module_scope)
