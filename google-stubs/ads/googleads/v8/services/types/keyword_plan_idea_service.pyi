from typing import Any

import proto

from google.ads.googleads.v8.common.types import (
    keyword_plan_common as keyword_plan_common,
)
from google.ads.googleads.v8.enums.types import (
    keyword_plan_keyword_annotation as keyword_plan_keyword_annotation,
)

__protobuf__: Any

class GenerateKeywordIdeasRequest(proto.Message):
    customer_id: Any
    language: Any
    geo_target_constants: Any
    include_adult_keywords: Any
    page_token: Any
    page_size: Any
    keyword_plan_network: Any
    keyword_annotation: Any
    aggregate_metrics: Any
    historical_metrics_options: Any
    keyword_and_url_seed: Any
    keyword_seed: Any
    url_seed: Any
    site_seed: Any

class KeywordAndUrlSeed(proto.Message):
    url: Any
    keywords: Any

class KeywordSeed(proto.Message):
    keywords: Any

class SiteSeed(proto.Message):
    site: Any

class UrlSeed(proto.Message):
    url: Any

class GenerateKeywordIdeaResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Any
    aggregate_metric_results: Any
    next_page_token: Any
    total_size: Any

class GenerateKeywordIdeaResult(proto.Message):
    text: Any
    keyword_idea_metrics: Any
    keyword_annotations: Any
