from typing import Any, Optional

from google.ads.google_ads.v4.proto.services import (
    batch_job_service_pb2_grpc as batch_job_service_pb2_grpc,
)

class BatchJobServiceGrpcTransport:
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
    def mutate_batch_job(self): ...
    @property
    def get_batch_job(self): ...
    @property
    def list_batch_job_results(self): ...
    @property
    def run_batch_job(self): ...
    @property
    def add_batch_job_operations(self): ...
