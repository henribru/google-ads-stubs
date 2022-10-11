import proto
from _typeshed import Incomplete
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v11.resources.types import (
    account_budget_proposal as account_budget_proposal,
)

__protobuf__: Incomplete

class MutateAccountBudgetProposalRequest(proto.Message):
    customer_id: Incomplete
    operation: Incomplete
    validate_only: Incomplete

class AccountBudgetProposalOperation(proto.Message):
    update_mask: Incomplete
    create: Incomplete
    remove: Incomplete

class MutateAccountBudgetProposalResponse(proto.Message):
    result: Incomplete

class MutateAccountBudgetProposalResult(proto.Message):
    resource_name: Incomplete
