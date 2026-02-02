from google.type.money_pb2 import Money
from google.type.money_pb2 import Money
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class ApplyIncentiveRequest(proto.Message):
    selected_incentive_id: int
    customer_id: str
    country_code: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, selected_incentive_id: int = ..., customer_id: str = ..., country_code: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["selected_incentive_id", "customer_id", "country_code"]) -> bool: ...
class ApplyIncentiveResponse(proto.Message):
    coupon_code: str
    creation_time: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, coupon_code: str = ..., creation_time: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["coupon_code", "creation_time"]) -> bool: ...
class CyoIncentives(proto.Message):
    low_offer: Incentive
    medium_offer: Incentive
    high_offer: Incentive
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, low_offer: Incentive = ..., medium_offer: Incentive = ..., high_offer: Incentive = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["low_offer", "medium_offer", "high_offer"]) -> bool: ...
class FetchIncentiveRequest(proto.Message):
    class IncentiveType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        ACQUISITION = 2
    language_code: str
    country_code: str
    email: str
    type_: FetchIncentiveRequest.IncentiveType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, language_code: str = ..., country_code: str = ..., email: str = ..., type_: FetchIncentiveRequest.IncentiveType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["language_code", "country_code", "email", "type_"]) -> bool: ...
class FetchIncentiveResponse(proto.Message):
    incentive_offer: IncentiveOffer
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, incentive_offer: IncentiveOffer = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["incentive_offer"]) -> bool: ...
class Incentive(proto.Message):
    class Requirement(proto.Message):
        class Spend(proto.Message):
            award_amount: Money
            required_amount: Money
            def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, award_amount: Money = ..., required_amount: Money = ...) -> None: ...
            def __contains__(  # type: ignore[override]
            self, key: Literal["award_amount", "required_amount"]) -> bool: ...
        spend: Incentive.Requirement.Spend
        def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, spend: Incentive.Requirement.Spend = ...) -> None: ...
        def __contains__(  # type: ignore[override]
        self, key: Literal["spend"]) -> bool: ...
    incentive_id: int
    requirement: Incentive.Requirement
    incentive_terms_and_conditions_url: str
    type_: FetchIncentiveRequest.IncentiveType
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, incentive_id: int = ..., requirement: Incentive.Requirement = ..., incentive_terms_and_conditions_url: str = ..., type_: FetchIncentiveRequest.IncentiveType = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["incentive_id", "requirement", "incentive_terms_and_conditions_url", "type_"]) -> bool: ...
class IncentiveOffer(proto.Message):
    class OfferType(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        NO_INCENTIVE = 2
        CYO_INCENTIVE = 3
    type_: IncentiveOffer.OfferType
    consolidated_terms_and_conditions_url: str
    cyo_incentives: CyoIncentives
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, type_: IncentiveOffer.OfferType = ..., consolidated_terms_and_conditions_url: str = ..., cyo_incentives: CyoIncentives = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["type_", "consolidated_terms_and_conditions_url", "cyo_incentives"]) -> bool: ...
