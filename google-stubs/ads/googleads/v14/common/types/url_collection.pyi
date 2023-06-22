from collections.abc import MutableSequence
from typing import Any

import proto

class UrlCollection(proto.Message):
    url_collection_id: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        url_collection_id: str = ...,
        final_urls: MutableSequence[str] = ...,
        final_mobile_urls: MutableSequence[str] = ...,
        tracking_url_template: str = ...
    ) -> None: ...
