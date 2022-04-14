# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: game.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='game.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\ngame.proto\".\n\x0c\x45nterGameReq\x12\x0e\n\x06UserId\x18\x01 \x01(\x03\x12\x0e\n\x06RoleId\x18\x02 \x01(\x05\"\x0e\n\x0c\x45nterGameAck*O\n\tGameMsgId\x12\n\n\x06MSG_ID\x10\x00\x12\x1a\n\x15GAME_ENTERGAMEREQ_REQ\x10\xd1\x0f\x12\x1a\n\x15GAME_ENTERGAMEACK_ACK\x10\xd2\x0f\x62\x06proto3'
)

_GAMEMSGID = _descriptor.EnumDescriptor(
  name='GameMsgId',
  full_name='GameMsgId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MSG_ID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAME_ENTERGAMEREQ_REQ', index=1, number=2001,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='GAME_ENTERGAMEACK_ACK', index=2, number=2002,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=78,
  serialized_end=157,
)
_sym_db.RegisterEnumDescriptor(_GAMEMSGID)

GameMsgId = enum_type_wrapper.EnumTypeWrapper(_GAMEMSGID)
MSG_ID = 0
GAME_ENTERGAMEREQ_REQ = 2001
GAME_ENTERGAMEACK_ACK = 2002



_ENTERGAMEREQ = _descriptor.Descriptor(
  name='EnterGameReq',
  full_name='EnterGameReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='UserId', full_name='EnterGameReq.UserId', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='RoleId', full_name='EnterGameReq.RoleId', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14,
  serialized_end=60,
)


_ENTERGAMEACK = _descriptor.Descriptor(
  name='EnterGameAck',
  full_name='EnterGameAck',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=62,
  serialized_end=76,
)

DESCRIPTOR.message_types_by_name['EnterGameReq'] = _ENTERGAMEREQ
DESCRIPTOR.message_types_by_name['EnterGameAck'] = _ENTERGAMEACK
DESCRIPTOR.enum_types_by_name['GameMsgId'] = _GAMEMSGID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EnterGameReq = _reflection.GeneratedProtocolMessageType('EnterGameReq', (_message.Message,), {
  'DESCRIPTOR' : _ENTERGAMEREQ,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:EnterGameReq)
  })
_sym_db.RegisterMessage(EnterGameReq)

EnterGameAck = _reflection.GeneratedProtocolMessageType('EnterGameAck', (_message.Message,), {
  'DESCRIPTOR' : _ENTERGAMEACK,
  '__module__' : 'game_pb2'
  # @@protoc_insertion_point(class_scope:EnterGameAck)
  })
_sym_db.RegisterMessage(EnterGameAck)


# @@protoc_insertion_point(module_scope)
