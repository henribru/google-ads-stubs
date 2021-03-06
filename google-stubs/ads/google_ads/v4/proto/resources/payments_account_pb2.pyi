"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.wrappers_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class PaymentsAccount(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    PAYMENTS_ACCOUNT_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    CURRENCY_CODE_FIELD_NUMBER: builtins.int
    PAYMENTS_PROFILE_ID_FIELD_NUMBER: builtins.int
    SECONDARY_PAYMENTS_PROFILE_ID_FIELD_NUMBER: builtins.int
    PAYING_MANAGER_CUSTOMER_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    @property
    def payments_account_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def name(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def currency_code(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def payments_profile_id(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def secondary_payments_profile_id(
        self,
    ) -> google.protobuf.wrappers_pb2.StringValue: ...
    @property
    def paying_manager_customer(self) -> google.protobuf.wrappers_pb2.StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        payments_account_id: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        name: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        currency_code: typing.Optional[google.protobuf.wrappers_pb2.StringValue] = ...,
        payments_profile_id: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        secondary_payments_profile_id: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
        paying_manager_customer: typing.Optional[
            google.protobuf.wrappers_pb2.StringValue
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "currency_code",
            b"currency_code",
            "name",
            b"name",
            "paying_manager_customer",
            b"paying_manager_customer",
            "payments_account_id",
            b"payments_account_id",
            "payments_profile_id",
            b"payments_profile_id",
            "secondary_payments_profile_id",
            b"secondary_payments_profile_id",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "currency_code",
            b"currency_code",
            "name",
            b"name",
            "paying_manager_customer",
            b"paying_manager_customer",
            "payments_account_id",
            b"payments_account_id",
            "payments_profile_id",
            b"payments_profile_id",
            "resource_name",
            b"resource_name",
            "secondary_payments_profile_id",
            b"secondary_payments_profile_id",
        ],
    ) -> None: ...

global___PaymentsAccount = PaymentsAccount
