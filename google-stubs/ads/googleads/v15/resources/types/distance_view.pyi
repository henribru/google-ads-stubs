from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.distance_bucket import DistanceBucketEnum

_M = TypeVar("_M")

class DistanceView(proto.Message):
    resource_name: str
    distance_bucket: DistanceBucketEnum.DistanceBucket
    metric_system: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        distance_bucket: DistanceBucketEnum.DistanceBucket = ...,
        metric_system: bool = ...
    ) -> None: ...
