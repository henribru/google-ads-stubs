from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    account_budget_proposal_service_pb2_grpc as account_budget_proposal_service_pb2_grpc,
)

class AccountBudgetProposalServiceGrpcTransport:
    def __init__(
        self,
        channel: Optional[Any] = ...,
        credentials: Optional[Any] = ...,
        address: str = ...,
    ) -> None: ...
    @classmethod
    def create_channel(
        cls, address: str = ..., credentials: Optional[Any] = ..., **kwargs: Any
    ): ...
    @property
    def channel(self): ...
    @property
    def get_account_budget_proposal(self): ...
    @property
    def mutate_account_budget_proposal(self): ...
