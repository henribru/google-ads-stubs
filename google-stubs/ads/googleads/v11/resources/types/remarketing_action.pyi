from typing import Any

import proto

from google.ads.googleads.v11.common.types.tag_snippet import TagSnippet

class RemarketingAction(proto.Message):
    resource_name: str
    id: int
    name: str
    tag_snippets: list[TagSnippet]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        name: str = ...,
        tag_snippets: list[TagSnippet] = ...
    ) -> None: ...
