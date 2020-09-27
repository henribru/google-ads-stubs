from typing import Any, Optional

from google.ads.google_ads.v5.proto.services import (
    offline_user_data_job_service_pb2_grpc as offline_user_data_job_service_pb2_grpc,
)

class OfflineUserDataJobServiceGrpcTransport:
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
    def create_offline_user_data_job(self): ...
    @property
    def get_offline_user_data_job(self): ...
    @property
    def add_offline_user_data_job_operations(self): ...
    @property
    def run_offline_user_data_job(self): ...
