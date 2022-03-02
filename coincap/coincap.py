"""CoinCap API wrapper.

Web: https://coincap.io/
Doc: https://docs.coincap.io/
"""
import logging
from typing import Any, Dict, List, Optional

import requests

from .utils import clean_params

logger = logging.getLogger(__name__)


class CoinCapAPIError(Exception):
    def __init__(self, response, message=""):
        super().__init__(message)
        self.response = response
        self.message = message

    def __str__(self):
        return f"{self.response.status_code} {self.response.content.decode()}"


class CoinCap:
    """CoinCap API wrapper.

    Web: https://coincap.io/
    Doc: https://docs.coincap.io/
    """

    BASE_URL = "https://api.coincap.io/v2/"

    def __init__(
        self, key: Optional[str] = None, fail_silently: bool = False
    ) -> None:
        """Init the CoinCap API.

        Args:
            key (:obj:`str`, optional): CoinCap API key.
            fail_silently (:obj:`bool`, optional): If true an exception should
                be raise in case of wrong status code. Defaults to False.
        """
        self.key = key
        self.fail_silently = fail_silently

    def _get_headers(self) -> Dict[str, str]:
        headers = dict()
        if self.key:
            headers.update({"Authorization": f"Bearer {self.key}"})
        return headers

    def _get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """Get requests to the specified path on CoinCap API."""
        r = requests.get(
            url=self.BASE_URL + path,
            params=clean_params(params),
            headers=self._get_headers(),
        )

        if r.status_code == 200:
            return r.json()

        details = r.content.decode()
        try:
            details = r.json()
        except Exception:
            pass

        if not self.fail_silently:
            logger.warning(
                f"CoinCap API error {r.status_code} on {path}: {details}"
            )
            self._fail(r)
        else:
            logger.info(
                f"CoinCap API silent error {r.status_code} on {path}: "
                f"{details}"
            )
            return None

    def _fail(self, r):
        raise CoinCapAPIError(response=r)

    def get_assets(
        self,
        search: Optional[str] = None,
        ids: Optional[List[str]] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        return self._get(
            "assets",
            params={
                "search": search,
                "ids": ids,
                "limit": limit,
                "offset": offset,
            },
        )

    def get_asset(self, id: str):
        return self._get(f"assets/{id}")

    def get_asset_history(
        self,
        id: str,
        interval: str,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ):
        return self._get(
            f"assets/{id}/history?interval={interval}",
            params={
                "interval": interval,
                "start": start,
                "end": end,
            },
        )

    def get_asset_markets(
        self,
        id: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        return self._get(
            f"assets/{id}/markets",
            params={
                "limit": limit,
                "offset": offset,
            },
        )

    def get_rates(self):
        return self._get("rates")

    def get_rate(self, id: str):
        return self._get(f"rates/{id}")

    def get_exchanges(self):
        return self._get("exchanges")

    def get_exchange(self, id: str):
        return self._get(f"exchanges/{id}")

    def get_markets(
        self,
        exchange_id: Optional[str] = None,
        base_symbol: Optional[str] = None,
        quote_symbol: Optional[str] = None,
        base_id: Optional[str] = None,
        quote_id: Optional[str] = None,
        asset_symbol: Optional[str] = None,
        asset_id: Optional[str] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
    ):
        return self._get(
            "markets",
            params={
                "exchangeId": exchange_id,
                "baseSymbol": base_symbol,
                "quoteSymbol": quote_symbol,
                "baseId": base_id,
                "quoteId": quote_id,
                "assetSymbol": asset_symbol,
                "assetId": asset_id,
                "limit": limit,
                "offset": offset,
            },
        )

    def get_candles(
        self,
        exchange: str,
        interval: str,
        base_id: str,
        quote_id: str,
        start: Optional[int] = None,
        end: Optional[int] = None,
    ):
        return self._get(
            path="candles",
            params={
                "exchange": exchange,
                "interval": interval,
                "baseId": base_id,
                "quoteId": quote_id,
                "start": start,
                "end": end,
            },
        )
