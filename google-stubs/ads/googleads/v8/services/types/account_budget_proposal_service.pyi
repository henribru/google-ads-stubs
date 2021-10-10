from typing import Any

import proto
from google.protobuf import field_mask_pb2 as field_mask_pb2

from google.ads.googleads.v8.resources.types import (
    account_budget_proposal as account_budget_proposal,
)

__protobuf__: Any

class GetAccountBudgetProposalRequest(proto.Message):
    resource_name: Any

class MutateAccountBudgetProposalRequest(proto.Message):
    customer_id: Any
    operation: Any
    validate_only: Any

class AccountBudgetProposalOperation(proto.Message):
    update_mask: Any
    create: Any
    remove: Any

class MutateAccountBudgetProposalResponse(proto.Message):
    result: Any

class MutateAccountBudgetProposalResult(proto.Message):
    resource_name: Any
