import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.common.types import (
    keyword_plan_common as keyword_plan_common,
)
from google.ads.googleads.v11.enums.types import (
    keyword_match_type as keyword_match_type,
    keyword_plan_keyword_annotation as keyword_plan_keyword_annotation,
)

__protobuf__: Incomplete

class GenerateKeywordIdeasRequest(proto.Message):
    customer_id: Incomplete
    language: Incomplete
    geo_target_constants: Incomplete
    include_adult_keywords: Incomplete
    page_token: Incomplete
    page_size: Incomplete
    keyword_plan_network: Incomplete
    keyword_annotation: Incomplete
    aggregate_metrics: Incomplete
    historical_metrics_options: Incomplete
    keyword_and_url_seed: Incomplete
    keyword_seed: Incomplete
    url_seed: Incomplete
    site_seed: Incomplete

class KeywordAndUrlSeed(proto.Message):
    url: Incomplete
    keywords: Incomplete

class KeywordSeed(proto.Message):
    keywords: Incomplete

class SiteSeed(proto.Message):
    site: Incomplete

class UrlSeed(proto.Message):
    url: Incomplete

class GenerateKeywordIdeaResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Incomplete
    aggregate_metric_results: Incomplete
    next_page_token: Incomplete
    total_size: Incomplete

class GenerateKeywordIdeaResult(proto.Message):
    text: Incomplete
    keyword_idea_metrics: Incomplete
    keyword_annotations: Incomplete
    close_variants: Incomplete

class GenerateKeywordHistoricalMetricsRequest(proto.Message):
    customer_id: Incomplete
    keywords: Incomplete
    language: Incomplete
    include_adult_keywords: Incomplete
    geo_target_constants: Incomplete
    keyword_plan_network: Incomplete
    aggregate_metrics: Incomplete
    historical_metrics_options: Incomplete

class GenerateKeywordHistoricalMetricsResponse(proto.Message):
    results: Incomplete
    aggregate_metric_results: Incomplete

class GenerateKeywordHistoricalMetricsResult(proto.Message):
    text: Incomplete
    close_variants: Incomplete
    keyword_metrics: Incomplete

class GenerateAdGroupThemesRequest(proto.Message):
    customer_id: Incomplete
    keywords: Incomplete
    ad_groups: Incomplete

class GenerateAdGroupThemesResponse(proto.Message):
    ad_group_keyword_suggestions: Incomplete
    unusable_ad_groups: Incomplete

class AdGroupKeywordSuggestion(proto.Message):
    keyword_text: Incomplete
    suggested_keyword_text: Incomplete
    suggested_match_type: Incomplete
    suggested_ad_group: Incomplete
    suggested_campaign: Incomplete

class UnusableAdGroup(proto.Message):
    ad_group: Incomplete
    campaign: Incomplete
