# Type stubs for the Google Ads API Client Library for Python

[![PyPI version](https://badge.fury.io/py/google-ads-stubs.svg)](https://badge.fury.io/py/google-ads-stubs)

This package provides type stubs for the [Google Ads API Client Library for Python](https://github.com/googleads/google-ads-python). 
It's currently compatible with v20.0.0 of this library. It allows you to type check usage of the library with e.g. [mypy](http://mypy-lang.org/) and will also improve autocomplete in many editors.

**This is in no way affiliated with Google.**

Most stubs were created automatically by [stubgen](https://mypy.readthedocs.io/en/stable/stubgen.html), the rest are handwritten or generated by self-made scripts.

If you find incorrect annotations, please create an issue. Contributions for fixes are also welcome.

## Installation

```
$ pip install google-ads-stubs
```

## Caveats

There are some caveats. The primary one is that type inference does _not_ work for the `get_type`
method of `Client`.The workaround is to explicitly state the type. You can also instantiate the object directly to get inference. 

```python
# Replace this:
campaign_operation = client.get_type('CampaignOperation')
# With this:
from google.ads.googleads.v13 import CampaignOperation
campaign_operation: CampaignOperation = client.get_type('CampaignOperation')
# Or this:
from google.ads.googleads.v13 import CampaignOperation
campaign_operation = CampaignOperation()
```

While it is technically possible to type this method using a combination of overloading and literal types,
this is not included in these stubs. The reason is that it requires about 10,000 overloads, which makes most typecheckers fairly slow.

Certain types are too lenient compared to what's allowed at runtime. `GoogleAdsClient.enums` is typed as `Any` and so is the `mapping` argument to protobuf message constructors. 
On the other hand certain types are more strict than what's allowed at runtime. You can't substitute a protobuf message for an equivalent dict or an enum with it's equivalent name or value. This might improve in the future, but for now:

```python
# Replace this:
AdGroupAd({"status": "ENABLED", ad={"type": 2}})
# With this:
from google.ads.googleads.v13 import AdGroupAdStatusEnum, AdTypeEnum, Ad
AdGroupAd(status=AdGroupAdStatusEnum.AdGroupAdStatus.ENABLED, ad=Ad(type=AdTypeEnum.AdType.TEXT_AD))
```

Note that if you're using Mypy you need to use the `--namespace-packages` option as `google` and `google.ads` are namespace packages.