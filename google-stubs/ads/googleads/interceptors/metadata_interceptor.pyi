from typing import Callable, Tuple, TypeVar

import grpc

from google.ads.googleads import v10, v11

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    v10.SearchGoogleAdsRequest,
    v10.SearchGoogleAdsStreamRequest,
    v11.SearchGoogleAdsRequest,
    v11.SearchGoogleAdsStreamRequest,
)
_Response = TypeVar("_Response")

class MetadataInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    developer_token_meta: Tuple[str, str] = ...
    login_customer_id_meta: Tuple[str, str] | None = ...
    linked_customer_id_meta: Tuple[str, str] | None = ...
    def __init__(
        self,
        developer_token: str,
        login_customer_id: str,
        linked_customer_id: str | None = None,
    ) -> None: ...
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
