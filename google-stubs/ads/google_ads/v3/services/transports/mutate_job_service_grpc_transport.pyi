from typing import Any, Optional

from google.ads.google_ads.v3.proto.services import (
    mutate_job_service_pb2_grpc as mutate_job_service_pb2_grpc,
)

class MutateJobServiceGrpcTransport:
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
    def create_mutate_job(self): ...
    @property
    def get_mutate_job(self): ...
    @property
    def list_mutate_job_results(self): ...
    @property
    def run_mutate_job(self): ...
    @property
    def add_mutate_job_operations(self): ...
