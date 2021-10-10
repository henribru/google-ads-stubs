from typing import Any

import proto

__protobuf__: Any

class BudgetCampaignAssociationStatusEnum(proto.Message):
    class BudgetCampaignAssociationStatus(proto.Enum):
        UNSPECIFIED: int
        UNKNOWN: int
        ENABLED: int
        REMOVED: int
