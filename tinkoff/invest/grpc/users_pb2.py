# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tinkoff/invest/grpc/users.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from tinkoff.invest.grpc import common_pb2 as tinkoff_dot_invest_dot_grpc_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tinkoff/invest/grpc/users.proto',
  package='tinkoff.public.invest.api.contract.v1',
  syntax='proto3',
  serialized_options=b'\n\034ru.tinkoff.piapi.contract.v1P\001Z\021Tinkoff/investAPI\242\002\005TIAPI\252\002\024Tinkoff.InvestAPI.V1\312\002\021Tinkoff\\Invest\\V1',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1ftinkoff/invest/grpc/users.proto\x12%tinkoff.public.invest.api.contract.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a tinkoff/invest/grpc/common.proto\"\x14\n\x12GetAccountsRequest\"W\n\x13GetAccountsResponse\x12@\n\x08\x61\x63\x63ounts\x18\x01 \x03(\x0b\x32..tinkoff.public.invest.api.contract.v1.Account\"\x8d\x02\n\x07\x41\x63\x63ount\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.tinkoff.public.invest.api.contract.v1.AccountType\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x44\n\x06status\x18\x04 \x01(\x0e\x32\x34.tinkoff.public.invest.api.contract.v1.AccountStatus\x12/\n\x0bopened_date\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12/\n\x0b\x63losed_date\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"0\n\x1aGetMarginAttributesRequest\x12\x12\n\naccount_id\x18\x01 \x01(\t\"\xa8\x03\n\x1bGetMarginAttributesResponse\x12K\n\x10liquid_portfolio\x18\x01 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12J\n\x0fstarting_margin\x18\x02 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12I\n\x0eminimal_margin\x18\x03 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\x12Q\n\x17\x66unds_sufficiency_level\x18\x04 \x01(\x0b\x32\x30.tinkoff.public.invest.api.contract.v1.Quotation\x12R\n\x17\x61mount_of_missing_funds\x18\x05 \x01(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.MoneyValue\"\x16\n\x14GetUserTariffRequest\"\xab\x01\n\x15GetUserTariffResponse\x12G\n\x0cunary_limits\x18\x01 \x03(\x0b\x32\x31.tinkoff.public.invest.api.contract.v1.UnaryLimit\x12I\n\rstream_limits\x18\x02 \x03(\x0b\x32\x32.tinkoff.public.invest.api.contract.v1.StreamLimit\"7\n\nUnaryLimit\x12\x18\n\x10limit_per_minute\x18\x01 \x01(\x05\x12\x0f\n\x07methods\x18\x02 \x03(\t\"-\n\x0bStreamLimit\x12\r\n\x05limit\x18\x01 \x01(\x05\x12\x0f\n\x07streams\x18\x02 \x03(\t\"\x10\n\x0eGetInfoRequest\"\\\n\x0fGetInfoResponse\x12\x13\n\x0bprem_status\x18\x01 \x01(\x08\x12\x13\n\x0bqual_status\x18\x02 \x01(\x08\x12\x1f\n\x17qualified_for_work_with\x18\x03 \x03(\t*\x80\x01\n\x0b\x41\x63\x63ountType\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_UNSPECIFIED\x10\x00\x12\x18\n\x14\x41\x43\x43OUNT_TYPE_TINKOFF\x10\x01\x12\x1c\n\x18\x41\x43\x43OUNT_TYPE_TINKOFF_IIS\x10\x02\x12\x1b\n\x17\x41\x43\x43OUNT_TYPE_INVEST_BOX\x10\x03*{\n\rAccountStatus\x12\x1e\n\x1a\x41\x43\x43OUNT_STATUS_UNSPECIFIED\x10\x00\x12\x16\n\x12\x41\x43\x43OUNT_STATUS_NEW\x10\x01\x12\x17\n\x13\x41\x43\x43OUNT_STATUS_OPEN\x10\x02\x12\x19\n\x15\x41\x43\x43OUNT_STATUS_CLOSED\x10\x03\x32\xbb\x04\n\x0cUsersService\x12\x84\x01\n\x0bGetAccounts\x12\x39.tinkoff.public.invest.api.contract.v1.GetAccountsRequest\x1a:.tinkoff.public.invest.api.contract.v1.GetAccountsResponse\x12\x9c\x01\n\x13GetMarginAttributes\x12\x41.tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest\x1a\x42.tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse\x12\x8a\x01\n\rGetUserTariff\x12;.tinkoff.public.invest.api.contract.v1.GetUserTariffRequest\x1a<.tinkoff.public.invest.api.contract.v1.GetUserTariffResponse\x12x\n\x07GetInfo\x12\x35.tinkoff.public.invest.api.contract.v1.GetInfoRequest\x1a\x36.tinkoff.public.invest.api.contract.v1.GetInfoResponseBf\n\x1cru.tinkoff.piapi.contract.v1P\x01Z\x11Tinkoff/investAPI\xa2\x02\x05TIAPI\xaa\x02\x14Tinkoff.InvestAPI.V1\xca\x02\x11Tinkoff\\Invest\\V1b\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,tinkoff_dot_invest_dot_grpc_dot_common__pb2.DESCRIPTOR,])

_ACCOUNTTYPE = _descriptor.EnumDescriptor(
  name='AccountType',
  full_name='tinkoff.public.invest.api.contract.v1.AccountType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_TYPE_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_TYPE_TINKOFF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_TYPE_TINKOFF_IIS', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_TYPE_INVEST_BOX', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1416,
  serialized_end=1544,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTTYPE)

AccountType = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTTYPE)
_ACCOUNTSTATUS = _descriptor.EnumDescriptor(
  name='AccountStatus',
  full_name='tinkoff.public.invest.api.contract.v1.AccountStatus',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_STATUS_UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_STATUS_NEW', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_STATUS_OPEN', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACCOUNT_STATUS_CLOSED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1546,
  serialized_end=1669,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTSTATUS)

AccountStatus = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTSTATUS)
ACCOUNT_TYPE_UNSPECIFIED = 0
ACCOUNT_TYPE_TINKOFF = 1
ACCOUNT_TYPE_TINKOFF_IIS = 2
ACCOUNT_TYPE_INVEST_BOX = 3
ACCOUNT_STATUS_UNSPECIFIED = 0
ACCOUNT_STATUS_NEW = 1
ACCOUNT_STATUS_OPEN = 2
ACCOUNT_STATUS_CLOSED = 3



_GETACCOUNTSREQUEST = _descriptor.Descriptor(
  name='GetAccountsRequest',
  full_name='tinkoff.public.invest.api.contract.v1.GetAccountsRequest',
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
  serialized_start=141,
  serialized_end=161,
)


_GETACCOUNTSRESPONSE = _descriptor.Descriptor(
  name='GetAccountsResponse',
  full_name='tinkoff.public.invest.api.contract.v1.GetAccountsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accounts', full_name='tinkoff.public.invest.api.contract.v1.GetAccountsResponse.accounts', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=163,
  serialized_end=250,
)


_ACCOUNT = _descriptor.Descriptor(
  name='Account',
  full_name='tinkoff.public.invest.api.contract.v1.Account',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tinkoff.public.invest.api.contract.v1.Account.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='type', full_name='tinkoff.public.invest.api.contract.v1.Account.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='tinkoff.public.invest.api.contract.v1.Account.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='status', full_name='tinkoff.public.invest.api.contract.v1.Account.status', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='opened_date', full_name='tinkoff.public.invest.api.contract.v1.Account.opened_date', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='closed_date', full_name='tinkoff.public.invest.api.contract.v1.Account.closed_date', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=253,
  serialized_end=522,
)


_GETMARGINATTRIBUTESREQUEST = _descriptor.Descriptor(
  name='GetMarginAttributesRequest',
  full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest.account_id', index=0,
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
  serialized_start=524,
  serialized_end=572,
)


_GETMARGINATTRIBUTESRESPONSE = _descriptor.Descriptor(
  name='GetMarginAttributesResponse',
  full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='liquid_portfolio', full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse.liquid_portfolio', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='starting_margin', full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse.starting_margin', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minimal_margin', full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse.minimal_margin', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='funds_sufficiency_level', full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse.funds_sufficiency_level', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='amount_of_missing_funds', full_name='tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse.amount_of_missing_funds', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=575,
  serialized_end=999,
)


_GETUSERTARIFFREQUEST = _descriptor.Descriptor(
  name='GetUserTariffRequest',
  full_name='tinkoff.public.invest.api.contract.v1.GetUserTariffRequest',
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
  serialized_start=1001,
  serialized_end=1023,
)


_GETUSERTARIFFRESPONSE = _descriptor.Descriptor(
  name='GetUserTariffResponse',
  full_name='tinkoff.public.invest.api.contract.v1.GetUserTariffResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='unary_limits', full_name='tinkoff.public.invest.api.contract.v1.GetUserTariffResponse.unary_limits', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stream_limits', full_name='tinkoff.public.invest.api.contract.v1.GetUserTariffResponse.stream_limits', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1026,
  serialized_end=1197,
)


_UNARYLIMIT = _descriptor.Descriptor(
  name='UnaryLimit',
  full_name='tinkoff.public.invest.api.contract.v1.UnaryLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit_per_minute', full_name='tinkoff.public.invest.api.contract.v1.UnaryLimit.limit_per_minute', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='methods', full_name='tinkoff.public.invest.api.contract.v1.UnaryLimit.methods', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=1199,
  serialized_end=1254,
)


_STREAMLIMIT = _descriptor.Descriptor(
  name='StreamLimit',
  full_name='tinkoff.public.invest.api.contract.v1.StreamLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='limit', full_name='tinkoff.public.invest.api.contract.v1.StreamLimit.limit', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='streams', full_name='tinkoff.public.invest.api.contract.v1.StreamLimit.streams', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=1256,
  serialized_end=1301,
)


_GETINFOREQUEST = _descriptor.Descriptor(
  name='GetInfoRequest',
  full_name='tinkoff.public.invest.api.contract.v1.GetInfoRequest',
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
  serialized_start=1303,
  serialized_end=1319,
)


_GETINFORESPONSE = _descriptor.Descriptor(
  name='GetInfoResponse',
  full_name='tinkoff.public.invest.api.contract.v1.GetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='prem_status', full_name='tinkoff.public.invest.api.contract.v1.GetInfoResponse.prem_status', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qual_status', full_name='tinkoff.public.invest.api.contract.v1.GetInfoResponse.qual_status', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='qualified_for_work_with', full_name='tinkoff.public.invest.api.contract.v1.GetInfoResponse.qualified_for_work_with', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=1321,
  serialized_end=1413,
)

_GETACCOUNTSRESPONSE.fields_by_name['accounts'].message_type = _ACCOUNT
_ACCOUNT.fields_by_name['type'].enum_type = _ACCOUNTTYPE
_ACCOUNT.fields_by_name['status'].enum_type = _ACCOUNTSTATUS
_ACCOUNT.fields_by_name['opened_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACCOUNT.fields_by_name['closed_date'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETMARGINATTRIBUTESRESPONSE.fields_by_name['liquid_portfolio'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._MONEYVALUE
_GETMARGINATTRIBUTESRESPONSE.fields_by_name['starting_margin'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._MONEYVALUE
_GETMARGINATTRIBUTESRESPONSE.fields_by_name['minimal_margin'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._MONEYVALUE
_GETMARGINATTRIBUTESRESPONSE.fields_by_name['funds_sufficiency_level'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._QUOTATION
_GETMARGINATTRIBUTESRESPONSE.fields_by_name['amount_of_missing_funds'].message_type = tinkoff_dot_invest_dot_grpc_dot_common__pb2._MONEYVALUE
_GETUSERTARIFFRESPONSE.fields_by_name['unary_limits'].message_type = _UNARYLIMIT
_GETUSERTARIFFRESPONSE.fields_by_name['stream_limits'].message_type = _STREAMLIMIT
DESCRIPTOR.message_types_by_name['GetAccountsRequest'] = _GETACCOUNTSREQUEST
DESCRIPTOR.message_types_by_name['GetAccountsResponse'] = _GETACCOUNTSRESPONSE
DESCRIPTOR.message_types_by_name['Account'] = _ACCOUNT
DESCRIPTOR.message_types_by_name['GetMarginAttributesRequest'] = _GETMARGINATTRIBUTESREQUEST
DESCRIPTOR.message_types_by_name['GetMarginAttributesResponse'] = _GETMARGINATTRIBUTESRESPONSE
DESCRIPTOR.message_types_by_name['GetUserTariffRequest'] = _GETUSERTARIFFREQUEST
DESCRIPTOR.message_types_by_name['GetUserTariffResponse'] = _GETUSERTARIFFRESPONSE
DESCRIPTOR.message_types_by_name['UnaryLimit'] = _UNARYLIMIT
DESCRIPTOR.message_types_by_name['StreamLimit'] = _STREAMLIMIT
DESCRIPTOR.message_types_by_name['GetInfoRequest'] = _GETINFOREQUEST
DESCRIPTOR.message_types_by_name['GetInfoResponse'] = _GETINFORESPONSE
DESCRIPTOR.enum_types_by_name['AccountType'] = _ACCOUNTTYPE
DESCRIPTOR.enum_types_by_name['AccountStatus'] = _ACCOUNTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GetAccountsRequest = _reflection.GeneratedProtocolMessageType('GetAccountsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetAccountsRequest)
  })
_sym_db.RegisterMessage(GetAccountsRequest)

GetAccountsResponse = _reflection.GeneratedProtocolMessageType('GetAccountsResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETACCOUNTSRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetAccountsResponse)
  })
_sym_db.RegisterMessage(GetAccountsResponse)

Account = _reflection.GeneratedProtocolMessageType('Account', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNT,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.Account)
  })
_sym_db.RegisterMessage(Account)

GetMarginAttributesRequest = _reflection.GeneratedProtocolMessageType('GetMarginAttributesRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETMARGINATTRIBUTESREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetMarginAttributesRequest)
  })
_sym_db.RegisterMessage(GetMarginAttributesRequest)

GetMarginAttributesResponse = _reflection.GeneratedProtocolMessageType('GetMarginAttributesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMARGINATTRIBUTESRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetMarginAttributesResponse)
  })
_sym_db.RegisterMessage(GetMarginAttributesResponse)

GetUserTariffRequest = _reflection.GeneratedProtocolMessageType('GetUserTariffRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERTARIFFREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetUserTariffRequest)
  })
_sym_db.RegisterMessage(GetUserTariffRequest)

GetUserTariffResponse = _reflection.GeneratedProtocolMessageType('GetUserTariffResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETUSERTARIFFRESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetUserTariffResponse)
  })
_sym_db.RegisterMessage(GetUserTariffResponse)

UnaryLimit = _reflection.GeneratedProtocolMessageType('UnaryLimit', (_message.Message,), {
  'DESCRIPTOR' : _UNARYLIMIT,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.UnaryLimit)
  })
_sym_db.RegisterMessage(UnaryLimit)

StreamLimit = _reflection.GeneratedProtocolMessageType('StreamLimit', (_message.Message,), {
  'DESCRIPTOR' : _STREAMLIMIT,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.StreamLimit)
  })
_sym_db.RegisterMessage(StreamLimit)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETINFOREQUEST,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetInfoRequest)
  })
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETINFORESPONSE,
  '__module__' : 'tinkoff.invest.grpc.users_pb2'
  # @@protoc_insertion_point(class_scope:tinkoff.public.invest.api.contract.v1.GetInfoResponse)
  })
_sym_db.RegisterMessage(GetInfoResponse)


DESCRIPTOR._options = None

_USERSSERVICE = _descriptor.ServiceDescriptor(
  name='UsersService',
  full_name='tinkoff.public.invest.api.contract.v1.UsersService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1672,
  serialized_end=2243,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetAccounts',
    full_name='tinkoff.public.invest.api.contract.v1.UsersService.GetAccounts',
    index=0,
    containing_service=None,
    input_type=_GETACCOUNTSREQUEST,
    output_type=_GETACCOUNTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetMarginAttributes',
    full_name='tinkoff.public.invest.api.contract.v1.UsersService.GetMarginAttributes',
    index=1,
    containing_service=None,
    input_type=_GETMARGINATTRIBUTESREQUEST,
    output_type=_GETMARGINATTRIBUTESRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetUserTariff',
    full_name='tinkoff.public.invest.api.contract.v1.UsersService.GetUserTariff',
    index=2,
    containing_service=None,
    input_type=_GETUSERTARIFFREQUEST,
    output_type=_GETUSERTARIFFRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetInfo',
    full_name='tinkoff.public.invest.api.contract.v1.UsersService.GetInfo',
    index=3,
    containing_service=None,
    input_type=_GETINFOREQUEST,
    output_type=_GETINFORESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_USERSSERVICE)

DESCRIPTOR.services_by_name['UsersService'] = _USERSSERVICE

# @@protoc_insertion_point(module_scope)