import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import google_ads_field
from typing import MutableSequence

__protobuf__: Incomplete

class GetGoogleAdsFieldRequest(proto.Message):
    resource_name: str

class SearchGoogleAdsFieldsRequest(proto.Message):
    query: str
    page_token: str
    page_size: int

class SearchGoogleAdsFieldsResponse(proto.Message):
    @property
    def raw_page(self): ...
    results: MutableSequence[google_ads_field.GoogleAdsField]
    next_page_token: str
    total_results_count: int
