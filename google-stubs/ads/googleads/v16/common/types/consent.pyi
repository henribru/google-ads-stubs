from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.consent_status import ConsentStatusEnum

_M = TypeVar("_M")

class Consent(proto.Message):
    ad_user_data: ConsentStatusEnum.ConsentStatus
    ad_personalization: ConsentStatusEnum.ConsentStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ad_user_data: ConsentStatusEnum.ConsentStatus = ...,
        ad_personalization: ConsentStatusEnum.ConsentStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ad_user_data", "ad_personalization"]
    ) -> bool: ...
