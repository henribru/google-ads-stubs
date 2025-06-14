import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class ExperimentMetricEnum(proto.Message):
    class ExperimentMetric(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        CLICKS: int
        IMPRESSIONS: int
        COST: int
        CONVERSIONS_PER_INTERACTION_RATE: int
        COST_PER_CONVERSION: int
        CONVERSIONS_VALUE_PER_COST: int
        AVERAGE_CPC: int
        CTR: int
        INCREMENTAL_CONVERSIONS: int
        COMPLETED_VIDEO_VIEWS: int
        CUSTOM_ALGORITHMS: int
        CONVERSIONS: int
        CONVERSION_VALUE: int
