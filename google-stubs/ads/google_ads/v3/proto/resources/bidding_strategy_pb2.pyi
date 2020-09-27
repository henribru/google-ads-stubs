# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v3.proto.common.bidding_pb2 import (
    EnhancedCpc as google___ads___googleads___v3___common___bidding_pb2___EnhancedCpc,
    TargetCpa as google___ads___googleads___v3___common___bidding_pb2___TargetCpa,
    TargetImpressionShare as google___ads___googleads___v3___common___bidding_pb2___TargetImpressionShare,
    TargetRoas as google___ads___googleads___v3___common___bidding_pb2___TargetRoas,
    TargetSpend as google___ads___googleads___v3___common___bidding_pb2___TargetSpend,
)
from google.ads.google_ads.v3.proto.enums.bidding_strategy_status_pb2 import (
    BiddingStrategyStatusEnum as google___ads___googleads___v3___enums___bidding_strategy_status_pb2___BiddingStrategyStatusEnum,
)
from google.ads.google_ads.v3.proto.enums.bidding_strategy_type_pb2 import (
    BiddingStrategyTypeEnum as google___ads___googleads___v3___enums___bidding_strategy_type_pb2___BiddingStrategyTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class BiddingStrategy(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    status: google___ads___googleads___v3___enums___bidding_strategy_status_pb2___BiddingStrategyStatusEnum.BiddingStrategyStatusValue = ...
    type: google___ads___googleads___v3___enums___bidding_strategy_type_pb2___BiddingStrategyTypeEnum.BiddingStrategyTypeValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def campaign_count(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def non_removed_campaign_count(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def enhanced_cpc(
        self,
    ) -> google___ads___googleads___v3___common___bidding_pb2___EnhancedCpc: ...
    @property
    def target_cpa(
        self,
    ) -> google___ads___googleads___v3___common___bidding_pb2___TargetCpa: ...
    @property
    def target_impression_share(
        self,
    ) -> google___ads___googleads___v3___common___bidding_pb2___TargetImpressionShare: ...
    @property
    def target_roas(
        self,
    ) -> google___ads___googleads___v3___common___bidding_pb2___TargetRoas: ...
    @property
    def target_spend(
        self,
    ) -> google___ads___googleads___v3___common___bidding_pb2___TargetSpend: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        status: typing___Optional[
            google___ads___googleads___v3___enums___bidding_strategy_status_pb2___BiddingStrategyStatusEnum.BiddingStrategyStatusValue
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v3___enums___bidding_strategy_type_pb2___BiddingStrategyTypeEnum.BiddingStrategyTypeValue
        ] = None,
        campaign_count: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        non_removed_campaign_count: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        enhanced_cpc: typing___Optional[
            google___ads___googleads___v3___common___bidding_pb2___EnhancedCpc
        ] = None,
        target_cpa: typing___Optional[
            google___ads___googleads___v3___common___bidding_pb2___TargetCpa
        ] = None,
        target_impression_share: typing___Optional[
            google___ads___googleads___v3___common___bidding_pb2___TargetImpressionShare
        ] = None,
        target_roas: typing___Optional[
            google___ads___googleads___v3___common___bidding_pb2___TargetRoas
        ] = None,
        target_spend: typing___Optional[
            google___ads___googleads___v3___common___bidding_pb2___TargetSpend
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_count",
            b"campaign_count",
            "enhanced_cpc",
            b"enhanced_cpc",
            "id",
            b"id",
            "name",
            b"name",
            "non_removed_campaign_count",
            b"non_removed_campaign_count",
            "scheme",
            b"scheme",
            "target_cpa",
            b"target_cpa",
            "target_impression_share",
            b"target_impression_share",
            "target_roas",
            b"target_roas",
            "target_spend",
            b"target_spend",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_count",
            b"campaign_count",
            "enhanced_cpc",
            b"enhanced_cpc",
            "id",
            b"id",
            "name",
            b"name",
            "non_removed_campaign_count",
            b"non_removed_campaign_count",
            "resource_name",
            b"resource_name",
            "scheme",
            b"scheme",
            "status",
            b"status",
            "target_cpa",
            b"target_cpa",
            "target_impression_share",
            b"target_impression_share",
            "target_roas",
            b"target_roas",
            "target_spend",
            b"target_spend",
            "type",
            b"type",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["scheme", b"scheme"]
    ) -> typing_extensions___Literal[
        "enhanced_cpc",
        "target_cpa",
        "target_impression_share",
        "target_roas",
        "target_spend",
    ]: ...

type___BiddingStrategy = BiddingStrategy