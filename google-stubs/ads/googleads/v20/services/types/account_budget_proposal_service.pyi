from google.ads.googleads.v20.resources.types.account_budget_proposal import AccountBudgetProposal
from google.protobuf.field_mask_pb2 import FieldMask
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AccountBudgetProposalOperation(proto.Message):
    update_mask: FieldMask
    create: AccountBudgetProposal
    remove: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, update_mask: FieldMask = ..., create: AccountBudgetProposal = ..., remove: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["update_mask", "create", "remove"]) -> bool: ...
class MutateAccountBudgetProposalRequest(proto.Message):
    customer_id: str
    operation: AccountBudgetProposalOperation
    validate_only: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., operation: AccountBudgetProposalOperation = ..., validate_only: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "operation", "validate_only"]) -> bool: ...
class MutateAccountBudgetProposalResponse(proto.Message):
    result: MutateAccountBudgetProposalResult
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, result: MutateAccountBudgetProposalResult = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["result"]) -> bool: ...
class MutateAccountBudgetProposalResult(proto.Message):
    resource_name: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name"]) -> bool: ...
