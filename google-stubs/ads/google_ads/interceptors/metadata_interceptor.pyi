from typing import Callable, Optional, Tuple, TypeVar

import grpc  # type: ignore
from grpc import UnaryUnaryClientInterceptor

from .interceptor import Interceptor

_Request = TypeVar("_Request")
_Response = TypeVar("_Response")

class MetadataInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    developer_token_meta: Tuple[str, str] = ...
    login_customer_id_meta: Optional[Tuple[str, str]] = ...
    def __init__(self, developer_token: str, login_customer_id: str) -> None: ...
    def intercept_unary_unary(
        self,
        continuation: Callable[[grpc.ClientCallDetails, _Request], _Response],
        client_call_details: grpc.ClientCallDetails,
        request: _Request,
    ) -> _Response: ...
    def intercept_unary_stream(
        self,
        continuation: Callable[[grpc.ClientCallDetails, _Request], _Response],
        client_call_details: grpc.ClientCallDetails,
        request: _Request,
    ) -> _Response: ...
