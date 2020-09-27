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

from google.ads.google_ads.v2.proto.common.simulation_pb2 import (
    CpcBidSimulationPointList as google___ads___googleads___v2___common___simulation_pb2___CpcBidSimulationPointList,
)
from google.ads.google_ads.v2.proto.enums.simulation_modification_method_pb2 import (
    SimulationModificationMethodEnum as google___ads___googleads___v2___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum,
)
from google.ads.google_ads.v2.proto.enums.simulation_type_pb2 import (
    SimulationTypeEnum as google___ads___googleads___v2___enums___simulation_type_pb2___SimulationTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AdGroupCriterionSimulation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    type: google___ads___googleads___v2___enums___simulation_type_pb2___SimulationTypeEnum.SimulationTypeValue = ...
    modification_method: google___ads___googleads___v2___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethodValue = ...
    @property
    def ad_group_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def criterion_id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def cpc_bid_point_list(
        self,
    ) -> google___ads___googleads___v2___common___simulation_pb2___CpcBidSimulationPointList: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad_group_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        criterion_id: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___simulation_type_pb2___SimulationTypeEnum.SimulationTypeValue
        ] = None,
        modification_method: typing___Optional[
            google___ads___googleads___v2___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethodValue
        ] = None,
        start_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        end_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        cpc_bid_point_list: typing___Optional[
            google___ads___googleads___v2___common___simulation_pb2___CpcBidSimulationPointList
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "criterion_id",
            b"criterion_id",
            "end_date",
            b"end_date",
            "point_list",
            b"point_list",
            "start_date",
            b"start_date",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "criterion_id",
            b"criterion_id",
            "end_date",
            b"end_date",
            "modification_method",
            b"modification_method",
            "point_list",
            b"point_list",
            "resource_name",
            b"resource_name",
            "start_date",
            b"start_date",
            "type",
            b"type",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["point_list", b"point_list"]
    ) -> typing_extensions___Literal["cpc_bid_point_list"]: ...

type___AdGroupCriterionSimulation = AdGroupCriterionSimulation
