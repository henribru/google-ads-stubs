from typing import Union

import grpc

from google.ads.googleads.v12 import GoogleAdsFailure as GoogleAdsFailureV12
from google.ads.googleads.v13 import GoogleAdsFailure as GoogleAdsFailureV13

GoogleAdsFailure = Union[GoogleAdsFailureV12, GoogleAdsFailureV13]

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
