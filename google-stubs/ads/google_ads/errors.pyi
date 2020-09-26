from typing import Union
import grpc  # type: ignore
from google.ads.google_ads.v2.proto.errors.errors_pb2 import (
    GoogleAdsFailure as GoogleAdsFailureV2,
)

class GoogleAdsException(Exception):
    error: grpc.RpcError = ...
    call: grpc.Call = ...
    failure: GoogleAdsFailureV2 = ...
    request_id: str = ...
    def __init__(
        self,
        error: grpc.RpcError,
        call: grpc.Call,
        failure: GoogleAdsFailureV2,
        request_id: str,
    ) -> None: ...
