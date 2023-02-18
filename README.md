# Subreg API Python bindings

This is the very early version of Python library to talk to Subreg API at https://api.subreg.cz

# Installation

```console
pip install subregapi
```
# Usage

```python
from subregapi.client import SubregApi
api = SubregApi(api_key=_TOKEN_)

# Get a list of domains
domains = api.get_domains()
print(domains)
```
