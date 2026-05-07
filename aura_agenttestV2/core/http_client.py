import requests
import logging
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HttpClient")

class HttpClient:
    def __init__(self, base_url="", timeout=10, retry=3):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.retry = retry
        self.session = requests.Session()

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=1, max=5),
        retry=retry_if_exception_type((requests.exceptions.Timeout, requests.exceptions.ConnectionError))
    )
    def get(self, path, **kwargs):
        url = self.base_url + path
        logger.info(f"[GET] {url}")
        resp = self.session.get(url, timeout=self.timeout, **kwargs)
        logger.info(f"[STATUS] {resp.status_code}")
        return resp

    @retry(stop=stop_after_attempt(3))
    def post(self, path, json=None, **kwargs):
        url = self.base_url + path
        logger.info(f"[POST] {url} | {json}")
        resp = self.session.post(url, json=json, timeout=self.timeout, **kwargs)
        logger.info(f"[STATUS] {resp.status_code}")
        return resp