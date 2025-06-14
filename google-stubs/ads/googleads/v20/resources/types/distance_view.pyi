import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import distance_bucket as gage_distance_bucket

__protobuf__: Incomplete

class DistanceView(proto.Message):
    resource_name: str
    distance_bucket: gage_distance_bucket.DistanceBucketEnum.DistanceBucket
    metric_system: bool
