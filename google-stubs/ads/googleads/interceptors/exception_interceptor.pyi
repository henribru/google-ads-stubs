from collections.abc import Callable
from typing import TypeVar

import grpc

from google.ads.googleads import v13, v14, v15

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    v13.SearchGoogleAdsRequest,
    v13.SearchGoogleAdsStreamRequest,
    v14.SearchGoogleAdsRequest,
    v14.SearchGoogleAdsStreamRequest,
    v15.SearchGoogleAdsRequest,
    v15.SearchGoogleAdsStreamRequest,
)
_Response = TypeVar("_Response")

class ExceptionInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    def __init__(self, api_version: str, use_proto_plus: bool = False) -> None: ...
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
