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

from google.ads.google_ads.v6.proto.enums.merchant_center_link_status_pb2 import (
    MerchantCenterLinkStatusEnum as google___ads___googleads___v6___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class MerchantCenterLink(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    merchant_center_account_name: typing___Text = ...
    status: google___ads___googleads___v6___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        merchant_center_account_name: typing___Optional[typing___Text] = None,
        status: typing___Optional[
            google___ads___googleads___v6___enums___merchant_center_link_status_pb2___MerchantCenterLinkStatusEnum.MerchantCenterLinkStatusValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_merchant_center_account_name",
            b"_merchant_center_account_name",
            "id",
            b"id",
            "merchant_center_account_name",
            b"merchant_center_account_name",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_id",
            b"_id",
            "_merchant_center_account_name",
            b"_merchant_center_account_name",
            "id",
            b"id",
            "merchant_center_account_name",
            b"merchant_center_account_name",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_merchant_center_account_name", b"_merchant_center_account_name"
        ],
    ) -> typing_extensions___Literal["merchant_center_account_name"]: ...

type___MerchantCenterLink = MerchantCenterLink
