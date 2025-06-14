import proto
from _typeshed import Incomplete
from typing import MutableSequence

__protobuf__: Incomplete

class UrlCollection(proto.Message):
    url_collection_id: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
