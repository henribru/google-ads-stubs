# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v6.proto.enums.budget_delivery_method_pb2 import (
    BudgetDeliveryMethodEnum as google___ads___googleads___v6___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum,
)
from google.ads.google_ads.v6.proto.enums.budget_period_pb2 import (
    BudgetPeriodEnum as google___ads___googleads___v6___enums___budget_period_pb2___BudgetPeriodEnum,
)
from google.ads.google_ads.v6.proto.enums.budget_status_pb2 import (
    BudgetStatusEnum as google___ads___googleads___v6___enums___budget_status_pb2___BudgetStatusEnum,
)
from google.ads.google_ads.v6.proto.enums.budget_type_pb2 import (
    BudgetTypeEnum as google___ads___googleads___v6___enums___budget_type_pb2___BudgetTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CampaignBudget(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name: typing___Text = ...
    id: builtin___int = ...
    name: typing___Text = ...
    amount_micros: builtin___int = ...
    total_amount_micros: builtin___int = ...
    status: google___ads___googleads___v6___enums___budget_status_pb2___BudgetStatusEnum.BudgetStatusValue = ...
    delivery_method: google___ads___googleads___v6___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum.BudgetDeliveryMethodValue = ...
    explicitly_shared: builtin___bool = ...
    reference_count: builtin___int = ...
    has_recommended_budget: builtin___bool = ...
    recommended_budget_amount_micros: builtin___int = ...
    period: google___ads___googleads___v6___enums___budget_period_pb2___BudgetPeriodEnum.BudgetPeriodValue = ...
    recommended_budget_estimated_change_weekly_clicks: builtin___int = ...
    recommended_budget_estimated_change_weekly_cost_micros: builtin___int = ...
    recommended_budget_estimated_change_weekly_interactions: builtin___int = ...
    recommended_budget_estimated_change_weekly_views: builtin___int = ...
    type: google___ads___googleads___v6___enums___budget_type_pb2___BudgetTypeEnum.BudgetTypeValue = ...
    def __init__(
        self,
        *,
        resource_name: typing___Optional[typing___Text] = None,
        id: typing___Optional[builtin___int] = None,
        name: typing___Optional[typing___Text] = None,
        amount_micros: typing___Optional[builtin___int] = None,
        total_amount_micros: typing___Optional[builtin___int] = None,
        status: typing___Optional[
            google___ads___googleads___v6___enums___budget_status_pb2___BudgetStatusEnum.BudgetStatusValue
        ] = None,
        delivery_method: typing___Optional[
            google___ads___googleads___v6___enums___budget_delivery_method_pb2___BudgetDeliveryMethodEnum.BudgetDeliveryMethodValue
        ] = None,
        explicitly_shared: typing___Optional[builtin___bool] = None,
        reference_count: typing___Optional[builtin___int] = None,
        has_recommended_budget: typing___Optional[builtin___bool] = None,
        recommended_budget_amount_micros: typing___Optional[builtin___int] = None,
        period: typing___Optional[
            google___ads___googleads___v6___enums___budget_period_pb2___BudgetPeriodEnum.BudgetPeriodValue
        ] = None,
        recommended_budget_estimated_change_weekly_clicks: typing___Optional[
            builtin___int
        ] = None,
        recommended_budget_estimated_change_weekly_cost_micros: typing___Optional[
            builtin___int
        ] = None,
        recommended_budget_estimated_change_weekly_interactions: typing___Optional[
            builtin___int
        ] = None,
        recommended_budget_estimated_change_weekly_views: typing___Optional[
            builtin___int
        ] = None,
        type: typing___Optional[
            google___ads___googleads___v6___enums___budget_type_pb2___BudgetTypeEnum.BudgetTypeValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_amount_micros",
            b"_amount_micros",
            "_explicitly_shared",
            b"_explicitly_shared",
            "_has_recommended_budget",
            b"_has_recommended_budget",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_recommended_budget_amount_micros",
            b"_recommended_budget_amount_micros",
            "_recommended_budget_estimated_change_weekly_clicks",
            b"_recommended_budget_estimated_change_weekly_clicks",
            "_recommended_budget_estimated_change_weekly_cost_micros",
            b"_recommended_budget_estimated_change_weekly_cost_micros",
            "_recommended_budget_estimated_change_weekly_interactions",
            b"_recommended_budget_estimated_change_weekly_interactions",
            "_recommended_budget_estimated_change_weekly_views",
            b"_recommended_budget_estimated_change_weekly_views",
            "_reference_count",
            b"_reference_count",
            "_total_amount_micros",
            b"_total_amount_micros",
            "amount_micros",
            b"amount_micros",
            "explicitly_shared",
            b"explicitly_shared",
            "has_recommended_budget",
            b"has_recommended_budget",
            "id",
            b"id",
            "name",
            b"name",
            "recommended_budget_amount_micros",
            b"recommended_budget_amount_micros",
            "recommended_budget_estimated_change_weekly_clicks",
            b"recommended_budget_estimated_change_weekly_clicks",
            "recommended_budget_estimated_change_weekly_cost_micros",
            b"recommended_budget_estimated_change_weekly_cost_micros",
            "recommended_budget_estimated_change_weekly_interactions",
            b"recommended_budget_estimated_change_weekly_interactions",
            "recommended_budget_estimated_change_weekly_views",
            b"recommended_budget_estimated_change_weekly_views",
            "reference_count",
            b"reference_count",
            "total_amount_micros",
            b"total_amount_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_amount_micros",
            b"_amount_micros",
            "_explicitly_shared",
            b"_explicitly_shared",
            "_has_recommended_budget",
            b"_has_recommended_budget",
            "_id",
            b"_id",
            "_name",
            b"_name",
            "_recommended_budget_amount_micros",
            b"_recommended_budget_amount_micros",
            "_recommended_budget_estimated_change_weekly_clicks",
            b"_recommended_budget_estimated_change_weekly_clicks",
            "_recommended_budget_estimated_change_weekly_cost_micros",
            b"_recommended_budget_estimated_change_weekly_cost_micros",
            "_recommended_budget_estimated_change_weekly_interactions",
            b"_recommended_budget_estimated_change_weekly_interactions",
            "_recommended_budget_estimated_change_weekly_views",
            b"_recommended_budget_estimated_change_weekly_views",
            "_reference_count",
            b"_reference_count",
            "_total_amount_micros",
            b"_total_amount_micros",
            "amount_micros",
            b"amount_micros",
            "delivery_method",
            b"delivery_method",
            "explicitly_shared",
            b"explicitly_shared",
            "has_recommended_budget",
            b"has_recommended_budget",
            "id",
            b"id",
            "name",
            b"name",
            "period",
            b"period",
            "recommended_budget_amount_micros",
            b"recommended_budget_amount_micros",
            "recommended_budget_estimated_change_weekly_clicks",
            b"recommended_budget_estimated_change_weekly_clicks",
            "recommended_budget_estimated_change_weekly_cost_micros",
            b"recommended_budget_estimated_change_weekly_cost_micros",
            "recommended_budget_estimated_change_weekly_interactions",
            b"recommended_budget_estimated_change_weekly_interactions",
            "recommended_budget_estimated_change_weekly_views",
            b"recommended_budget_estimated_change_weekly_views",
            "reference_count",
            b"reference_count",
            "resource_name",
            b"resource_name",
            "status",
            b"status",
            "total_amount_micros",
            b"total_amount_micros",
            "type",
            b"type",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_amount_micros", b"_amount_micros"],
    ) -> typing_extensions___Literal["amount_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_explicitly_shared", b"_explicitly_shared"
        ],
    ) -> typing_extensions___Literal["explicitly_shared"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_has_recommended_budget", b"_has_recommended_budget"
        ],
    ) -> typing_extensions___Literal["has_recommended_budget"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_id", b"_id"]
    ) -> typing_extensions___Literal["id"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_name", b"_name"]
    ) -> typing_extensions___Literal["name"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_recommended_budget_amount_micros", b"_recommended_budget_amount_micros"
        ],
    ) -> typing_extensions___Literal["recommended_budget_amount_micros"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_recommended_budget_estimated_change_weekly_clicks",
            b"_recommended_budget_estimated_change_weekly_clicks",
        ],
    ) -> typing_extensions___Literal[
        "recommended_budget_estimated_change_weekly_clicks"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_recommended_budget_estimated_change_weekly_cost_micros",
            b"_recommended_budget_estimated_change_weekly_cost_micros",
        ],
    ) -> typing_extensions___Literal[
        "recommended_budget_estimated_change_weekly_cost_micros"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_recommended_budget_estimated_change_weekly_interactions",
            b"_recommended_budget_estimated_change_weekly_interactions",
        ],
    ) -> typing_extensions___Literal[
        "recommended_budget_estimated_change_weekly_interactions"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_recommended_budget_estimated_change_weekly_views",
            b"_recommended_budget_estimated_change_weekly_views",
        ],
    ) -> typing_extensions___Literal[
        "recommended_budget_estimated_change_weekly_views"
    ]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_reference_count", b"_reference_count"
        ],
    ) -> typing_extensions___Literal["reference_count"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_total_amount_micros", b"_total_amount_micros"
        ],
    ) -> typing_extensions___Literal["total_amount_micros"]: ...

type___CampaignBudget = CampaignBudget
