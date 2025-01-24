from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LocalServicesBusinessRegistrationCheckRejectionReasonEnum(proto.Message):
    class LocalServicesBusinessRegistrationCheckRejectionReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME_MISMATCH = 2
        BUSINESS_DETAILS_MISMATCH = 3
        ID_NOT_FOUND = 4
        POOR_DOCUMENT_IMAGE_QUALITY = 5
        DOCUMENT_EXPIRED = 6
        DOCUMENT_INVALID = 7
        DOCUMENT_TYPE_MISMATCH = 8
        DOCUMENT_UNVERIFIABLE = 9
        OTHER = 10

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
