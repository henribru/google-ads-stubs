from typing import Callable, TypeVar

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

class ExceptionInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    def __init__(self, api_version: str, use_proto_plus: bool = ...) -> None: ...
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
