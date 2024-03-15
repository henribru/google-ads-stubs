from collections.abc import Callable
from typing import TypeVar

import grpc

from google.ads.googleads import v14, v15, v16

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    v14.SearchGoogleAdsRequest,
    v14.SearchGoogleAdsStreamRequest,
    v15.SearchGoogleAdsRequest,
    v15.SearchGoogleAdsStreamRequest,
    v16.SearchGoogleAdsRequest,
    v16.SearchGoogleAdsStreamRequest,
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
