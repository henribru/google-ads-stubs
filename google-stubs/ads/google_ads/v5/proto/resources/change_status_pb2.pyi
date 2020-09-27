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
from google.protobuf.wrappers_pb2 import (
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.change_status_operation_pb2 import (
    ChangeStatusOperationEnum as google___ads___googleads___v5___enums___change_status_operation_pb2___ChangeStatusOperationEnum,
)
from google.ads.google_ads.v5.proto.enums.change_status_resource_type_pb2 import (
    ChangeStatusResourceTypeEnum as google___ads___googleads___v5___enums___change_status_resource_type_pb2___ChangeStatusResourceTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class ChangeStatus(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    resource_type: google___ads___googleads___v5___enums___change_status_resource_type_pb2___ChangeStatusResourceTypeEnum.ChangeStatusResourceTypeValue = ...
    campaign: typing___Text = ...
    ad_group: typing___Text = ...
    resource_status: google___ads___googleads___v5___enums___change_status_operation_pb2___ChangeStatusOperationEnum.ChangeStatusOperationValue = ...
    @property
    def last_change_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def ad_group_ad(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def ad_group_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def campaign_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def feed_item(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def ad_group_feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def campaign_feed(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def ad_group_bid_modifier(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        last_change_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        resource_type: typing___Optional[
            google___ads___googleads___v5___enums___change_status_resource_type_pb2___ChangeStatusResourceTypeEnum.ChangeStatusResourceTypeValue
        ] = None,
        campaign: typing___Optional[typing___Text] = None,
        ad_group: typing___Optional[typing___Text] = None,
        resource_status: typing___Optional[
            google___ads___googleads___v5___enums___change_status_operation_pb2___ChangeStatusOperationEnum.ChangeStatusOperationValue
        ] = None,
        ad_group_ad: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        ad_group_criterion: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        campaign_criterion: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        feed: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        feed_item: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        ad_group_feed: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        campaign_feed: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        ad_group_bid_modifier: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_group",
            b"_ad_group",
            "_campaign",
            b"_campaign",
            "ad_group",
            b"ad_group",
            "ad_group_ad",
            b"ad_group_ad",
            "ad_group_bid_modifier",
            b"ad_group_bid_modifier",
            "ad_group_criterion",
            b"ad_group_criterion",
            "ad_group_feed",
            b"ad_group_feed",
            "campaign",
            b"campaign",
            "campaign_criterion",
            b"campaign_criterion",
            "campaign_feed",
            b"campaign_feed",
            "feed",
            b"feed",
            "feed_item",
            b"feed_item",
            "last_change_date_time",
            b"last_change_date_time",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_group",
            b"_ad_group",
            "_campaign",
            b"_campaign",
            "ad_group",
            b"ad_group",
            "ad_group_ad",
            b"ad_group_ad",
            "ad_group_bid_modifier",
            b"ad_group_bid_modifier",
            "ad_group_criterion",
            b"ad_group_criterion",
            "ad_group_feed",
            b"ad_group_feed",
            "campaign",
            b"campaign",
            "campaign_criterion",
            b"campaign_criterion",
            "campaign_feed",
            b"campaign_feed",
            "feed",
            b"feed",
            "feed_item",
            b"feed_item",
            "last_change_date_time",
            b"last_change_date_time",
            "resource_name",
            b"resource_name",
            "resource_status",
            b"resource_status",
            "resource_type",
            b"resource_type",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_ad_group", b"_ad_group"]
    ) -> typing_extensions___Literal["ad_group"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_campaign", b"_campaign"]
    ) -> typing_extensions___Literal["campaign"]: ...

type___ChangeStatus = ChangeStatus
