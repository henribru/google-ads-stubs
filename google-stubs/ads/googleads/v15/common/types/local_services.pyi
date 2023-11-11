from typing import Any

import proto

class LocalServicesDocumentReadOnly(proto.Message):
    document_url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        document_url: str = ...
    ) -> None: ...
