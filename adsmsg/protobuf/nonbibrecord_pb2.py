# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: nonbibrecord.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import status_pb2 as status__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='nonbibrecord.proto',
  package='adsmsg',
  syntax='proto3',
  serialized_pb=_b('\n\x12nonbibrecord.proto\x12\x06\x61\x64smsg\x1a\x0cstatus.proto\"\xf1\x03\n\x0cNonBibRecord\x12\x0f\n\x07\x62ibcode\x18\x01 \x01(\t\x12\x10\n\x08refereed\x18\x02 \x01(\x08\x12\x16\n\x0esimbad_objects\x18\x03 \x03(\t\x12\x0e\n\x06grants\x18\x04 \x03(\t\x12\x11\n\tcitations\x18\x05 \x03(\t\x12\r\n\x05\x62oost\x18\x06 \x01(\x02\x12\x16\n\x0e\x63itation_count\x18\x07 \x01(\x05\x12\x12\n\nread_count\x18\x08 \x01(\x05\x12\x0f\n\x07readers\x18\t \x03(\t\x12\x11\n\tdownloads\x18\n \x03(\x05\x12\r\n\x05reads\x18\x0b \x03(\x05\x12\x11\n\treference\x18\x0c \x03(\t\x12\x13\n\x0bned_objects\x18\r \x03(\t\x12\x0c\n\x04\x64\x61ta\x18\x0e \x03(\t\x12\x19\n\x11total_link_counts\x18\x0f \x01(\x05\x12\x37\n\ndata_links\x18\x10 \x03(\x0b\x32#.adsmsg.NonBibRecord.DataLinksEntry\x12\x0f\n\x07\x65source\x18\x11 \x03(\t\x12\x10\n\x08property\x18\x12 \x03(\t\x12\x1e\n\x06status\x18\x13 \x01(\x0e\x32\x0e.adsmsg.Status\x1aH\n\x0e\x44\x61taLinksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.adsmsg.DataLinksValue:\x02\x38\x01\"\x1f\n\x0e\x44\x61taLinksValue\x12\r\n\x05value\x18\x01 \x03(\t\"`\n\x10NonBibRecordList\x12,\n\x0enonbib_records\x18\x01 \x03(\x0b\x32\x14.adsmsg.NonBibRecord\x12\x1e\n\x06status\x18\x02 \x01(\x0e\x32\x0e.adsmsg.Statusb\x06proto3')
  ,
  dependencies=[status__pb2.DESCRIPTOR,])




_NONBIBRECORD_DATALINKSENTRY = _descriptor.Descriptor(
  name='DataLinksEntry',
  full_name='adsmsg.NonBibRecord.DataLinksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='adsmsg.NonBibRecord.DataLinksEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='adsmsg.NonBibRecord.DataLinksEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=470,
  serialized_end=542,
)

_NONBIBRECORD = _descriptor.Descriptor(
  name='NonBibRecord',
  full_name='adsmsg.NonBibRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bibcode', full_name='adsmsg.NonBibRecord.bibcode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='refereed', full_name='adsmsg.NonBibRecord.refereed', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='simbad_objects', full_name='adsmsg.NonBibRecord.simbad_objects', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='grants', full_name='adsmsg.NonBibRecord.grants', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citations', full_name='adsmsg.NonBibRecord.citations', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='boost', full_name='adsmsg.NonBibRecord.boost', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='citation_count', full_name='adsmsg.NonBibRecord.citation_count', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_count', full_name='adsmsg.NonBibRecord.read_count', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='readers', full_name='adsmsg.NonBibRecord.readers', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='downloads', full_name='adsmsg.NonBibRecord.downloads', index=9,
      number=10, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reads', full_name='adsmsg.NonBibRecord.reads', index=10,
      number=11, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference', full_name='adsmsg.NonBibRecord.reference', index=11,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ned_objects', full_name='adsmsg.NonBibRecord.ned_objects', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data', full_name='adsmsg.NonBibRecord.data', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='total_link_counts', full_name='adsmsg.NonBibRecord.total_link_counts', index=14,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_links', full_name='adsmsg.NonBibRecord.data_links', index=15,
      number=16, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='esource', full_name='adsmsg.NonBibRecord.esource', index=16,
      number=17, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='property', full_name='adsmsg.NonBibRecord.property', index=17,
      number=18, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.NonBibRecord.status', index=18,
      number=19, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_NONBIBRECORD_DATALINKSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=542,
)


_DATALINKSVALUE = _descriptor.Descriptor(
  name='DataLinksValue',
  full_name='adsmsg.DataLinksValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='adsmsg.DataLinksValue.value', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=544,
  serialized_end=575,
)


_NONBIBRECORDLIST = _descriptor.Descriptor(
  name='NonBibRecordList',
  full_name='adsmsg.NonBibRecordList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nonbib_records', full_name='adsmsg.NonBibRecordList.nonbib_records', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='adsmsg.NonBibRecordList.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=577,
  serialized_end=673,
)

_NONBIBRECORD_DATALINKSENTRY.fields_by_name['value'].message_type = _DATALINKSVALUE
_NONBIBRECORD_DATALINKSENTRY.containing_type = _NONBIBRECORD
_NONBIBRECORD.fields_by_name['data_links'].message_type = _NONBIBRECORD_DATALINKSENTRY
_NONBIBRECORD.fields_by_name['status'].enum_type = status__pb2._STATUS
_NONBIBRECORDLIST.fields_by_name['nonbib_records'].message_type = _NONBIBRECORD
_NONBIBRECORDLIST.fields_by_name['status'].enum_type = status__pb2._STATUS
DESCRIPTOR.message_types_by_name['NonBibRecord'] = _NONBIBRECORD
DESCRIPTOR.message_types_by_name['DataLinksValue'] = _DATALINKSVALUE
DESCRIPTOR.message_types_by_name['NonBibRecordList'] = _NONBIBRECORDLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NonBibRecord = _reflection.GeneratedProtocolMessageType('NonBibRecord', (_message.Message,), dict(

  DataLinksEntry = _reflection.GeneratedProtocolMessageType('DataLinksEntry', (_message.Message,), dict(
    DESCRIPTOR = _NONBIBRECORD_DATALINKSENTRY,
    __module__ = 'nonbibrecord_pb2'
    # @@protoc_insertion_point(class_scope:adsmsg.NonBibRecord.DataLinksEntry)
    ))
  ,
  DESCRIPTOR = _NONBIBRECORD,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.NonBibRecord)
  ))
_sym_db.RegisterMessage(NonBibRecord)
_sym_db.RegisterMessage(NonBibRecord.DataLinksEntry)

DataLinksValue = _reflection.GeneratedProtocolMessageType('DataLinksValue', (_message.Message,), dict(
  DESCRIPTOR = _DATALINKSVALUE,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.DataLinksValue)
  ))
_sym_db.RegisterMessage(DataLinksValue)

NonBibRecordList = _reflection.GeneratedProtocolMessageType('NonBibRecordList', (_message.Message,), dict(
  DESCRIPTOR = _NONBIBRECORDLIST,
  __module__ = 'nonbibrecord_pb2'
  # @@protoc_insertion_point(class_scope:adsmsg.NonBibRecordList)
  ))
_sym_db.RegisterMessage(NonBibRecordList)


_NONBIBRECORD_DATALINKSENTRY.has_options = True
_NONBIBRECORD_DATALINKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
