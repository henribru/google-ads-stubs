from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.common.types.tag_snippet import TagSnippet

_M = TypeVar("_M")

class RemarketingAction(proto.Message):
    resource_name: str
    id: int
    name: str
    tag_snippets: MutableSequence[TagSnippet]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        tag_snippets: MutableSequence[TagSnippet] = ...
    ) -> None: ...
