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
from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.rpc.status_pb2 import Status as google___rpc___status_pb2___Status
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v4.proto.resources.campaign_experiment_pb2 import (
    CampaignExperiment as google___ads___googleads___v4___resources___campaign_experiment_pb2___CampaignExperiment,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetCampaignExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetCampaignExperimentRequest = GetCampaignExperimentRequest

class MutateCampaignExperimentsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CampaignExperimentOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[type___CampaignExperimentOperation]
        ] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___MutateCampaignExperimentsRequest = MutateCampaignExperimentsRequest

class CampaignExperimentOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def update(
        self,
    ) -> google___ads___googleads___v4___resources___campaign_experiment_pb2___CampaignExperiment: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        update: typing___Optional[
            google___ads___googleads___v4___resources___campaign_experiment_pb2___CampaignExperiment
        ] = None,
        remove: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["update", "remove"]: ...

type___CampaignExperimentOperation = CampaignExperimentOperation

class MutateCampaignExperimentsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MutateCampaignExperimentResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
        results: typing___Optional[
            typing___Iterable[type___MutateCampaignExperimentResult]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error", "results", b"results"
        ],
    ) -> None: ...

type___MutateCampaignExperimentsResponse = MutateCampaignExperimentsResponse

class MutateCampaignExperimentResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateCampaignExperimentResult = MutateCampaignExperimentResult

class CreateCampaignExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    validate_only: builtin___bool = ...
    @property
    def campaign_experiment(
        self,
    ) -> google___ads___googleads___v4___resources___campaign_experiment_pb2___CampaignExperiment: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        campaign_experiment: typing___Optional[
            google___ads___googleads___v4___resources___campaign_experiment_pb2___CampaignExperiment
        ] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_experiment", b"campaign_experiment"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_experiment",
            b"campaign_experiment",
            "customer_id",
            b"customer_id",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___CreateCampaignExperimentRequest = CreateCampaignExperimentRequest

class CreateCampaignExperimentMetadata(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    campaign_experiment: typing___Text = ...
    def __init__(
        self, *, campaign_experiment: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_experiment", b"campaign_experiment"
        ],
    ) -> None: ...

type___CreateCampaignExperimentMetadata = CreateCampaignExperimentMetadata

class GraduateCampaignExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    campaign_experiment: typing___Text = ...
    campaign_budget: typing___Text = ...
    def __init__(
        self,
        *,
        campaign_experiment: typing___Optional[typing___Text] = None,
        campaign_budget: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_budget",
            b"campaign_budget",
            "campaign_experiment",
            b"campaign_experiment",
        ],
    ) -> None: ...

type___GraduateCampaignExperimentRequest = GraduateCampaignExperimentRequest

class GraduateCampaignExperimentResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    graduated_campaign: typing___Text = ...
    def __init__(
        self, *, graduated_campaign: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "graduated_campaign", b"graduated_campaign"
        ],
    ) -> None: ...

type___GraduateCampaignExperimentResponse = GraduateCampaignExperimentResponse

class PromoteCampaignExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    campaign_experiment: typing___Text = ...
    def __init__(
        self, *, campaign_experiment: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_experiment", b"campaign_experiment"
        ],
    ) -> None: ...

type___PromoteCampaignExperimentRequest = PromoteCampaignExperimentRequest

class EndCampaignExperimentRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    campaign_experiment: typing___Text = ...
    def __init__(
        self, *, campaign_experiment: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "campaign_experiment", b"campaign_experiment"
        ],
    ) -> None: ...

type___EndCampaignExperimentRequest = EndCampaignExperimentRequest

class ListCampaignExperimentAsyncErrorsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    page_token: typing___Text = ...
    page_size: builtin___int = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        page_token: typing___Optional[typing___Text] = None,
        page_size: typing___Optional[builtin___int] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "page_size",
            b"page_size",
            "page_token",
            b"page_token",
            "resource_name",
            b"resource_name",
        ],
    ) -> None: ...

type___ListCampaignExperimentAsyncErrorsRequest = (
    ListCampaignExperimentAsyncErrorsRequest
)

class ListCampaignExperimentAsyncErrorsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    next_page_token: typing___Text = ...
    @property
    def errors(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___rpc___status_pb2___Status
    ]: ...
    def __init__(
        self,
        *,
        errors: typing___Optional[
            typing___Iterable[google___rpc___status_pb2___Status]
        ] = None,
        next_page_token: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "errors", b"errors", "next_page_token", b"next_page_token"
        ],
    ) -> None: ...

type___ListCampaignExperimentAsyncErrorsResponse = (
    ListCampaignExperimentAsyncErrorsResponse
)
