from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.common.types.tag_snippet import TagSnippet

_M = TypeVar("_M")

class RemarketingAction(proto.Message):
    resource_name: str
    id: int
    name: str
    tag_snippets: MutableSequence[TagSnippet]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        tag_snippets: MutableSequence[TagSnippet] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "id", "name", "tag_snippets"]
    ) -> bool: ...
