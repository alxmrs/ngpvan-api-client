# ngpvan-api-client
A client library for accessing VAN CRM

## Installation

```commandline
pip install git+https://github.com/alxmrs/ngpvan-api-client.git
```

## Usage
First, create a client:

```python
from ngpvan_api_client import Client

client = Client(base_url="https://api.example.com")
```

If the endpoints you're going to hit require authentication, use `AuthenticatedClient` instead:

```python
from ngpvan_api_client import AuthenticatedClient

client = AuthenticatedClient(base_url="https://api.example.com", token="SuperSecretToken")
```

Now call your endpoint and use your models:

```python
from ngpvan_api_client.models import MyDataModel
from ngpvan_api_client.api.my_tag import get_my_data_model
from ngpvan_api_client.types import Response

my_data: MyDataModel = get_my_data_model.sync(client=client)
# or if you need more info (e.g. status_code)
response: Response[MyDataModel] = get_my_data_model.sync_detailed(client=client)
```

Or do the same thing with an async version:

```python
from ngpvan_api_client.models import MyDataModel
from ngpvan_api_client.api.my_tag import get_my_data_model
from ngpvan_api_client.types import Response

my_data: MyDataModel = await get_my_data_model.asyncio(client=client)
response: Response[MyDataModel] = await get_my_data_model.asyncio_detailed(client=client)
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `ngpvan_api_client.api.default`

## Script to generate code:

```commandline
#!/usr/bin/env bash

DIR=${1:-.}

mkdir -p $DIR

(
  cd $DIR
  curl -s https://dash.readme.com/api/v1/api-registry/5r6sg7sl74xoc30 \
    | jq '. + {"openapi": "3.0.3"}' > api.json
  openapi-python-client generate --path api.json --meta setup --config $OLDPWD/config.yml
  rm api.json
)

```

`config.yml`:
```yaml
project_name_override: ngpvan-api-client
```