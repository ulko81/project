import pytest

@pytest.mark.usefixtures('get_driver')
class TestCart:

    def test_cart(self):
        self.driver.get('https://exist.ua/')

    def test_cart2(self):
        self.driver.get('https://exist.ua/')