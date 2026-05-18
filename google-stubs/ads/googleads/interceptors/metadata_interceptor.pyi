import grpc
from google.protobuf.message import Message as ProtobufMessageType

from google.ads.googleads.interceptors import ContinuationType, Interceptor

__all__ = [
    "MetadataInterceptor",
    "AsyncUnaryUnaryMetadataInterceptor",
    "AsyncUnaryStreamMetadataInterceptor",
]

class MetadataInterceptor(
    Interceptor, grpc.UnaryUnaryClientInterceptor, grpc.UnaryStreamClientInterceptor
):
    developer_token_meta: tuple[str, str]
    login_customer_id_meta: tuple[str, str] | None
    linked_customer_id_meta: tuple[str, str] | None
    ads_assistant: str | None
    use_cloud_org_for_api_access: bool | None
    def __init__(
        self,
        developer_token: str,
        login_customer_id: str | None = None,
        linked_customer_id: str | None = None,
        use_cloud_org_for_api_access: bool | None = None,
        ads_assistant: str | None = None,
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

class _AsyncMetadataInterceptor(MetadataInterceptor):
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

class AsyncUnaryUnaryMetadataInterceptor(  # type: ignore[misc]
    _AsyncMetadataInterceptor, grpc.aio.UnaryUnaryClientInterceptor
): ...
class AsyncUnaryStreamMetadataInterceptor(  # type: ignore[misc]
    _AsyncMetadataInterceptor, grpc.aio.UnaryStreamClientInterceptor
): ...
