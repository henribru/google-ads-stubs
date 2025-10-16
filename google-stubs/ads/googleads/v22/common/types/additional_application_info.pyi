from google.ads.googleads.v22.enums.types.application_instance import ApplicationInstanceEnum
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AdditionalApplicationInfo(proto.Message):
    application_id: str
    application_instance: ApplicationInstanceEnum.ApplicationInstance
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, application_id: str = ..., application_instance: ApplicationInstanceEnum.ApplicationInstance = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["application_id", "application_instance"]) -> bool: ...
