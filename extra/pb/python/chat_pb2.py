# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chat.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='chat.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\nchat.proto*\x1c\n\tChatMsgId\x12\x0f\n\x0b\x43hat_MSG_ID\x10\x00\x62\x06proto3'
)

_CHATMSGID = _descriptor.EnumDescriptor(
  name='ChatMsgId',
  full_name='ChatMsgId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Chat_MSG_ID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=14,
  serialized_end=42,
)
_sym_db.RegisterEnumDescriptor(_CHATMSGID)

ChatMsgId = enum_type_wrapper.EnumTypeWrapper(_CHATMSGID)
Chat_MSG_ID = 0


DESCRIPTOR.enum_types_by_name['ChatMsgId'] = _CHATMSGID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
