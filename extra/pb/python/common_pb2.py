# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63ommon.proto\"\x16\n\x06\x41ssets\x12\x0c\n\x04path\x18\x01 \x01(\t* \n\x0b\x43ommonMsgId\x12\x11\n\rCommon_MSG_ID\x10\x00\x62\x06proto3'
)

_COMMONMSGID = _descriptor.EnumDescriptor(
  name='CommonMsgId',
  full_name='CommonMsgId',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Common_MSG_ID', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=40,
  serialized_end=72,
)
_sym_db.RegisterEnumDescriptor(_COMMONMSGID)

CommonMsgId = enum_type_wrapper.EnumTypeWrapper(_COMMONMSGID)
Common_MSG_ID = 0



_ASSETS = _descriptor.Descriptor(
  name='Assets',
  full_name='Assets',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='path', full_name='Assets.path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=16,
  serialized_end=38,
)

DESCRIPTOR.message_types_by_name['Assets'] = _ASSETS
DESCRIPTOR.enum_types_by_name['CommonMsgId'] = _COMMONMSGID
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Assets = _reflection.GeneratedProtocolMessageType('Assets', (_message.Message,), {
  'DESCRIPTOR' : _ASSETS,
  '__module__' : 'common_pb2'
  # @@protoc_insertion_point(class_scope:Assets)
  })
_sym_db.RegisterMessage(Assets)


# @@protoc_insertion_point(module_scope)
