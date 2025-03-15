from collections.abc import Callable
from typing import TypeVar

import grpc

import google.ads.googleads.v17.services
import google.ads.googleads.v18.services
import google.ads.googleads.v19.services

from .interceptor import Interceptor

_Request = TypeVar(
    "_Request",
    google.ads.googleads.v17.services.SearchGoogleAdsRequest,
    google.ads.googleads.v17.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v18.services.SearchGoogleAdsRequest,
    google.ads.googleads.v18.services.SearchGoogleAdsStreamRequest,
    google.ads.googleads.v19.services.SearchGoogleAdsRequest,
    google.ads.googleads.v19.services.SearchGoogleAdsStreamRequest,
)
_Response = TypeVar("_Response")

class MetadataInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    developer_token_meta: tuple[str, str] = ...
    login_customer_id_meta: tuple[str, str] | None = ...
    linked_customer_id_meta: tuple[str, str] | None = ...
    use_cloud_org_for_api_access: bool | None = ...
    def __init__(
        self,
        developer_token: str,
        login_customer_id: str,
        linked_customer_id: str | None = None,
        use_cloud_org_for_api_access: bool | None = None,
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
