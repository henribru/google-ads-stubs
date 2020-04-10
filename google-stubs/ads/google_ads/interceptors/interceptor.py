import grpc  # type: ignore
from typing import Tuple, Any, Optional, List, NamedTuple


class _ClientCallDetails(
    NamedTuple(
        "_ClientCallDetails",
        [
            ("method", str),
            ("timeout", float),
            ("metadata", List[Tuple[str, Any]]),
            ("credentials", Optional[grpc.CallCredentials]),
        ],
    ),
    grpc.ClientCallDetails,
):
    pass


class Interceptor:
    @classmethod
    def get_request_id_from_metadata(
        cls, trailing_metadata: Tuple[Tuple[str, Any]]
    ) -> Optional[str]:
        ...

    @classmethod
    def parse_metadata_to_json(cls, metadata: List[Tuple[str, Any]]) -> str:
        ...

    @classmethod
    def format_json_object(cls, obj: Any) -> str:
        ...

    @classmethod
    def get_trailing_metadata_from_interceptor_exception(
        cls, exception
    ) -> Tuple[Tuple[str, Any]]:
        ...

    @classmethod
    def get_client_call_details_instance(
        cls,
        method: str,
        timeout: float,
        metadata: List[Tuple[str, Any]],
        credentials: Optional[grpc.CallCredentials] = ...,
    ) -> None:
        ...

    def __init__(self, api_version: str) -> None:
        ...
