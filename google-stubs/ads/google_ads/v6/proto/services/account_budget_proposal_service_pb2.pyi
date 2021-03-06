# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Optional as typing___Optional, Text as typing___Text

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.field_mask_pb2 import (
    FieldMask as google___protobuf___field_mask_pb2___FieldMask,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.resources.account_budget_proposal_pb2 import (
    AccountBudgetProposal as google___ads___googleads___v6___resources___account_budget_proposal_pb2___AccountBudgetProposal,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class GetAccountBudgetProposalRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___GetAccountBudgetProposalRequest = GetAccountBudgetProposalRequest

class MutateAccountBudgetProposalRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    validate_only: builtin___bool = ...
    @property
    def operation(self) -> type___AccountBudgetProposalOperation: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operation: typing___Optional[type___AccountBudgetProposalOperation] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["operation", b"operation"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "operation",
            b"operation",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___MutateAccountBudgetProposalRequest = MutateAccountBudgetProposalRequest

class AccountBudgetProposalOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    remove: typing___Text = ...
    @property
    def update_mask(self) -> google___protobuf___field_mask_pb2___FieldMask: ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v6___resources___account_budget_proposal_pb2___AccountBudgetProposal: ...
    def __init__(
        self,
        *,
        update_mask: typing___Optional[
            google___protobuf___field_mask_pb2___FieldMask
        ] = None,
        create: typing___Optional[
            google___ads___googleads___v6___resources___account_budget_proposal_pb2___AccountBudgetProposal
        ] = None,
        remove: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create",
            b"create",
            "operation",
            b"operation",
            "remove",
            b"remove",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create", "remove"]: ...

type___AccountBudgetProposalOperation = AccountBudgetProposalOperation

class MutateAccountBudgetProposalResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def result(self) -> type___MutateAccountBudgetProposalResult: ...
    def __init__(
        self,
        *,
        result: typing___Optional[type___MutateAccountBudgetProposalResult] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> builtin___bool: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["result", b"result"]
    ) -> None: ...

type___MutateAccountBudgetProposalResponse = MutateAccountBudgetProposalResponse

class MutateAccountBudgetProposalResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    def __init__(
        self, *, resource_name: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions___Literal["resource_name", b"resource_name"]
    ) -> None: ...

type___MutateAccountBudgetProposalResult = MutateAccountBudgetProposalResult
