import pytest
from pages.header import HeaderPage
from settings.project_setting import TEST_URL, language
from methods.general_method import GeneralMethod


@pytest.mark.usefixtures('get_driver')
class TestHeader(GeneralMethod):
    mega_menu_elements = {
        'RU': ('АВТОЗАПЧАСТИ', 'КУЗОВНЫЕ ЗАПЧАСТИ', 'МАСЛА, ЖИДКОСТИ И АВТОХИМИЯ', 'ШИНЫ И ДИСКИ', 'ОСВЕЩЕНИЕ',
               'АУДИО И ЭЛЕКТРОНИКА', 'ИНТЕРЬЕР', 'ЭКСТЕРЬЕР', 'ИНСТРУМЕНТЫ И ОБОРУДОВАНИЕ', 'СПОРТ, ОТДЫХ, ТУРИЗМ'),
        'UA': ('АВТОЗАПЧАСТИНИ', 'КУЗОВНІ ЗАПЧАСТИНИ', 'МАСЛА, РІДИНИ І АВТОХІМІЯ', 'ШИНИ ТА ДИСКИ', 'ОСВІТЛЕННЯ',
                'АУДІО ТА ЕЛЕКТРОНІКА', "ІНТЕР'ЄР", "ЕКСТЕР'ЄР", 'ІНСТРУМЕНТИ І ОБЛАДНАННЯ', 'СПОРТ, ВІДПОЧИНОК, '
                                                                                             'ТУРИЗМ'),
        'EN': ('REPAIR PARTS', 'BODY PARTS', 'OILS & FLUIDS', 'WHEELS & TIRES', 'LIGHTING', 'AUDIO & ELECTRONICS',
                'INTERIOR', 'EXTERIOR', 'TOOLS & GARAGE', 'SPORTS, RECREATION, TOURISM')

    }

    @pytest.mark.header
    @pytest.mark.parametrize('current_language', language)
    def test_mega_menu_element_name(self, current_language):
        header = HeaderPage(self.driver)
        self.driver.get(TEST_URL)
        self.change_language(self.driver, current_language)
        expected_title_blocks = self.mega_menu_elements.get(current_language)
        actual_title_blocks = header.text_mega_menu
        assert len(actual_title_blocks) == len(expected_title_blocks)
        for i in range(len(expected_title_blocks)):
            assert actual_title_blocks[i] == expected_title_blocks[i]


