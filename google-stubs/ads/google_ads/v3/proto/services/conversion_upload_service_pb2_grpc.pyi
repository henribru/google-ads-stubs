from typing import Any

class ConversionUploadServiceStub:
    UploadClickConversions: Any = ...
    UploadCallConversions: Any = ...
    def __init__(self, channel: Any) -> None: ...

class ConversionUploadServiceServicer:
    def UploadClickConversions(self, request: Any, context: Any) -> None: ...
    def UploadCallConversions(self, request: Any, context: Any) -> None: ...

def add_ConversionUploadServiceServicer_to_server(
    servicer: Any, server: Any
) -> None: ...
