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
from google.rpc.status_pb2 import Status as google___rpc___status_pb2___Status
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v3.proto.resources.customer_negative_criterion_pb2 import (
    CustomerNegativeCriterion as google___ads___googleads___v3___resources___customer_negative_criterion_pb2___CustomerNegativeCriterion,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetCustomerNegativeCriterionRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetCustomerNegativeCriterionRequest = GetCustomerNegativeCriterionRequest

class MutateCustomerNegativeCriteriaRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CustomerNegativeCriterionOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[type___CustomerNegativeCriterionOperation]
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

type___MutateCustomerNegativeCriteriaRequest = MutateCustomerNegativeCriteriaRequest

class CustomerNegativeCriterionOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v3___resources___customer_negative_criterion_pb2___CustomerNegativeCriterion: ...
    def __init__(
        self,
        *,
        create: typing___Optional[
            google___ads___googleads___v3___resources___customer_negative_criterion_pb2___CustomerNegativeCriterion
        ] = None,
        remove: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation", "remove", b"remove"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation", "remove", b"remove"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "remove"]: ...

type___CustomerNegativeCriterionOperation = CustomerNegativeCriterionOperation

class MutateCustomerNegativeCriteriaResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MutateCustomerNegativeCriteriaResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
        results: typing___Optional[
            typing___Iterable[type___MutateCustomerNegativeCriteriaResult]
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

type___MutateCustomerNegativeCriteriaResponse = MutateCustomerNegativeCriteriaResponse

class MutateCustomerNegativeCriteriaResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateCustomerNegativeCriteriaResult = MutateCustomerNegativeCriteriaResult
