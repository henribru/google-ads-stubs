from dataclasses import dataclass
from typing import AnyStr, Callable, Sequence

import grpc
from google.protobuf.message import Message

MetadataType = Sequence[tuple[str, AnyStr]]
ContinuationType = Callable[[grpc.ClientCallDetails, Message], grpc.Call]

class Interceptor:
    @dataclass
    class _ClientCallDetails(grpc.ClientCallDetails):
        method: str
        timeout: float | None
        metadata: MetadataType | None  # type:ignore[assignment]
        credentials: grpc.CallCredentials | None
        wait_for_ready: bool | None = ...

    @classmethod
    def get_request_id_from_metadata(
        cls, trailing_metadata: MetadataType
    ) -> str | None: ...
    @classmethod
    def parse_metadata_to_json(cls, metadata: MetadataType | None) -> str: ...
    @classmethod
    def format_json_object(cls, obj: dict) -> str: ...
    @classmethod
    def get_trailing_metadata_from_interceptor_exception(
        cls, exception: grpc.RpcError
    ) -> MetadataType: ...
    @classmethod
    def get_client_call_details_instance(
        cls,
        method: str,
        timeout: float,
        metadata: MetadataType,
        credentials: grpc.CallCredentials | None = None,
        wait_for_ready: bool | None = None,
    ) -> grpc.ClientCallDetails: ...
    def __init__(self, api_version: str) -> None: ...
