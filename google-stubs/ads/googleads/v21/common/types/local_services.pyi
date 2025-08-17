import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class LocalServicesDocumentReadOnly(proto.Message):
    document_url: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, document_url: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["document_url"]) -> bool: ...
