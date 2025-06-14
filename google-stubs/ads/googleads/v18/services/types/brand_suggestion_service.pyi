import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import brand_state
from typing import MutableSequence

__protobuf__: Incomplete

class SuggestBrandsRequest(proto.Message):
    customer_id: str
    brand_prefix: str
    selected_brands: MutableSequence[str]

class SuggestBrandsResponse(proto.Message):
    brands: MutableSequence['BrandSuggestion']

class BrandSuggestion(proto.Message):
    id: str
    name: str
    urls: MutableSequence[str]
    state: brand_state.BrandStateEnum.BrandState
