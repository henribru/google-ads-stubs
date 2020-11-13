# Type stubs for the Google Ads API Client Library for Python

[![PyPI version](https://badge.fury.io/py/google-ads-stubs.svg)](https://badge.fury.io/py/google-ads-stubs)

This package provides type stubs for the [Google Ads API Client Library for Python](https://github.com/googleads/google-ads-python). 
It's currently compatible with v.8.0.0 of this library. It allows you to type check usage of the library with e.g. [mypy](http://mypy-lang.org/) and will also improve autocomplete in many editors.

**This is in no way affiliated with Google.**

The stubs for protobuf messages were created by [mypy-protobuf](https://github.com/dropbox/mypy-protobuf).
The rest were created either by hand or by self-made scripts, with the output of MyPy's `stubgen` as
a starting point.

If you find incorrect annotations, please create an issue. Contributions for fixes are also welcome.

## Installation

```
$ pip install google-ads-stubs
```

## Caveats

There are some caveats. The primary one is that type inference does _not_ work for the `get_type` and `get_service`
methods of `Client`. The workaround is to explicitly state the type. For `get_type` you can also instantiate
the object directly.

```python
# Replace this:
campaign_operation = client.get_type('CampaignOperation')
# With this:
from google.ads.google_ads.v3.types import CampaignOperation
campaign_operation: CampaignOperation = client.get_type('CampaignOperation')
# Or this:
from google.ads.google_ads.v3.types import CampaignOperation
campaign_operation = CampaignOperation()

# Replace this:
google_ads_service = client.get_service('GoogleAdsService')
# With this:
from google.ads.google_ads.v3.services import GoogleAdsServiceClient
google_ads_service: GoogleAdsServiceClient = client.get_service('GoogleAdsService')
```

While it is technically possible to type these methods using a combination of overloading and literal types,
this is not included in these stubs. The reason is that it requires about 10,000 overloads, which, while simple
to generate, slows type checking to a crawl.

This package does not provide complete type annotations, although it should cover what's used by most developers.
The bare output from `stubgen` is used by the service stubs and transport classes.
The service stubs are unlikely to be typed as long as there is no `mypy-protobuf` equivalent
for GRPC stubs. The transport classes may be typed in the future if there is a need for it.

Some service methods allow you to pass in either a protobuf message or a dictionary for certain arguments.
There is no check that the dictionary conforms to the message structure, as this would require a `TypedDict` subclass
for each message.
