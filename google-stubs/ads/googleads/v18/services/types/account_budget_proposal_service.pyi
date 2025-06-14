import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.resources.types import account_budget_proposal
from google.protobuf import field_mask_pb2

__protobuf__: Incomplete

class MutateAccountBudgetProposalRequest(proto.Message):
    customer_id: str
    operation: AccountBudgetProposalOperation
    validate_only: bool

class AccountBudgetProposalOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: account_budget_proposal.AccountBudgetProposal
    remove: str

class MutateAccountBudgetProposalResponse(proto.Message):
    result: MutateAccountBudgetProposalResult

class MutateAccountBudgetProposalResult(proto.Message):
    resource_name: str
