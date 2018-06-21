# PyLooker

[![Build Status](https://travis-ci.org/bufferapp/pylooker.svg?branch=master)](https://travis-ci.org/bufferapp/pylooker)

A basic Python interface to [Looker API][looker-api].

## Installation

You can use `pip` to install PyLooker.

```bash
pip install pylooker
```

If you prefer, you can clone it and run the setup.py file. Use the following
commands to install PyLooker from Github:

```bash
git clone https://github.com/bufferapp/pylooker
cd pylooker
python setup.py install
```

## Basic Usage

To use PyLooker you'll need to get the `client_id` and `client_secret` pair for
your Looker user. You can request these to your Looker admin as stated in the
[Looker documentation][docs].

```python
from pylooker.client import LookerClient

api_endpoint = 'https://looker.company.com:19999/api/3.0/'
client_id = 'your-client-id'
client_secret = 'your-client-secret'
lc = LookerClient(api_endpoint, client_id, client_secret)

look_data = lc.run_look(1234)
query_data = lc.run_query('5A0lg9e7U7SNN8fquk0JKz')
```

The JSON results can be converted to a Pandas Dataframe:

```python
import pandas as pd
df = pd.DataFrame(query_data)
```

[looker-api]: https://looker.com/docs/reference/api-and-integration
[docs]: https://looker.com/docs/reference/api-and-integration/api-auth
