# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/protobuf/internal/import_test_package/import_public_nested.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/protobuf/internal/import_test_package/import_public_nested.proto',
  package='google.protobuf.python.internal.import_test_package',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\nGgoogle/protobuf/internal/import_test_package/import_public_nested.proto\x12\x33google.protobuf.python.internal.import_test_package\".\n\x19ImportPublicNestedMessage\x12\x11\n\x05value\x18\x01 \x01(\x05:\x02\x35\x38'
)




_IMPORTPUBLICNESTEDMESSAGE = _descriptor.Descriptor(
  name='ImportPublicNestedMessage',
  full_name='google.protobuf.python.internal.import_test_package.ImportPublicNestedMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='google.protobuf.python.internal.import_test_package.ImportPublicNestedMessage.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=58,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=174,
)

DESCRIPTOR.message_types_by_name['ImportPublicNestedMessage'] = _IMPORTPUBLICNESTEDMESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImportPublicNestedMessage = _reflection.GeneratedProtocolMessageType('ImportPublicNestedMessage', (_message.Message,), {
  'DESCRIPTOR' : _IMPORTPUBLICNESTEDMESSAGE,
  '__module__' : 'google.protobuf.internal.import_test_package.import_public_nested_pb2'
  # @@protoc_insertion_point(class_scope:google.protobuf.python.internal.import_test_package.ImportPublicNestedMessage)
  })
_sym_db.RegisterMessage(ImportPublicNestedMessage)


# @@protoc_insertion_point(module_scope)
