from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.reservation_request_type import (
    ReservationRequestTypeEnum,
)

_M = TypeVar("_M")

class BookCampaignsOperation(proto.Message):
    class Campaign(proto.Message):
        campaign: str
        request_type: ReservationRequestTypeEnum.ReservationRequestType
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            campaign: str = ...,
            request_type: ReservationRequestTypeEnum.ReservationRequestType = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["campaign", "request_type"]
        ) -> bool: ...

    campaigns: MutableSequence[BookCampaignsOperation.Campaign]
    quote_signature: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaigns: MutableSequence[BookCampaignsOperation.Campaign] = ...,
        quote_signature: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["campaigns", "quote_signature"]
    ) -> bool: ...

class BookCampaignsResult(proto.Message):
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: NoReturn
    ) -> bool: ...
