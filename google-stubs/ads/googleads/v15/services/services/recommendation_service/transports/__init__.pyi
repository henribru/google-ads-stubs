from .base import RecommendationServiceTransport as RecommendationServiceTransport
from .grpc import (
    RecommendationServiceGrpcTransport as RecommendationServiceGrpcTransport,
)

__all__ = ["RecommendationServiceTransport", "RecommendationServiceGrpcTransport"]
