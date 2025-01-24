from .base import LocalServicesLeadServiceTransport as LocalServicesLeadServiceTransport
from .grpc import (
    LocalServicesLeadServiceGrpcTransport as LocalServicesLeadServiceGrpcTransport,
)

__all__ = ["LocalServicesLeadServiceTransport", "LocalServicesLeadServiceGrpcTransport"]
