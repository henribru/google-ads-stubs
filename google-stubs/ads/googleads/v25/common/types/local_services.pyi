from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.gls_phone_number_type import (
    GlsPhoneNumberTypeEnum,
)

_M = TypeVar("_M")

class LocalServicesDocumentReadOnly(proto.Message):
    document_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        document_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["document_url"]
    ) -> bool: ...

class LocalServicesPhoneNumber(proto.Message):
    phone_number: str
    country_code: str
    phone_number_type: GlsPhoneNumberTypeEnum.GlsPhoneNumberType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        phone_number: str = ...,
        country_code: str = ...,
        phone_number_type: GlsPhoneNumberTypeEnum.GlsPhoneNumberType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["phone_number", "country_code", "phone_number_type"]
    ) -> bool: ...
