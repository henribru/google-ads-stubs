from collections.abc import Callable
from typing import TypeVar

import grpc

import google.ads.googleads.v19.services
import google.ads.googleads.v20.services
import google.ads.googleads.v21.services

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    google.ads.googleads.v19.services.SearchGoogleAdsRequest,
    google.ads.googleads.v19.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v20.services.SearchGoogleAdsRequest,
    google.ads.googleads.v20.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v21.services.SearchGoogleAdsRequest,
    google.ads.googleads.v21.services.SearchGoogleAdsStreamRequest,
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
