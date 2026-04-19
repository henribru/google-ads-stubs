from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class CampaignReservationQuote(proto.Message):
    campaign: str
    max_budget_micros: int
    possible_hold_duration_seconds: int
    suggested_cpm_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign: str = ...,
        max_budget_micros: int = ...,
        possible_hold_duration_seconds: int = ...,
        suggested_cpm_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "campaign",
            "max_budget_micros",
            "possible_hold_duration_seconds",
            "suggested_cpm_micros",
        ],
    ) -> bool: ...
