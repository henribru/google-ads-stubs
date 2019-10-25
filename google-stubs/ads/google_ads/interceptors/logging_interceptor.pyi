import logging

import grpc  # type: ignore

from .interceptor_mixin import InterceptorMixin
from grpc import UnaryUnaryClientInterceptor
from typing import Optional, Callable, TypeVar

_Request = TypeVar("_Request")
_Response = TypeVar("_Response")


class LoggingInterceptor(InterceptorMixin, UnaryUnaryClientInterceptor):
    endpoint: str = ...
    logger: logging.Logger = ...
    def __init__(self, logger: logging.Logger, endpoint: Optional[str] = ...) -> None: ...
    def intercept_unary_unary(self, continuation: Callable[[grpc.ClientCallDetails, _Request], _Response], client_call_details: grpc.ClientCallDetails, request: _Request) -> _Response: ...
