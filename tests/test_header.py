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
               'АУДІО ТА ЕЛЕКТРОНІКА', "ІНТЕР'ЄР", "ЕКСТЕР'ЄР", 'ІНСТРУМЕНТИ І ОБЛАДНАННЯ',
               'СПОРТ, ВІДПОЧИНОК, ТУРИЗМ'),
        'EN': ('REPAIR PARTS', 'BODY PARTS', 'OILS & FLUIDS', 'WHEELS & TIRES', 'LIGHTING', 'AUDIO & ELECTRONICS',
               'INTERIOR', 'EXTERIOR', 'TOOLS & GARAGE', 'SPORTS, RECREATION, TOURISM')

    }

    user_menu_elements = {
        'RU': ('МОЕ\nАВТО\nНет авто', 'ЛИЧНЫЙ\nКАБИНЕТ', 'МОЯ\nКОРЗИНА'),
        'UA': ('МОЄ\nАВТО\nНемає авто', 'ОСОБИСТИЙ\nКАБІНЕТ', 'МІЙ\nКОШИК'),
        'EN': ('MY\nCAR\nNo car', 'MY\nPROFILE', 'MY\nCART')

    }

    type_menu = ('mega', 'user')

    @pytest.mark.header
    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.parametrize('type_menu', type_menu)
    def test_menu_element_name(self, current_language, type_menu):
        self.driver.get(TEST_URL)
        menu = {
            'mega': (self.mega_menu_elements, HeaderPage(self.driver).text_mega_menu),
            'user': (self.user_menu_elements, HeaderPage(self.driver).text_user_menu)
        }
        self.change_language(self.driver, current_language)
        expected_menu = menu.get(type_menu)[0].get(current_language)
        actual_menu = menu.get(type_menu)[1]()
        assert len(actual_menu) == len(expected_menu)
        for i in range(len(expected_menu)):
            assert actual_menu[i] == expected_menu[i]
