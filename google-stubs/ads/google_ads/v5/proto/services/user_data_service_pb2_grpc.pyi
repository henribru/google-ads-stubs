from typing import Any, Optional

class UserDataServiceStub:
    UploadUserData: Any = ...
    def __init__(self, channel: Any) -> None: ...

class UserDataServiceServicer:
    def UploadUserData(self, request: Any, context: Any) -> None: ...

def add_UserDataServiceServicer_to_server(servicer: Any, server: Any) -> None: ...

class UserDataService:
    @staticmethod
    def UploadUserData(
        request: Any,
        target: Any,
        options: Any = ...,
        channel_credentials: Optional[Any] = ...,
        call_credentials: Optional[Any] = ...,
        compression: Optional[Any] = ...,
        wait_for_ready: Optional[Any] = ...,
        timeout: Optional[Any] = ...,
        metadata: Optional[Any] = ...,
    ): ...
