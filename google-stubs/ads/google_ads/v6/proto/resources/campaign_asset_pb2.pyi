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

from google.ads.google_ads.v6.proto.enums.asset_field_type_pb2 import (
    AssetFieldTypeEnum as google___ads___googleads___v6___enums___asset_field_type_pb2___AssetFieldTypeEnum,
)
from google.ads.google_ads.v6.proto.enums.asset_link_status_pb2 import (
    AssetLinkStatusEnum as google___ads___googleads___v6___enums___asset_link_status_pb2___AssetLinkStatusEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CampaignAsset(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    campaign: typing___Text = ...
    asset: typing___Text = ...
    field_type: google___ads___googleads___v6___enums___asset_field_type_pb2___AssetFieldTypeEnum.AssetFieldTypeValue = ...
    status: google___ads___googleads___v6___enums___asset_link_status_pb2___AssetLinkStatusEnum.AssetLinkStatusValue = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        campaign: typing___Optional[typing___Text] = None,
        asset: typing___Optional[typing___Text] = None,
        field_type: typing___Optional[
            google___ads___googleads___v6___enums___asset_field_type_pb2___AssetFieldTypeEnum.AssetFieldTypeValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v6___enums___asset_link_status_pb2___AssetLinkStatusEnum.AssetLinkStatusValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_asset",
            b"_asset",
            "_campaign",
            b"_campaign",
            "asset",
            b"asset",
            "campaign",
            b"campaign",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_asset",
            b"_asset",
            "_campaign",
            b"_campaign",
            "asset",
            b"asset",
            "campaign",
            b"campaign",
            "field_type",
            b"field_type",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_asset", b"_asset"]
    ) -> typing_extensions___Literal["asset"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_campaign", b"_campaign"]
    ) -> typing_extensions___Literal["campaign"]: ...

type___CampaignAsset = CampaignAsset
