from typing import Union

import grpc

from google.ads.googleads.v10 import GoogleAdsFailure as GoogleAdsFailureV10
from google.ads.googleads.v11 import GoogleAdsFailure as GoogleAdsFailureV11

GoogleAdsFailure = Union[GoogleAdsFailureV10, GoogleAdsFailureV11]

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
