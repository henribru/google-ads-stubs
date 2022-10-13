from typing import Any

import proto

class UrlCollection(proto.Message):
    url_collection_id: str
    final_urls: list[str]
    final_mobile_urls: list[str]
    tracking_url_template: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        url_collection_id: str = ...,
        final_urls: list[str] = ...,
        final_mobile_urls: list[str] = ...,
        tracking_url_template: str = ...
    ) -> None: ...
