from google.ads.googleads.v20.enums.types.consent_status import ConsentStatusEnum
from google.ads.googleads.v20.enums.types.consent_status import ConsentStatusEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class Consent(proto.Message):
    ad_user_data: ConsentStatusEnum.ConsentStatus
    ad_personalization: ConsentStatusEnum.ConsentStatus
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, ad_user_data: ConsentStatusEnum.ConsentStatus = ..., ad_personalization: ConsentStatusEnum.ConsentStatus = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["ad_user_data", "ad_personalization"]) -> bool: ...
