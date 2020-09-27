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

from google.ads.google_ads.v5.proto.common.simulation_pb2 import (
    CpcBidSimulationPointList as google___ads___googleads___v5___common___simulation_pb2___CpcBidSimulationPointList,
    CpvBidSimulationPointList as google___ads___googleads___v5___common___simulation_pb2___CpvBidSimulationPointList,
    TargetCpaSimulationPointList as google___ads___googleads___v5___common___simulation_pb2___TargetCpaSimulationPointList,
    TargetRoasSimulationPointList as google___ads___googleads___v5___common___simulation_pb2___TargetRoasSimulationPointList,
)
from google.ads.google_ads.v5.proto.enums.simulation_modification_method_pb2 import (
    SimulationModificationMethodEnum as google___ads___googleads___v5___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum,
)
from google.ads.google_ads.v5.proto.enums.simulation_type_pb2 import (
    SimulationTypeEnum as google___ads___googleads___v5___enums___simulation_type_pb2___SimulationTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class AdGroupSimulation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    ad_group_id: builtin___int = ...
    type: google___ads___googleads___v5___enums___simulation_type_pb2___SimulationTypeEnum.SimulationTypeValue = ...
    modification_method: google___ads___googleads___v5___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethodValue = ...
    start_date: typing___Text = ...
    end_date: typing___Text = ...
    @property
    def cpc_bid_point_list(
        self,
    ) -> google___ads___googleads___v5___common___simulation_pb2___CpcBidSimulationPointList: ...
    @property
    def cpv_bid_point_list(
        self,
    ) -> google___ads___googleads___v5___common___simulation_pb2___CpvBidSimulationPointList: ...
    @property
    def target_cpa_point_list(
        self,
    ) -> google___ads___googleads___v5___common___simulation_pb2___TargetCpaSimulationPointList: ...
    @property
    def target_roas_point_list(
        self,
    ) -> google___ads___googleads___v5___common___simulation_pb2___TargetRoasSimulationPointList: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        ad_group_id: typing___Optional[builtin___int] = None,
        type: typing___Optional[
            google___ads___googleads___v5___enums___simulation_type_pb2___SimulationTypeEnum.SimulationTypeValue
        ] = None,
        modification_method: typing___Optional[
            google___ads___googleads___v5___enums___simulation_modification_method_pb2___SimulationModificationMethodEnum.SimulationModificationMethodValue
        ] = None,
        start_date: typing___Optional[typing___Text] = None,
        end_date: typing___Optional[typing___Text] = None,
        cpc_bid_point_list: typing___Optional[
            google___ads___googleads___v5___common___simulation_pb2___CpcBidSimulationPointList
        ] = None,
        cpv_bid_point_list: typing___Optional[
            google___ads___googleads___v5___common___simulation_pb2___CpvBidSimulationPointList
        ] = None,
        target_cpa_point_list: typing___Optional[
            google___ads___googleads___v5___common___simulation_pb2___TargetCpaSimulationPointList
        ] = None,
        target_roas_point_list: typing___Optional[
            google___ads___googleads___v5___common___simulation_pb2___TargetRoasSimulationPointList
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_group_id",
            b"_ad_group_id",
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "cpv_bid_point_list",
            b"cpv_bid_point_list",
            "end_date",
            b"end_date",
            "point_list",
            b"point_list",
            "start_date",
            b"start_date",
            "target_cpa_point_list",
            b"target_cpa_point_list",
            "target_roas_point_list",
            b"target_roas_point_list",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_ad_group_id",
            b"_ad_group_id",
            "_end_date",
            b"_end_date",
            "_start_date",
            b"_start_date",
            "ad_group_id",
            b"ad_group_id",
            "cpc_bid_point_list",
            b"cpc_bid_point_list",
            "cpv_bid_point_list",
            b"cpv_bid_point_list",
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
            "target_cpa_point_list",
            b"target_cpa_point_list",
            "target_roas_point_list",
            b"target_roas_point_list",
            "type",
            b"type",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_ad_group_id", b"_ad_group_id"]
    ) -> typing_extensions___Literal["ad_group_id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_end_date", b"_end_date"]
    ) -> typing_extensions___Literal["end_date"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_start_date", b"_start_date"]
    ) -> typing_extensions___Literal["start_date"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["point_list", b"point_list"]
    ) -> typing_extensions___Literal[
        "cpc_bid_point_list",
        "cpv_bid_point_list",
        "target_cpa_point_list",
        "target_roas_point_list",
    ]: ...

type___AdGroupSimulation = AdGroupSimulation
