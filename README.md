# [CoinCap API](https://coincap.io/) wrapper

[![py-coincap-client-pypi](https://img.shields.io/pypi/v/py-coincap-client.svg)](https://pypi.python.org/pypi/py-coincap-client)

CoinCap REST API Doc: https://docs.coincap.io/

## Install

```bash
pip install py-coincap-client
```

## Usage

```python
from coincap import CoinCap

cc = CoinCap(key=None)
cc.get_asset(id="bitcoin")
```

## Testing

```bash
virtualenv venv
source ./venv/bin/activate
pip install -r dev_requirements.txt
pytest
```
