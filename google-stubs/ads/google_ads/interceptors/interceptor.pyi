from google.ads.google_ads.errors import GoogleAdsException as GoogleAdsException
from google.protobuf.message import DecodeError as DecodeError
from typing import Any, Optional

class Interceptor:
    @classmethod
    def get_request_id_from_metadata(cls, trailing_metadata: Any): ...
    @classmethod
    def parse_metadata_to_json(cls, metadata: Any): ...
    @classmethod
    def format_json_object(cls, obj: Any): ...
    @classmethod
    def get_trailing_metadata_from_interceptor_exception(cls, exception: Any): ...
    @classmethod
    def get_client_call_details_instance(
        cls, method: Any, timeout: Any, metadata: Any, credentials: Optional[Any] = ...
    ): ...
    def __init__(self, api_version: Any) -> None: ...
