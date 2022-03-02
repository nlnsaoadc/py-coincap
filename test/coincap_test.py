from unittest import TestCase, mock

from coincap.coincap import CoinCap


class CoinCapTestCase(TestCase):
    def setUp(self):
        self.api = CoinCap(key="123key")

    def test_get_headers(self):
        headers = self.api._get_headers()
        self.assertIsNotNone(headers["Authorization"])

    @mock.patch(
        "requests.get", return_value=mock.Mock(status_code=200, json=lambda: {})
    )
    def test_get(self, mock_get):
        self.api._get("test")
        mock_get.assert_called_once_with(
            url="https://api.coincap.io/v2/test",
            params=None,
            headers={"Authorization": "Bearer 123key"},
        )

    @mock.patch("coincap.coincap.logger.warning")
    @mock.patch(
        "requests.get",
        return_value=mock.Mock(
            status_code=404,
            json=lambda: {"message": "Not Found"},
            content=b"404 Not Found Message",
        ),
    )
    def test_get_404_status(self, mock_get, mock_log):
        with self.assertRaises(Exception) as context:
            self.api._get("/test")
        self.assertEqual(
            "404 404 Not Found Message",
            str(context.exception),
        )
        mock_log.assert_called_once()

    @mock.patch("coincap.coincap.logger.info")
    @mock.patch(
        "requests.get",
        return_value=mock.Mock(
            status_code=404,
            json=mock.Mock(side_effect=Exception("")),
            content=b"404 Not Found Message",
        ),
    )
    def test_get_404_status_fail_silently(self, mock_get, mock_log):
        self.api.fail_silently = True
        self.assertEqual(self.api._get("/test"), None)
        mock_log.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_assets(self, mock_get):
        self.api.get_assets()
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_asset(self, mock_get):
        self.api.get_asset(id="")
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_asset_history(self, mock_get):
        self.api.get_asset_history(id="", interval="")
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_asset_markets(self, mock_get):
        self.api.get_asset_markets(id="")
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_rates(self, mock_get):
        self.api.get_rates()
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_rate(self, mock_get):
        self.api.get_rate(id="")
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_exchanges(self, mock_get):
        self.api.get_exchanges()
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_exchange(self, mock_get):
        self.api.get_exchange(id="")
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_markets(self, mock_get):
        self.api.get_markets()
        mock_get.assert_called_once()

    @mock.patch("coincap.coincap.CoinCap._get")
    def test_get_candles(self, mock_get):
        self.api.get_candles(exchange="", interval="", base_id="", quote_id="")
        mock_get.assert_called_once()
