# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.enums.access_role_pb2 import (
    AccessRoleEnum as google___ads___googleads___v6___enums___access_role_pb2___AccessRoleEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CustomerUserAccess(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    user_id: builtin___int = ...
    email_address: typing___Text = ...
    access_role: google___ads___googleads___v6___enums___access_role_pb2___AccessRoleEnum.AccessRoleValue = ...
    access_creation_date_time: typing___Text = ...
    inviter_user_email_address: typing___Text = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        user_id: typing___Optional[builtin___int] = None,
        email_address: typing___Optional[typing___Text] = None,
        access_role: typing___Optional[
            google___ads___googleads___v6___enums___access_role_pb2___AccessRoleEnum.AccessRoleValue
        ] = None,
        access_creation_date_time: typing___Optional[typing___Text] = None,
        inviter_user_email_address: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_access_creation_date_time",
            b"_access_creation_date_time",
            "_email_address",
            b"_email_address",
            "_inviter_user_email_address",
            b"_inviter_user_email_address",
            "access_creation_date_time",
            b"access_creation_date_time",
            "email_address",
            b"email_address",
            "inviter_user_email_address",
            b"inviter_user_email_address",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_access_creation_date_time",
            b"_access_creation_date_time",
            "_email_address",
            b"_email_address",
            "_inviter_user_email_address",
            b"_inviter_user_email_address",
            "access_creation_date_time",
            b"access_creation_date_time",
            "access_role",
            b"access_role",
            "email_address",
            b"email_address",
            "inviter_user_email_address",
            b"inviter_user_email_address",
            "resource_name",
            b"resource_name",
            "user_id",
            b"user_id",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_access_creation_date_time", b"_access_creation_date_time"
        ],
    ) -> typing_extensions___Literal["access_creation_date_time"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_email_address", b"_email_address"],
    ) -> typing_extensions___Literal["email_address"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_inviter_user_email_address", b"_inviter_user_email_address"
        ],
    ) -> typing_extensions___Literal["inviter_user_email_address"]: ...

type___CustomerUserAccess = CustomerUserAccess
