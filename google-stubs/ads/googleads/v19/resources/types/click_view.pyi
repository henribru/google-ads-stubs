import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import click_location, criteria

__protobuf__: Incomplete

class ClickView(proto.Message):
    resource_name: str
    gclid: str
    area_of_interest: click_location.ClickLocation
    location_of_presence: click_location.ClickLocation
    page_number: int
    ad_group_ad: str
    campaign_location_target: str
    user_list: str
    keyword: str
    keyword_info: criteria.KeywordInfo
