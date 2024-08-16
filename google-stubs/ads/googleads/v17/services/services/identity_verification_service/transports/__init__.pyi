from .base import (
    IdentityVerificationServiceTransport as IdentityVerificationServiceTransport,
)
from .grpc import (
    IdentityVerificationServiceGrpcTransport as IdentityVerificationServiceGrpcTransport,
)

__all__ = [
    "IdentityVerificationServiceTransport",
    "IdentityVerificationServiceGrpcTransport",
]
