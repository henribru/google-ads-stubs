from typing import Any

import proto

from google.ads.googleads.v15.enums.types.consent_status import ConsentStatusEnum

class Consent(proto.Message):
    ad_user_data: ConsentStatusEnum.ConsentStatus
    ad_personalization: ConsentStatusEnum.ConsentStatus
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ad_user_data: ConsentStatusEnum.ConsentStatus = ...,
        ad_personalization: ConsentStatusEnum.ConsentStatus = ...
    ) -> None: ...
