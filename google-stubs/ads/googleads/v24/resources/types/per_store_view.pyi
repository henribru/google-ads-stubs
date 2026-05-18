from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class PerStoreView(proto.Message):
    resource_name: str
    place_id: str
    address1: str
    address2: str
    business_name: str
    city: str
    country_code: str
    phone_number: str
    postal_code: str
    province: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        place_id: str = ...,
        address1: str = ...,
        address2: str = ...,
        business_name: str = ...,
        city: str = ...,
        country_code: str = ...,
        phone_number: str = ...,
        postal_code: str = ...,
        province: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "place_id",
            "address1",
            "address2",
            "business_name",
            "city",
            "country_code",
            "phone_number",
            "postal_code",
            "province",
        ],
    ) -> bool: ...
