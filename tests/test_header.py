import pytest
from pages.header_page import HeaderPage
from settings.project_setting import TEST_URL
from helpers.general_data import language
from helpers.methods import Methods


@pytest.mark.usefixtures('get_driver')
class TestHeader(Methods):

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

    contact_elements = {
        'RU': ('Форум', 'Оплата', 'Доставка', 'Возврат\nи гарантия', 'Помощь'),
        'UA': ('Форум', 'Оплата', 'Доставка', 'Повернення\nта гарантія', 'Допомога'),
        'EN': ('Forum', 'Payment', 'Delivery', 'Return\nand warranty', 'Help')
    }

    type_nav = (
        'mega',
        'user',
        'contact')

    @pytest.mark.header
    @pytest.mark.parametrize('current_language', language)
    @pytest.mark.parametrize('type_nav', type_nav)
    def test_menu_element_name(self, current_language, type_nav):
        self.driver.get(TEST_URL)
        menu = {
            'mega': (self.mega_menu_elements, HeaderPage(self.driver).text_mega_menu),
            'user': (self.user_menu_elements, HeaderPage(self.driver).text_user_menu),
            'contact': (self.contact_elements, HeaderPage(self.driver).text_contact)
        }
        self.change_language(self.driver, current_language)
        expected_menu = menu.get(type_nav)[0].get(current_language)
        actual_menu = menu.get(type_nav)[1]()

        assert len(actual_menu) == len(expected_menu)
        for i in range(len(expected_menu)):
            assert actual_menu[i] == expected_menu[i]
