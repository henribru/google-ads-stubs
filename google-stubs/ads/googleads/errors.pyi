import grpc

from google.ads.googleads.v17.errors import GoogleAdsFailure as GoogleAdsFailureV17
from google.ads.googleads.v18.errors import GoogleAdsFailure as GoogleAdsFailureV18
from google.ads.googleads.v19.errors import GoogleAdsFailure as GoogleAdsFailureV19

GoogleAdsFailure = GoogleAdsFailureV17 | GoogleAdsFailureV18 | GoogleAdsFailureV19

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
