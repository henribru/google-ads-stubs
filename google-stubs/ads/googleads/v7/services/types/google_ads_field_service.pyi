from typing import Any

import proto

from google.ads.googleads.v7.resources.types import google_ads_field as google_ads_field

__protobuf__: Any

class GetGoogleAdsFieldRequest(proto.Message):
    resource_name: Any

class SearchGoogleAdsFieldsRequest(proto.Message):
    query: Any
    page_token: Any
    page_size: Any

class SearchGoogleAdsFieldsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Any
    next_page_token: Any
    total_results_count: Any
