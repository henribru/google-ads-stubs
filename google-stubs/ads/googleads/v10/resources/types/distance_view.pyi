from typing import Any

import proto

from google.ads.googleads.v10.enums.types.distance_bucket import DistanceBucketEnum

class DistanceView(proto.Message):
    resource_name: str
    distance_bucket: DistanceBucketEnum.DistanceBucket
    metric_system: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        distance_bucket: DistanceBucketEnum.DistanceBucket = ...,
        metric_system: bool = ...
    ) -> None: ...
