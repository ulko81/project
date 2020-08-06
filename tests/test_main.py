import pytest
from pages.main_page import MainPage
from settings.project_setting import TEST_URL, language
from methods.general_method import GeneralMethod


@pytest.mark.usefixtures('get_driver')
class Testmain(GeneralMethod):
    title_blocks = {
        'RU': ('НЕОБХОДИМОЕ ДЛЯ КАЖДОГО АВТО', 'ПОПУЛЯРНЫЕ МОДЕЛИ АВТО', 'ПОПУЛЯРНЫЕ МАРКИ', 'ПОПУЛЯРНЫЕ ЗАПЧАСТИ',
               'ПОПУЛЯРНЫЕ БРЕНДЫ АВТОЗАПЧАСТЕЙ', 'АВТОГИД ПОМОЩНИК ПО УДОБНОМУ ИСПОЛЬЗОВАНИЮ АВТОМОБИЛЯ'),
        'UA': ('НЕОБХІДНЕ ДЛЯ КОЖНОГО АВТО', 'ПОПУЛЯРНІ МОДЕЛІ АВТО', 'ПОПУЛЯРНІ МАРКИ', 'ПОПУЛЯРНІ ЗАПЧАСТИНИ',
               'ПОПУЛЯРНІ БРЕНДИ АВТОЗАПЧАСТИН', 'АВТОГІД ПОМІЧНИК ПО ЗРУЧНОМУ ВИКОРИСТАННЮ АВТОМОБІЛЯ'),
        'EN': ('NECESSARY FOR EVERY CAR', 'POPULAR CAR MODELS', 'POPULAR MANUFACTURES', 'POPULAR PARTS',
               'POPULAR SPARE PARTS BRANDS', 'AUTO GUIDANCE VEHICLE USABILITY ASSISTANT')
    }

    @pytest.mark.smoke
    @pytest.mark.main
    @pytest.mark.parametrize('current_language', language)
    def test_block_header_main_page(self, current_language):
        main = MainPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        expected_title_blocks = self.title_blocks.get(current_language)
        actual_title_blocks = main.text_title_block
        assert len(actual_title_blocks) == len(expected_title_blocks)
        for i in range(len(expected_title_blocks)):
            assert actual_title_blocks[i] == expected_title_blocks[i]


