import pytest
from methods.car_method import CarMethod
from settings.project_setting import TEST_URL, test_car
from pages.header_page import HeaderPage
from pages.module_page import ModulePage
from pages.garage_page import GaragePage


@pytest.mark.usefixtures('get_driver')
class TestGarage(CarMethod):
    expected_car = 'TOYOTA YARIS (P13) 1.0 (KSP130)'
    expected_car_year = '2013'

    @pytest.mark.smoke
    @pytest.mark.garage
    @pytest.mark.skip
    def test_add_update_delete_car_by_my_car(self):
        self.driver.get(TEST_URL)
        my_car = HeaderPage(self.driver)
        module_car = ModulePage(self.driver)
        self.add_car(self.driver, test_car.get('manufacture'), test_car.get('model'), test_car.get('type_model'),
                     test_car.get('modification'), 'my_car', test_car.get('year'))
        self.change_year_vin(self.driver, 'module', vin=test_car.get('vin'))
        assert test_car.get('vin') in module_car.text_car_vin('my_cars')
        assert test_car.get('vin') in module_car.text_car_vin('chosen_car')
        self.delete_chosen_car(self.driver, 'module')
        assert my_car.check_empty_my_car

    @pytest.mark.smoke
    @pytest.mark.garage
    @pytest.mark.skip
    def test_check_name_my_car(self):
        self.driver.get(TEST_URL)
        my_car = HeaderPage(self.driver)
        module_car = ModulePage(self.driver)
        self.add_car(self.driver, test_car.get('manufacture'), test_car.get('model'), test_car.get('type_model'),
                     test_car.get('modification'), 'my_car', test_car.get('year'))
        assert '{}{}'.format(test_car.get('manufacture'), test_car.get('model')).upper() == my_car.text_my_car
        assert set(self.expected_car) == module_car.set_text_car_name

    @pytest.mark.smoke
    @pytest.mark.garage
    @pytest.mark.skip
    def test_add_update_delete_car_by_parts_search(self):
        self.driver.get(TEST_URL)
        my_car = HeaderPage(self.driver)
        module_car = ModulePage(self.driver)
        garage = GaragePage(self.driver)
        self.add_car(self.driver, test_car.get('manufacture'), test_car.get('model'), test_car.get('type_model'),
                     test_car.get('modification'), 'parts_search', test_car.get('year'))
        my_car.click_my_car()
        module_car.click_button_go_to_garage()
        self.change_year_vin(self.driver, 'garage', year=self.expected_car_year, vin=test_car.get('vin'))
        assert test_car.get('vin') in garage.text_car_vin
        assert self.expected_car_year in garage.text_car_year
        self.delete_chosen_car(self.driver, 'garage')
        assert my_car.check_empty_my_car

    @pytest.mark.smoke
    @pytest.mark.garage
    def test_check_name_garage(self):
        self.driver.get(TEST_URL)
        my_car = HeaderPage(self.driver)
        module_car = ModulePage(self.driver)
        garage = GaragePage(self.driver)
        self.add_car(self.driver, test_car.get('manufacture'), test_car.get('model'), test_car.get('type_model'),
                     test_car.get('modification'), 'parts_search', test_car.get('year'))
        assert '{}{}'.format(test_car.get('manufacture'), test_car.get('model')).upper() == my_car.text_my_car
        my_car.click_my_car()
        module_car.click_button_go_to_garage()
        assert self.expected_car == garage.text_car_name
