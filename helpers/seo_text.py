microdata_types = {'main': 'Organization_WebSite',
                   '404': 'Organization_WebSite',
                   'registration': 'Organization_WebSite_BreadcrumbList',
                   'payment': 'Organization_WebSite_BreadcrumbList',
                   'search': 'Organization_WebSite_BreadcrumbList',
                   'balance': 'Organization_WebSite_BreadcrumbList',
                   'cart': 'Organization_WebSite_BreadcrumbList',
                   'notepad': 'Organization_WebSite_BreadcrumbList',
                   'brand': 'Organization_WebSite_BreadcrumbList',
                   'checkout': 'Organization_WebSite_BreadcrumbList',
                   'settings': 'Organization_WebSite_BreadcrumbList',
                   'orders': 'Organization_WebSite_BreadcrumbList',
                   'promotions': 'Organization_WebSite_BreadcrumbList',
                   'help': 'Organization_WebSite_BreadcrumbList',
                   'cars_catalog': 'Organization_WebSite_BreadcrumbList',
                   'spare_for_car': 'Organization_WebSite_BreadcrumbList',
                   'spare_for_car_model': 'Organization_WebSite_BreadcrumbList',
                   'category': 'Organization_WebSite_BreadcrumbList',
                   'catalog_with_car': 'Organization_WebSite_BreadcrumbList',
                   'catalog_with_car_model': 'Organization_WebSite_BreadcrumbList',
                   'catalog_with_brand': 'Organization_WebSite_BreadcrumbList',
                   'catalog_with_car_type_model': 'Organization_WebSite_BreadcrumbList',
                   'product_card_with_offers': 'Organization_WebSite_BreadcrumbList_Product',
                   'product_card_without_offers': 'Organization_WebSite_BreadcrumbList',
                   'full-search-product': 'Organization_WebSite_BreadcrumbList',
                   'full-search-category': 'Organization_WebSite_BreadcrumbList'}

microdata_organization = {'https://exist.ua': {
                    "@context": "http://schema.org",
                    "@type": "Organization",
                    "url": "https://exist.ua/",
                    "logo": "https://exist.ua/static/images/logo.svg"
                    }
                }

microdata_website = {'https://exist.ua': {
                    "@context": "http://schema.org",
                    "@type": "WebSite",
                    "url": "https://exist.ua/",
                    "potentialAction": {
                        "@type": "SearchAction",
                        "target": "https://exist.ua/search?query={search_term_string}",
                        "query-input": "required name=search_term_string"
                    }
                }
}

microdata_product = {
                "@context": "https://schema.org/",
                "@type": "Product",
                "name": "",
                "image": [],
                "description": "",
                "mpn": "",
                "sku": "",
                "brand": {
                    "@type": "Thing",
                    "name": ""
                }
                ,
                "review": {
                    "@type": "Review",
                    "author": "",
                    "datePublished": "",
                    "description": "",
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": "",
                        "bestRating": "",
                        "worstRating": ""
                    }
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "",
                    "reviewCount": "",
                    "bestRating": "",
                    "worstRating": ""
                }
                ,
                "offers": {
                    "@type": "Offer",
                    "url": "",
                    "priceCurrency": "UAH",
                    "price": "",
                    "itemCondition": "http://schema.org/NewCondition",
                    "availability": "http://schema.org/InStock"
                }
            }

seo_text_our_cities = {
    'RU': ("Наши офисы продаж в следующих городах Украины:• Винница • Днепр • Житомир • Запорожье • "
           "Ивано-Франковск • Киев • Краматорск • Кременчуг • Кривой Рог • Кропивницкий • Луцк • Львов • Мариуполь • "
           "Мукачево • Николаев • Одесса • Полтава • Ровно • Сумы • Тернополь • Харьков • Херсон • Хмельницкий • "
           "Черкассы • Чернигов • Черновцы"),
    'UA': ("Наші офіси продажів в наступних містах України:• Вінниця • Дніпро • Житомир • Запоріжжя • "
           "Івано-Франківськ • Київ • Краматорськ • Кременчук • Кривий Ріг • Кропивницький • Луцьк • Львів • "
           "Маріуполь • Мукачево • Миколаїв • Одеса • Полтава • Рівне • Суми • Тернопіль • Харків • Херсон • "
           "Хмельницький • Черкаси • Чернігів • Чернівці"),
    'EN': (".Our sales offices are in the following cities in Ukraine:• Vinnytsia • Dnepr • Zhytomyr • "
           "Zaporizhzhia • Ivano-Frankivs'k • Kiev • Kramatorsk • Kremenchug • Krivoy Rog • Kropyvnytskyi • Lutsk • "
           "Lviv •  Mariupol • Mukachevo • Nikolaev • Odessa • Poltava • Rivne • Sumy • Ternopil • Kharkov • "
           "Kherson • Khmelnitsky • Cherkasy • Chernigov • Chernivtsi")}

h1_group_on_manafacture = {
    'RU': 'МАСЛА НА TOYOTA (ТОЙОТА)',
    'UA': 'МАСЛА НА TOYOTA (ТОЙОТА)',
    'EN': 'OILS AND FLUIDS FOR TOYOTA'
    }

h1_group_on_model = {
    'RU': 'МАСЛА НА TOYOTA YARIS (ТОЙОТА ЯРИС)',
    'UA': 'МАСЛА НА TOYOTA YARIS (ТОЙОТА ЯРІС)',
    'EN': 'OILS AND FLUIDS FOR TOYOTA YARIS'
    }

all_type_manafactures = {
    'RU': 'ВСЕ МОДЕЛИ TOYOTA',
    'UA': 'ВСІ МОДЕЛІ TOYOTA',
    'EN': 'ALL MODELS TOYOTA'
}

all_type_models = {
    'RU': 'ВСЕ ТИПЫ МОДЕЛИ TOYOTA YARIS',
    'UA': 'ВСІ ТИПИ МОДЕЛЕЙ TOYOTA YARIS',
    'EN': 'ALL MODEL TYPES TOYOTA YARIS'
}
