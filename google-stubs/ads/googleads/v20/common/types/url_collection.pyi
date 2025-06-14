from collections.abc import MutableSequence
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class UrlCollection(proto.Message):
    url_collection_id: str
    final_urls: MutableSequence[str]
    final_mobile_urls: MutableSequence[str]
    tracking_url_template: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., url_collection_id: str = ..., final_urls: MutableSequence[str] = ..., final_mobile_urls: MutableSequence[str] = ..., tracking_url_template: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["url_collection_id", "final_urls", "final_mobile_urls", "tracking_url_template"]) -> bool: ...
