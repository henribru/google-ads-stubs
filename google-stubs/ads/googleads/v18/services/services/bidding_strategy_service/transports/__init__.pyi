from .base import BiddingStrategyServiceTransport as BiddingStrategyServiceTransport
from .grpc import (
    BiddingStrategyServiceGrpcTransport as BiddingStrategyServiceGrpcTransport,
)

__all__ = ["BiddingStrategyServiceTransport", "BiddingStrategyServiceGrpcTransport"]
