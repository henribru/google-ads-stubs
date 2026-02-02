from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

_M = TypeVar("_M")

class QualifyingQuestion(proto.Message):
    resource_name: str
    qualifying_question_id: int
    locale: str
    text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        qualifying_question_id: int = ...,
        locale: str = ...,
        text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "qualifying_question_id", "locale", "text"]
    ) -> bool: ...
