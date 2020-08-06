import pytest
from methods.car_method import CarMethod
from settings.project_setting import TEST_URL, test_car
from pages.header_page import HeaderPage
from pages.module_page import ModulePage


@pytest.mark.usefixtures('get_driver')
class TestGarage(CarMethod):

    @pytest.mark.smoke
    def test_add_update_delete_car_by_my_car(self):
        self.driver.get(TEST_URL)
        my_car = HeaderPage(self.driver)
        module_car = ModulePage(self.driver)
        self.add_car(self.driver, test_car.get('manufacture'), test_car.get('model'), test_car.get('type_model'),
                     test_car.get('modification'), 'my_car', test_car.get('year'))
        # assert test_car.get('manufacture').upper() in my_car.text_my_car
        self.change_year_vin(self.driver, vin=test_car.get('vin'))
        assert test_car.get('vin') in module_car.car_vin('my_cars')
        assert test_car.get('vin') in module_car.car_vin('chosen_car')
        self.delete_chosen_car(self.driver)
        assert my_car.check_empty_my_car

    def test_add_update_delete_car_by_parts_search(self):
        import time
        self.driver.get(TEST_URL)
        my_car = HeaderPage(self.driver)
        module_car = ModulePage(self.driver)
        self.add_car(self.driver, test_car.get('manufacture'), test_car.get('model'), test_car.get('type_model'),
                     test_car.get('modification'), 'parts_search', test_car.get('year'))
        my_car.click_my_car()
        module_car.click_button_go_to_garage()
        self.change_year_vin(self.driver, year='2013')
        assert '2013' in module_car.car_vin('my_cars')

        time.sleep(10)


    def test_add_car_by_garage(self):
        pass
