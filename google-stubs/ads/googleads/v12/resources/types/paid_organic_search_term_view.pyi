from typing import Any

import proto

class PaidOrganicSearchTermView(proto.Message):
    resource_name: str
    search_term: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        search_term: str = ...
    ) -> None: ...
