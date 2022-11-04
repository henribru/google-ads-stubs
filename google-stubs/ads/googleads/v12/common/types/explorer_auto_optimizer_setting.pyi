from typing import Any

import proto

class ExplorerAutoOptimizerSetting(proto.Message):
    opt_in: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        opt_in: bool = ...
    ) -> None: ...
