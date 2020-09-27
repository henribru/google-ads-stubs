# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v2.proto.enums.keyword_plan_network_pb2 import (
    KeywordPlanNetworkEnum as google___ads___googleads___v2___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class KeywordPlanCampaign(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    keyword_plan_network: google___ads___googleads___v2___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetworkValue = ...
    @property
    def keyword_plan(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def language_constants(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def cpc_bid_micros(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def geo_targets(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___KeywordPlanGeoTarget
    ]: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        keyword_plan: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        language_constants: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        keyword_plan_network: typing___Optional[
            google___ads___googleads___v2___enums___keyword_plan_network_pb2___KeywordPlanNetworkEnum.KeywordPlanNetworkValue
        ] = None,
        cpc_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        geo_targets: typing___Optional[
            typing___Iterable[type___KeywordPlanGeoTarget]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "id",
            b"id",
            "keyword_plan",
            b"keyword_plan",
            "name",
            b"name",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "cpc_bid_micros",
            b"cpc_bid_micros",
            "geo_targets",
            b"geo_targets",
            "id",
            b"id",
            "keyword_plan",
            b"keyword_plan",
            "keyword_plan_network",
            b"keyword_plan_network",
            "language_constants",
            b"language_constants",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___KeywordPlanCampaign = KeywordPlanCampaign

class KeywordPlanGeoTarget(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def geo_target_constant(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        geo_target_constant: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "geo_target_constant", b"geo_target_constant"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "geo_target_constant", b"geo_target_constant"
        ],
    ) -> None: ...

type___KeywordPlanGeoTarget = KeywordPlanGeoTarget
