from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v13.resources.types.account_budget_proposal import (
    AccountBudgetProposal,
)

_M = TypeVar("_M")

class AccountBudgetProposalOperation(proto.Message):
    update_mask: FieldMask
    create: AccountBudgetProposal
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: AccountBudgetProposal = ...,
        remove: str = ...
    ) -> None: ...

class MutateAccountBudgetProposalRequest(proto.Message):
    customer_id: str
    operation: AccountBudgetProposalOperation
    validate_only: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: AccountBudgetProposalOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAccountBudgetProposalResponse(proto.Message):
    result: MutateAccountBudgetProposalResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: MutateAccountBudgetProposalResult = ...
    ) -> None: ...

class MutateAccountBudgetProposalResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
