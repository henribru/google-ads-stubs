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

from google.ads.google_ads.v4.proto.enums.campaign_experiment_status_pb2 import (
    CampaignExperimentStatusEnum as google___ads___googleads___v4___enums___campaign_experiment_status_pb2___CampaignExperimentStatusEnum,
)
from google.ads.google_ads.v4.proto.enums.campaign_experiment_traffic_split_type_pb2 import (
    CampaignExperimentTrafficSplitTypeEnum as google___ads___googleads___v4___enums___campaign_experiment_traffic_split_type_pb2___CampaignExperimentTrafficSplitTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CampaignExperiment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    traffic_split_type: google___ads___googleads___v4___enums___campaign_experiment_traffic_split_type_pb2___CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitTypeValue = ...
    status: google___ads___googleads___v4___enums___campaign_experiment_status_pb2___CampaignExperimentStatusEnum.CampaignExperimentStatusValue = ...
    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def campaign_draft(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def description(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def traffic_split_percent(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def experiment_campaign(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def long_running_operation(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def start_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def end_date(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        campaign_draft: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        name: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        description: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        traffic_split_percent: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        traffic_split_type: typing___Optional[
            google___ads___googleads___v4___enums___campaign_experiment_traffic_split_type_pb2___CampaignExperimentTrafficSplitTypeEnum.CampaignExperimentTrafficSplitTypeValue
        ] = None,
        experiment_campaign: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        status: typing___Optional[
            google___ads___googleads___v4___enums___campaign_experiment_status_pb2___CampaignExperimentStatusEnum.CampaignExperimentStatusValue
        ] = None,
        long_running_operation: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        start_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        end_date: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_draft",
            b"campaign_draft",
            "description",
            b"description",
            "end_date",
            b"end_date",
            "experiment_campaign",
            b"experiment_campaign",
            "id",
            b"id",
            "long_running_operation",
            b"long_running_operation",
            "name",
            b"name",
            "start_date",
            b"start_date",
            "traffic_split_percent",
            b"traffic_split_percent",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_draft",
            b"campaign_draft",
            "description",
            b"description",
            "end_date",
            b"end_date",
            "experiment_campaign",
            b"experiment_campaign",
            "id",
            b"id",
            "long_running_operation",
            b"long_running_operation",
            "name",
            b"name",
            "resource_name",
            b"resource_name",
            "start_date",
            b"start_date",
            "status",
            b"status",
            "traffic_split_percent",
            b"traffic_split_percent",
            "traffic_split_type",
            b"traffic_split_type",
        ],
    ) -> None: ...

type___CampaignExperiment = CampaignExperiment
