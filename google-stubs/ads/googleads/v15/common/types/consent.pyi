from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.consent_status import ConsentStatusEnum

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
        ad_personalization: ConsentStatusEnum.ConsentStatus = ...
    ) -> None: ...
