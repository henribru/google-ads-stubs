from .base import CustomerServiceTransport as CustomerServiceTransport
from .grpc import CustomerServiceGrpcTransport as CustomerServiceGrpcTransport

__all__ = ["CustomerServiceTransport", "CustomerServiceGrpcTransport"]
