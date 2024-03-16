from .base import SharedCriterionServiceTransport as SharedCriterionServiceTransport
from .grpc import (
    SharedCriterionServiceGrpcTransport as SharedCriterionServiceGrpcTransport,
)

__all__ = ["SharedCriterionServiceTransport", "SharedCriterionServiceGrpcTransport"]
