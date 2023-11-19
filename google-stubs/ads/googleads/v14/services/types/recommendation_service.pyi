from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.extensions import (
    CallFeedItem,
    CalloutFeedItem,
    SitelinkFeedItem,
)
from google.ads.googleads.v14.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v14.resources.types.ad import Ad
from google.ads.googleads.v14.resources.types.asset import Asset

_M = TypeVar("_M")

class ApplyRecommendationOperation(proto.Message):
    class AdAssetApplyParameters(proto.Message):
        class ApplyScope(proto.Enum):
            UNSPECIFIED = 0
            UNKNOWN = 1
            CUSTOMER = 2
            CAMPAIGN = 3
        new_assets: MutableSequence[Asset]
        existing_assets: MutableSequence[str]
        scope: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            new_assets: MutableSequence[Asset] = ...,
            existing_assets: MutableSequence[str] = ...,
            scope: ApplyRecommendationOperation.AdAssetApplyParameters.ApplyScope = ...
        ) -> None: ...
        def __contains__(self, key: Literal["new_assets", "existing_assets", "scope"]) -> bool: ...  # type: ignore[override]

    class CallAssetParameters(proto.Message):
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters = ...
        ) -> None: ...
        def __contains__(self, key: Literal["ad_asset_apply_parameters"]) -> bool: ...  # type: ignore[override]

    class CallExtensionParameters(proto.Message):
        call_extensions: MutableSequence[CallFeedItem]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            call_extensions: MutableSequence[CallFeedItem] = ...
        ) -> None: ...
        def __contains__(self, key: Literal["call_extensions"]) -> bool: ...  # type: ignore[override]

    class CalloutAssetParameters(proto.Message):
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters = ...
        ) -> None: ...
        def __contains__(self, key: Literal["ad_asset_apply_parameters"]) -> bool: ...  # type: ignore[override]

    class CalloutExtensionParameters(proto.Message):
        callout_extensions: MutableSequence[CalloutFeedItem]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            callout_extensions: MutableSequence[CalloutFeedItem] = ...
        ) -> None: ...
        def __contains__(self, key: Literal["callout_extensions"]) -> bool: ...  # type: ignore[override]

    class CampaignBudgetParameters(proto.Message):
        new_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            new_budget_amount_micros: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["new_budget_amount_micros"]) -> bool: ...  # type: ignore[override]

    class ForecastingSetTargetRoasParameters(proto.Message):
        target_roas: float
        campaign_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_roas: float = ...,
            campaign_budget_amount_micros: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["target_roas", "campaign_budget_amount_micros"]) -> bool: ...  # type: ignore[override]

    class KeywordParameters(proto.Message):
        ad_group: str
        match_type: KeywordMatchTypeEnum.KeywordMatchType
        cpc_bid_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad_group: str = ...,
            match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
            cpc_bid_micros: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["ad_group", "match_type", "cpc_bid_micros"]) -> bool: ...  # type: ignore[override]

    class LowerTargetRoasParameters(proto.Message):
        target_roas_multiplier: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_roas_multiplier: float = ...
        ) -> None: ...
        def __contains__(self, key: Literal["target_roas_multiplier"]) -> bool: ...  # type: ignore[override]

    class MoveUnusedBudgetParameters(proto.Message):
        budget_micros_to_move: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            budget_micros_to_move: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["budget_micros_to_move"]) -> bool: ...  # type: ignore[override]

    class RaiseTargetCpaBidTooLowParameters(proto.Message):
        target_multiplier: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_multiplier: float = ...
        ) -> None: ...
        def __contains__(self, key: Literal["target_multiplier"]) -> bool: ...  # type: ignore[override]

    class RaiseTargetCpaParameters(proto.Message):
        target_cpa_multiplier: float
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_cpa_multiplier: float = ...
        ) -> None: ...
        def __contains__(self, key: Literal["target_cpa_multiplier"]) -> bool: ...  # type: ignore[override]

    class ResponsiveSearchAdAssetParameters(proto.Message):
        updated_ad: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            updated_ad: Ad = ...
        ) -> None: ...
        def __contains__(self, key: Literal["updated_ad"]) -> bool: ...  # type: ignore[override]

    class ResponsiveSearchAdImproveAdStrengthParameters(proto.Message):
        updated_ad: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            updated_ad: Ad = ...
        ) -> None: ...
        def __contains__(self, key: Literal["updated_ad"]) -> bool: ...  # type: ignore[override]

    class ResponsiveSearchAdParameters(proto.Message):
        ad: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad: Ad = ...
        ) -> None: ...
        def __contains__(self, key: Literal["ad"]) -> bool: ...  # type: ignore[override]

    class SitelinkAssetParameters(proto.Message):
        ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad_asset_apply_parameters: ApplyRecommendationOperation.AdAssetApplyParameters = ...
        ) -> None: ...
        def __contains__(self, key: Literal["ad_asset_apply_parameters"]) -> bool: ...  # type: ignore[override]

    class SitelinkExtensionParameters(proto.Message):
        sitelink_extensions: MutableSequence[SitelinkFeedItem]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            sitelink_extensions: MutableSequence[SitelinkFeedItem] = ...
        ) -> None: ...
        def __contains__(self, key: Literal["sitelink_extensions"]) -> bool: ...  # type: ignore[override]

    class TargetCpaOptInParameters(proto.Message):
        target_cpa_micros: int
        new_campaign_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_cpa_micros: int = ...,
            new_campaign_budget_amount_micros: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["target_cpa_micros", "new_campaign_budget_amount_micros"]) -> bool: ...  # type: ignore[override]

    class TargetRoasOptInParameters(proto.Message):
        target_roas: float
        new_campaign_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            target_roas: float = ...,
            new_campaign_budget_amount_micros: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["target_roas", "new_campaign_budget_amount_micros"]) -> bool: ...  # type: ignore[override]

    class TextAdParameters(proto.Message):
        ad: Ad
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            ad: Ad = ...
        ) -> None: ...
        def __contains__(self, key: Literal["ad"]) -> bool: ...  # type: ignore[override]

    class UseBroadMatchKeywordParameters(proto.Message):
        new_budget_amount_micros: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            new_budget_amount_micros: int = ...
        ) -> None: ...
        def __contains__(self, key: Literal["new_budget_amount_micros"]) -> bool: ...  # type: ignore[override]
    resource_name: str
    campaign_budget: ApplyRecommendationOperation.CampaignBudgetParameters
    text_ad: ApplyRecommendationOperation.TextAdParameters
    keyword: ApplyRecommendationOperation.KeywordParameters
    target_cpa_opt_in: ApplyRecommendationOperation.TargetCpaOptInParameters
    target_roas_opt_in: ApplyRecommendationOperation.TargetRoasOptInParameters
    callout_extension: ApplyRecommendationOperation.CalloutExtensionParameters
    call_extension: ApplyRecommendationOperation.CallExtensionParameters
    sitelink_extension: ApplyRecommendationOperation.SitelinkExtensionParameters
    move_unused_budget: ApplyRecommendationOperation.MoveUnusedBudgetParameters
    responsive_search_ad: ApplyRecommendationOperation.ResponsiveSearchAdParameters
    use_broad_match_keyword: ApplyRecommendationOperation.UseBroadMatchKeywordParameters
    responsive_search_ad_asset: ApplyRecommendationOperation.ResponsiveSearchAdAssetParameters
    responsive_search_ad_improve_ad_strength: ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters
    raise_target_cpa_bid_too_low: ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParameters
    forecasting_set_target_roas: ApplyRecommendationOperation.ForecastingSetTargetRoasParameters
    callout_asset: ApplyRecommendationOperation.CalloutAssetParameters
    call_asset: ApplyRecommendationOperation.CallAssetParameters
    sitelink_asset: ApplyRecommendationOperation.SitelinkAssetParameters
    raise_target_cpa: ApplyRecommendationOperation.RaiseTargetCpaParameters
    lower_target_roas: ApplyRecommendationOperation.LowerTargetRoasParameters
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign_budget: ApplyRecommendationOperation.CampaignBudgetParameters = ...,
        text_ad: ApplyRecommendationOperation.TextAdParameters = ...,
        keyword: ApplyRecommendationOperation.KeywordParameters = ...,
        target_cpa_opt_in: ApplyRecommendationOperation.TargetCpaOptInParameters = ...,
        target_roas_opt_in: ApplyRecommendationOperation.TargetRoasOptInParameters = ...,
        callout_extension: ApplyRecommendationOperation.CalloutExtensionParameters = ...,
        call_extension: ApplyRecommendationOperation.CallExtensionParameters = ...,
        sitelink_extension: ApplyRecommendationOperation.SitelinkExtensionParameters = ...,
        move_unused_budget: ApplyRecommendationOperation.MoveUnusedBudgetParameters = ...,
        responsive_search_ad: ApplyRecommendationOperation.ResponsiveSearchAdParameters = ...,
        use_broad_match_keyword: ApplyRecommendationOperation.UseBroadMatchKeywordParameters = ...,
        responsive_search_ad_asset: ApplyRecommendationOperation.ResponsiveSearchAdAssetParameters = ...,
        responsive_search_ad_improve_ad_strength: ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters = ...,
        raise_target_cpa_bid_too_low: ApplyRecommendationOperation.RaiseTargetCpaBidTooLowParameters = ...,
        forecasting_set_target_roas: ApplyRecommendationOperation.ForecastingSetTargetRoasParameters = ...,
        callout_asset: ApplyRecommendationOperation.CalloutAssetParameters = ...,
        call_asset: ApplyRecommendationOperation.CallAssetParameters = ...,
        sitelink_asset: ApplyRecommendationOperation.SitelinkAssetParameters = ...,
        raise_target_cpa: ApplyRecommendationOperation.RaiseTargetCpaParameters = ...,
        lower_target_roas: ApplyRecommendationOperation.LowerTargetRoasParameters = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "campaign_budget", "text_ad", "keyword", "target_cpa_opt_in", "target_roas_opt_in", "callout_extension", "call_extension", "sitelink_extension", "move_unused_budget", "responsive_search_ad", "use_broad_match_keyword", "responsive_search_ad_asset", "responsive_search_ad_improve_ad_strength", "raise_target_cpa_bid_too_low", "forecasting_set_target_roas", "callout_asset", "call_asset", "sitelink_asset", "raise_target_cpa", "lower_target_roas"]) -> bool: ...  # type: ignore[override]

class ApplyRecommendationRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ApplyRecommendationOperation]
    partial_failure: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ApplyRecommendationOperation] = ...,
        partial_failure: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure"]) -> bool: ...  # type: ignore[override]

class ApplyRecommendationResponse(proto.Message):
    results: MutableSequence[ApplyRecommendationResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[ApplyRecommendationResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results", "partial_failure_error"]) -> bool: ...  # type: ignore[override]

class ApplyRecommendationResult(proto.Message):
    resource_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]

class DismissRecommendationRequest(proto.Message):
    class DismissRecommendationOperation(proto.Message):
        resource_name: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            resource_name: str = ...
        ) -> None: ...
        def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]
    customer_id: str
    operations: MutableSequence[
        DismissRecommendationRequest.DismissRecommendationOperation
    ]
    partial_failure: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[
            DismissRecommendationRequest.DismissRecommendationOperation
        ] = ...,
        partial_failure: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["customer_id", "operations", "partial_failure"]) -> bool: ...  # type: ignore[override]

class DismissRecommendationResponse(proto.Message):
    class DismissRecommendationResult(proto.Message):
        resource_name: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            resource_name: str = ...
        ) -> None: ...
        def __contains__(self, key: Literal["resource_name"]) -> bool: ...  # type: ignore[override]
    results: MutableSequence[DismissRecommendationResponse.DismissRecommendationResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[
            DismissRecommendationResponse.DismissRecommendationResult
        ] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
    def __contains__(self, key: Literal["results", "partial_failure_error"]) -> bool: ...  # type: ignore[override]
