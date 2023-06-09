# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pdict.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pdict.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bpdict.proto\"<\n\x08PDictSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x17\n\x06values\x18\x03 \x01(\x0b\x32\x07.Values\"\x18\n\x06Values\x12\x0e\n\x06values\x18\x01 \x03(\x01\"`\n\x08PDictVal\x12\x1f\n\x03val\x18\x01 \x03(\x0b\x32\x12.PDictVal.ValEntry\x1a\x33\n\x08ValEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x16\n\x05value\x18\x02 \x01(\x0b\x32\x07.Values:\x02\x38\x01\x62\x06proto3'
)




_PDICTSET = _descriptor.Descriptor(
  name='PDictSet',
  full_name='PDictSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='PDictSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='PDictSet.key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='values', full_name='PDictSet.values', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=15,
  serialized_end=75,
)


_VALUES = _descriptor.Descriptor(
  name='Values',
  full_name='Values',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='Values.values', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=77,
  serialized_end=101,
)


_PDICTVAL_VALENTRY = _descriptor.Descriptor(
  name='ValEntry',
  full_name='PDictVal.ValEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PDictVal.ValEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='value', full_name='PDictVal.ValEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=b'8\001',
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=199,
)

_PDICTVAL = _descriptor.Descriptor(
  name='PDictVal',
  full_name='PDictVal',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='PDictVal.val', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_PDICTVAL_VALENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=199,
)

_PDICTSET.fields_by_name['values'].message_type = _VALUES
_PDICTVAL_VALENTRY.fields_by_name['value'].message_type = _VALUES
_PDICTVAL_VALENTRY.containing_type = _PDICTVAL
_PDICTVAL.fields_by_name['val'].message_type = _PDICTVAL_VALENTRY
DESCRIPTOR.message_types_by_name['PDictSet'] = _PDICTSET
DESCRIPTOR.message_types_by_name['Values'] = _VALUES
DESCRIPTOR.message_types_by_name['PDictVal'] = _PDICTVAL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PDictSet = _reflection.GeneratedProtocolMessageType('PDictSet', (_message.Message,), {
  'DESCRIPTOR' : _PDICTSET,
  '__module__' : 'pdict_pb2'
  # @@protoc_insertion_point(class_scope:PDictSet)
  })
_sym_db.RegisterMessage(PDictSet)

Values = _reflection.GeneratedProtocolMessageType('Values', (_message.Message,), {
  'DESCRIPTOR' : _VALUES,
  '__module__' : 'pdict_pb2'
  # @@protoc_insertion_point(class_scope:Values)
  })
_sym_db.RegisterMessage(Values)

PDictVal = _reflection.GeneratedProtocolMessageType('PDictVal', (_message.Message,), {

  'ValEntry' : _reflection.GeneratedProtocolMessageType('ValEntry', (_message.Message,), {
    'DESCRIPTOR' : _PDICTVAL_VALENTRY,
    '__module__' : 'pdict_pb2'
    # @@protoc_insertion_point(class_scope:PDictVal.ValEntry)
    })
  ,
  'DESCRIPTOR' : _PDICTVAL,
  '__module__' : 'pdict_pb2'
  # @@protoc_insertion_point(class_scope:PDictVal)
  })
_sym_db.RegisterMessage(PDictVal)
_sym_db.RegisterMessage(PDictVal.ValEntry)


_PDICTVAL_VALENTRY._options = None
# @@protoc_insertion_point(module_scope)
