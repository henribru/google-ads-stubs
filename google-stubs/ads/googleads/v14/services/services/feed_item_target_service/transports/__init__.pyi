from .base import FeedItemTargetServiceTransport as FeedItemTargetServiceTransport
from .grpc import (
    FeedItemTargetServiceGrpcTransport as FeedItemTargetServiceGrpcTransport,
)

__all__ = ["FeedItemTargetServiceTransport", "FeedItemTargetServiceGrpcTransport"]
