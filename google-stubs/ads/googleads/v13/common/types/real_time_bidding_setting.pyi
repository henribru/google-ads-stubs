from typing import Any

import proto

class RealTimeBiddingSetting(proto.Message):
    opt_in: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        opt_in: bool = ...
    ) -> None: ...
