from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CampaignDraftErrorEnum(proto.Message):
    class CampaignDraftError(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        DUPLICATE_DRAFT_NAME = 2
        INVALID_STATUS_TRANSITION_FROM_REMOVED = 3
        INVALID_STATUS_TRANSITION_FROM_PROMOTED = 4
        INVALID_STATUS_TRANSITION_FROM_PROMOTE_FAILED = 5
        CUSTOMER_CANNOT_CREATE_DRAFT = 6
        CAMPAIGN_CANNOT_CREATE_DRAFT = 7
        INVALID_DRAFT_CHANGE = 8
        INVALID_STATUS_TRANSITION = 9
        MAX_NUMBER_OF_DRAFTS_PER_CAMPAIGN_REACHED = 10
        LIST_ERRORS_FOR_PROMOTED_DRAFT_ONLY = 11

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
