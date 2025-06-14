import proto
from _typeshed import Incomplete

__protobuf__: Incomplete

class BrandGuidelinesMigrationErrorEnum(proto.Message):
    class BrandGuidelinesMigrationError(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        BRAND_GUIDELINES_ALREADY_ENABLED: int
        CANNOT_ENABLE_BRAND_GUIDELINES_FOR_REMOVED_CAMPAIGN: int
        BRAND_GUIDELINES_LOGO_LIMIT_EXCEEDED: int
        CANNOT_AUTO_POPULATE_BRAND_ASSETS_WHEN_BRAND_ASSETS_PROVIDED: int
        AUTO_POPULATE_BRAND_ASSETS_REQUIRED_WHEN_BRAND_ASSETS_OMITTED: int
        TOO_MANY_ENABLE_OPERATIONS: int
