import logging
from typing import Callable, Optional, TypeVar

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

class LoggingInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    endpoint: str = ...
    logger: logging.Logger = ...
    def __init__(
        self, logger: logging.Logger, api_version: str, endpoint: Optional[str] = ...
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
