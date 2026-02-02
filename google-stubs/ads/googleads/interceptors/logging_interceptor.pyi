import logging
from collections.abc import Callable
from typing import TypeVar

import grpc
from google.protobuf.message import Message

import google.ads.googleads.v20.services
import google.ads.googleads.v21.services
import google.ads.googleads.v22.services
import google.ads.googleads.v23.services

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    google.ads.googleads.v20.services.SearchGoogleAdsRequest,
    google.ads.googleads.v20.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v21.services.SearchGoogleAdsRequest,
    google.ads.googleads.v21.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v22.services.SearchGoogleAdsRequest,
    google.ads.googleads.v22.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v23.services.SearchGoogleAdsRequest,
    google.ads.googleads.v23.services.SearchGoogleAdsStreamRequest,
)
_Response = TypeVar("_Response")

class LoggingInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    endpoint: str = ...
    logger: logging.Logger = ...
    def __init__(
        self, logger: logging.Logger, api_version: str, endpoint: str | None = None
    ) -> None: ...
    def log_successful_request(
        self,
        method: str | None,
        customer_id: str | None,
        metadata_json: str,
        request_id: str | None,
        request: _Request,
        trailing_metadata_json: str,
        response: _Response,
    ) -> None: ...
    def log_failed_request(
        self,
        method: str | None,
        customer_id: str | None,
        metadata_json: str,
        request_id: str | None,
        request: _Request,
        trailing_metadata_json: str,
        response: _Response,
    ) -> None: ...
    def log_request(
        self,
        client_call_details: grpc.ClientCallDetails,
        request: _Request,
        response: _Response,
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
    def retrieve_and_mask_result(self, response: _Response) -> Message: ...
