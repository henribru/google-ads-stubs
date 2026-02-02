from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.incentive_state import IncentiveStateEnum

_M = TypeVar("_M")

class AppliedIncentive(proto.Message):
    resource_name: str
    coupon_code: str
    incentive_state: IncentiveStateEnum.IncentiveState
    redemption_date_time: str
    fulfillment_expiration_date_time: str
    reward_grant_date_time: str
    reward_expiration_date_time: str
    currency_code: str
    reward_amount_micros: int
    granted_amount_micros: int
    required_min_spend_micros: int
    current_spend_towards_fulfillment_micros: int
    reward_balance_remaining_micros: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        coupon_code: str = ...,
        incentive_state: IncentiveStateEnum.IncentiveState = ...,
        redemption_date_time: str = ...,
        fulfillment_expiration_date_time: str = ...,
        reward_grant_date_time: str = ...,
        reward_expiration_date_time: str = ...,
        currency_code: str = ...,
        reward_amount_micros: int = ...,
        granted_amount_micros: int = ...,
        required_min_spend_micros: int = ...,
        current_spend_towards_fulfillment_micros: int = ...,
        reward_balance_remaining_micros: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "coupon_code",
            "incentive_state",
            "redemption_date_time",
            "fulfillment_expiration_date_time",
            "reward_grant_date_time",
            "reward_expiration_date_time",
            "currency_code",
            "reward_amount_micros",
            "granted_amount_micros",
            "required_min_spend_micros",
            "current_spend_towards_fulfillment_micros",
            "reward_balance_remaining_micros",
        ],
    ) -> bool: ...
