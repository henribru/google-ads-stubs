from typing import Callable, Optional, Tuple, TypeVar

import grpc

from google.ads.googleads import v7, v8

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    v7.SearchGoogleAdsRequest,
    v7.SearchGoogleAdsStreamRequest,
    v8.SearchGoogleAdsRequest,
    v8.SearchGoogleAdsStreamRequest,
)
_Response = TypeVar("_Response")

class MetadataInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    developer_token_meta: Tuple[str, str] = ...
    login_customer_id_meta: Optional[Tuple[str, str]] = ...
    linked_customer_id_meta: Optional[Tuple[str, str]] = ...
    def __init__(
        self,
        developer_token: str,
        login_customer_id: str,
        linked_customer_id: Optional[str] = None,
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
