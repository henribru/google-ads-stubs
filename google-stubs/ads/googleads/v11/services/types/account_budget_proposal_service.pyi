from typing import Any

import proto
from google.protobuf.field_mask_pb2 import FieldMask

from google.ads.googleads.v11.resources.types.account_budget_proposal import (
    AccountBudgetProposal,
)

class AccountBudgetProposalOperation(proto.Message):
    update_mask: FieldMask
    create: AccountBudgetProposal
    remove: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        update_mask: FieldMask = ...,
        create: AccountBudgetProposal = ...,
        remove: str = ...
    ) -> None: ...

class MutateAccountBudgetProposalRequest(proto.Message):
    customer_id: str
    operation: AccountBudgetProposalOperation
    validate_only: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operation: AccountBudgetProposalOperation = ...,
        validate_only: bool = ...
    ) -> None: ...

class MutateAccountBudgetProposalResponse(proto.Message):
    result: MutateAccountBudgetProposalResult
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        result: MutateAccountBudgetProposalResult = ...
    ) -> None: ...

class MutateAccountBudgetProposalResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...
