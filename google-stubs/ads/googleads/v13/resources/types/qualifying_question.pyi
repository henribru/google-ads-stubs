from typing import Any

import proto

class QualifyingQuestion(proto.Message):
    resource_name: str
    qualifying_question_id: int
    locale: str
    text: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        qualifying_question_id: int = ...,
        locale: str = ...,
        text: str = ...
    ) -> None: ...
