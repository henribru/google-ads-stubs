from typing import Any, NamedTuple

import grpc

class _ClientCallDetails(
    NamedTuple(
        "_ClientCallDetails",
        [
            ("method", str),
            ("timeout", float | None),
            ("metadata", tuple[tuple[str, Any], ...] | None),
            ("credentials", grpc.CallCredentials | None),
        ],
    ),
    grpc.ClientCallDetails,
): ...

class Interceptor:
    @classmethod
    def get_request_id_from_metadata(
        cls, trailing_metadata: tuple[tuple[str, Any]]
    ) -> str | None: ...
    @classmethod
    def parse_metadata_to_json(cls, metadata: list[tuple[str, Any]]) -> str: ...
    @classmethod
    def format_json_object(cls, obj: Any) -> str: ...
    @classmethod
    def get_trailing_metadata_from_interceptor_exception(
        cls, exception: Any
    ) -> tuple[tuple[str, Any]]: ...
    @classmethod
    def get_client_call_details_instance(
        cls,
        method: str,
        timeout: float,
        metadata: list[tuple[str, Any]],
        credentials: grpc.CallCredentials | None = None,
    ) -> _ClientCallDetails: ...
    def __init__(self, api_version: str) -> None: ...
