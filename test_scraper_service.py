import pytest
from src.services.scraper_service import ScraperService
from requests.exceptions import RequestException

@pytest.fixture
def scraper():
    return ScraperService()

def test_valid_url(scraper):
    # 使用测试页面URL
    result = scraper.get_magnet_links("https://example.com/testpage")
    assert len(result) > 0
    assert all(link.startswith("magnet:") for link in result)

def test_invalid_url(scraper):
    with pytest.raises(RequestException):
        scraper.get_magnet_links("https://invalid.url.12345") 