from .base import LabelServiceTransport as LabelServiceTransport
from .grpc import LabelServiceGrpcTransport as LabelServiceGrpcTransport

__all__ = ["LabelServiceTransport", "LabelServiceGrpcTransport"]
