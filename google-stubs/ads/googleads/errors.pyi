from typing import Union

import grpc

from google.ads.googleads.v7 import GoogleAdsFailure as GoogleAdsFailureV7
from google.ads.googleads.v8 import GoogleAdsFailure as GoogleAdsFailureV8

GoogleAdsFailure = Union[GoogleAdsFailureV7, GoogleAdsFailureV8]

class GoogleAdsException(Exception):
    error: grpc.RpcError = ...
    call: grpc.Call = ...
    failure: GoogleAdsFailure = ...
    request_id: str = ...
    def __init__(
        self,
        error: grpc.RpcError,
        call: grpc.Call,
        failure: GoogleAdsFailure,
        request_id: str,
    ) -> None: ...
