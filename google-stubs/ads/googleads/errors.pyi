import grpc

from google.ads.googleads.v18.errors import GoogleAdsFailure as GoogleAdsFailureV18
from google.ads.googleads.v19.errors import GoogleAdsFailure as GoogleAdsFailureV19
from google.ads.googleads.v20.errors import GoogleAdsFailure as GoogleAdsFailureV20

GoogleAdsFailure = GoogleAdsFailureV18 | GoogleAdsFailureV19 | GoogleAdsFailureV20

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
