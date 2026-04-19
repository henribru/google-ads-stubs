from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.common.types.campaign_reservation_quote import (
    CampaignReservationQuote,
)

_M = TypeVar("_M")

class QuoteCampaignsOperation(proto.Message):
    class Campaign(proto.Message):
        campaign: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            campaign: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["campaign"]
        ) -> bool: ...

    campaigns: MutableSequence[QuoteCampaignsOperation.Campaign]
    quote_signature: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaigns: MutableSequence[QuoteCampaignsOperation.Campaign] = ...,
        quote_signature: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["campaigns", "quote_signature"]
    ) -> bool: ...

class QuoteCampaignsResult(proto.Message):
    quotes: MutableSequence[CampaignReservationQuote]
    quote_signature: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        quotes: MutableSequence[CampaignReservationQuote] = ...,
        quote_signature: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["quotes", "quote_signature"]
    ) -> bool: ...
