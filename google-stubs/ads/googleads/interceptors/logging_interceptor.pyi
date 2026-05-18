import logging

import grpc
from _typeshed import Incomplete
from google.protobuf.message import Message as ProtobufMessageType

from google.ads.googleads.interceptors import ContinuationType, Interceptor

__all__ = [
    "MetadataInterceptor",
    "AsyncUnaryUnaryLoggingInterceptor",
    "AsyncUnaryStreamLoggingInterceptor",
]

class LoggingInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    endpoint: Incomplete
    logger: Incomplete
    def __init__(
        self, logger: logging.Logger, api_version: str, endpoint: str | None = None
    ) -> None: ...
    def log_successful_request(
        self,
        method: str,
        customer_id: str,
        metadata_json: str,
        request_id: str,
        request: ProtobufMessageType,
        trailing_metadata_json: str,
        response: grpc.Call | grpc.Future,
    ) -> None: ...
    def log_failed_request(
        self,
        method: str,
        customer_id: str,
        metadata_json: str,
        request_id: str,
        request: ProtobufMessageType,
        trailing_metadata_json: str,
        response: grpc.Call | grpc.Future,
    ) -> None: ...
    def log_request(
        self,
        client_call_details: grpc.ClientCallDetails,
        request: ProtobufMessageType,
        response: grpc.Call | grpc.Future,
    ) -> None: ...
    def intercept_unary_unary(  # type: ignore[override]
        self,
        continuation: ContinuationType,
        client_call_details: grpc.ClientCallDetails,
        request: ProtobufMessageType,
    ) -> grpc.Call | grpc.Future: ...
    def intercept_unary_stream(  # type: ignore[override]
        self,
        continuation: ContinuationType,
        client_call_details: grpc.ClientCallDetails,
        request: ProtobufMessageType,
    ) -> grpc.Call | grpc.Future: ...
    def retrieve_and_mask_result(
        self, response: grpc.Call | grpc.Future
    ) -> ProtobufMessageType: ...

class _AsyncLoggingInterceptor(LoggingInterceptor):
    def log_failed_request_async(
        self,
        method: str,
        customer_id: str,
        metadata_json: str,
        request_id: str,
        request: ProtobufMessageType,
        trailing_metadata_json: str,
        response: grpc.aio.Call,
        exception: Exception,
    ) -> None: ...
    def log_successful_request_async(
        self,
        method: str,
        customer_id: str,
        metadata_json: str,
        request_id: str,
        request: ProtobufMessageType,
        trailing_metadata_json: str,
        response: grpc.aio.Call,
        result: ProtobufMessageType | None = None,
    ) -> None: ...
    async def intercept_unary_unary(  # type: ignore[override]
        self,
        continuation: ContinuationType,
        client_call_details: grpc.ClientCallDetails,
        request: ProtobufMessageType,
    ) -> grpc.Call | grpc.Future: ...
    async def intercept_unary_stream(  # type: ignore[override]
        self,
        continuation: ContinuationType,
        client_call_details: grpc.ClientCallDetails,
        request: ProtobufMessageType,
    ) -> grpc.Call | grpc.Future: ...

class AsyncUnaryUnaryLoggingInterceptor(  # type: ignore[misc]
    _AsyncLoggingInterceptor, grpc.aio.UnaryUnaryClientInterceptor
): ...
class AsyncUnaryStreamLoggingInterceptor(  # type: ignore[misc]
    _AsyncLoggingInterceptor, grpc.aio.UnaryStreamClientInterceptor
): ...

# Names in __all__ with no definition:
#   MetadataInterceptor
