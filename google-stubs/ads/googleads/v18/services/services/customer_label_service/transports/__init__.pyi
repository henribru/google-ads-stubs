from .base import CustomerLabelServiceTransport as CustomerLabelServiceTransport
from .grpc import CustomerLabelServiceGrpcTransport as CustomerLabelServiceGrpcTransport
from .grpc_asyncio import (
    CustomerLabelServiceGrpcAsyncIOTransport as CustomerLabelServiceGrpcAsyncIOTransport,
)

__all__ = [
    "CustomerLabelServiceTransport",
    "CustomerLabelServiceGrpcTransport",
    "CustomerLabelServiceGrpcAsyncIOTransport",
]
