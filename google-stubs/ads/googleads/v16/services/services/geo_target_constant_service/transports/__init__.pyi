from .base import GeoTargetConstantServiceTransport as GeoTargetConstantServiceTransport
from .grpc import (
    GeoTargetConstantServiceGrpcTransport as GeoTargetConstantServiceGrpcTransport,
)

__all__ = ["GeoTargetConstantServiceTransport", "GeoTargetConstantServiceGrpcTransport"]
