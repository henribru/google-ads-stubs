from google.ads.googleads.v20.enums.types.distance_bucket import DistanceBucketEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class DistanceView(proto.Message):
    resource_name: str
    distance_bucket: DistanceBucketEnum.DistanceBucket
    metric_system: bool
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., resource_name: str = ..., distance_bucket: DistanceBucketEnum.DistanceBucket = ..., metric_system: bool = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "distance_bucket", "metric_system"]) -> bool: ...
