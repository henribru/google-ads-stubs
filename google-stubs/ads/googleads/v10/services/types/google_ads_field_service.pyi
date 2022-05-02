import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.resources.types import (
    google_ads_field as google_ads_field,
)

__protobuf__: Incomplete

class GetGoogleAdsFieldRequest(proto.Message):
    resource_name: Incomplete

class SearchGoogleAdsFieldsRequest(proto.Message):
    query: Incomplete
    page_token: Incomplete
    page_size: Incomplete

class SearchGoogleAdsFieldsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: Incomplete
    next_page_token: Incomplete
    total_results_count: Incomplete
