from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class LocalServicesInsuranceRejectionReasonEnum(proto.Message):
    class LocalServicesInsuranceRejectionReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME_MISMATCH = 2
        INSURANCE_AMOUNT_INSUFFICIENT = 3
        EXPIRED = 4
        NO_SIGNATURE = 5
        NO_POLICY_NUMBER = 6
        NO_COMMERCIAL_GENERAL_LIABILITY = 7
        EDITABLE_FORMAT = 8
        CATEGORY_MISMATCH = 9
        MISSING_EXPIRATION_DATE = 10
        POOR_QUALITY = 11
        POTENTIALLY_EDITED = 12
        WRONG_DOCUMENT_TYPE = 13
        NON_FINAL = 14
        OTHER = 15

    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
