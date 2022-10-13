from typing import Any

import proto
from google.rpc.status_pb2 import Status

from google.ads.googleads.v11.common.types.extensions import (
    CallFeedItem,
    CalloutFeedItem,
    SitelinkFeedItem,
)
from google.ads.googleads.v11.enums.types.keyword_match_type import KeywordMatchTypeEnum
from google.ads.googleads.v11.resources.types.ad import Ad

class ApplyRecommendationOperation(proto.Message):
    class CallExtensionParameters(proto.Message):
        call_extensions: list[CallFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            call_extensions: list[CallFeedItem] = ...
        ) -> None: ...

    class CalloutExtensionParameters(proto.Message):
        callout_extensions: list[CalloutFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            callout_extensions: list[CalloutFeedItem] = ...
        ) -> None: ...

    class CampaignBudgetParameters(proto.Message):
        new_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            new_budget_amount_micros: int = ...
        ) -> None: ...

    class KeywordParameters(proto.Message):
        ad_group: str
        match_type: KeywordMatchTypeEnum.KeywordMatchType
        cpc_bid_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad_group: str = ...,
            match_type: KeywordMatchTypeEnum.KeywordMatchType = ...,
            cpc_bid_micros: int = ...
        ) -> None: ...

    class MoveUnusedBudgetParameters(proto.Message):
        budget_micros_to_move: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            budget_micros_to_move: int = ...
        ) -> None: ...

    class ResponsiveSearchAdAssetParameters(proto.Message):
        updated_ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            updated_ad: Ad = ...
        ) -> None: ...

    class ResponsiveSearchAdImproveAdStrengthParameters(proto.Message):
        updated_ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            updated_ad: Ad = ...
        ) -> None: ...

    class ResponsiveSearchAdParameters(proto.Message):
        ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad: Ad = ...
        ) -> None: ...

    class SitelinkExtensionParameters(proto.Message):
        sitelink_extensions: list[SitelinkFeedItem]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            sitelink_extensions: list[SitelinkFeedItem] = ...
        ) -> None: ...

    class TargetCpaOptInParameters(proto.Message):
        target_cpa_micros: int
        new_campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_cpa_micros: int = ...,
            new_campaign_budget_amount_micros: int = ...
        ) -> None: ...

    class TargetRoasOptInParameters(proto.Message):
        target_roas: float
        new_campaign_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            target_roas: float = ...,
            new_campaign_budget_amount_micros: int = ...
        ) -> None: ...

    class TextAdParameters(proto.Message):
        ad: Ad
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            ad: Ad = ...
        ) -> None: ...

    class UseBroadMatchKeywordParameters(proto.Message):
        new_budget_amount_micros: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            new_budget_amount_micros: int = ...
        ) -> None: ...
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
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        responsive_search_ad_improve_ad_strength: ApplyRecommendationOperation.ResponsiveSearchAdImproveAdStrengthParameters = ...
    ) -> None: ...

class ApplyRecommendationRequest(proto.Message):
    customer_id: str
    operations: list[ApplyRecommendationOperation]
    partial_failure: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[ApplyRecommendationOperation] = ...,
        partial_failure: bool = ...
    ) -> None: ...

class ApplyRecommendationResponse(proto.Message):
    results: list[ApplyRecommendationResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[ApplyRecommendationResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...

class ApplyRecommendationResult(proto.Message):
    resource_name: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...
    ) -> None: ...

class DismissRecommendationRequest(proto.Message):
    class DismissRecommendationOperation(proto.Message):
        resource_name: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            resource_name: str = ...
        ) -> None: ...
    customer_id: str
    operations: list[DismissRecommendationRequest.DismissRecommendationOperation]
    partial_failure: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        customer_id: str = ...,
        operations: list[
            DismissRecommendationRequest.DismissRecommendationOperation
        ] = ...,
        partial_failure: bool = ...
    ) -> None: ...

class DismissRecommendationResponse(proto.Message):
    class DismissRecommendationResult(proto.Message):
        resource_name: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            resource_name: str = ...
        ) -> None: ...
    results: list[DismissRecommendationResponse.DismissRecommendationResult]
    partial_failure_error: Status
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        results: list[DismissRecommendationResponse.DismissRecommendationResult] = ...,
        partial_failure_error: Status = ...
    ) -> None: ...
