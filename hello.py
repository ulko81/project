from deepdiff import DeepDiff


d1 = {
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

d2 = {
                "@context": "https://schema.org/",
                "@type": "Product",
                "name": "Фильтр масляный Mahle/Knecht OC 90",
                "image": ["https://images2.exist.ua/media/images/products/2020/03/7603595_14305648_nDxDz1n.jpg","https://images2.exist.ua/media/images/products/2020/01/7448993_14305648_yPhbIJ5.jpg","https://images2.exist.ua/media/images/products/3416/14305648/436094.jpg","https://images2.exist.ua/media/images/products/2020/03/7603594_14305648.jpg","https://images2.exist.ua/media/images/products/2020/01/7448995_14305648_mbzkgEE.jpg","https://images2.exist.ua/media/images/products/2020/03/7644610_14305648.jpg"],
                "description": "||| MAHLE, MAHLEORIGINAL, MAHLEKOLBEN, MAHLEKNECHT, MAHLEFILTER, MAHLEFILTERS, MAHLEFILTR, MAHLEENGINE, MAHLEF, KNECHT, KNECHTFILTER, KNECHTMAHLEFILTER, KNECHTMAHLE, METALLEVE, OC90, 4009026037935, IC233602, MHOC90, ОС90, ЩС90 |||",
                "mpn": "OC90",
                "sku": "OC 90",
                "brand": {
                    "@type": "Thing",
                    "name": "Mahle/Knecht"
                }
                ,
                "review": {
                    "@type": "Review",
                    "author": "Дмитрий",
                    "datePublished": "30.06.2020",
                    "description": "Классный, не дорогой фильтр. Юзаю на Сенс, отлично стал, как родной.",
                    "reviewRating": {
                        "@type": "Rating",
                        "ratingValue": "5",
                        "bestRating": "5",
                        "worstRating": "1"
                    }
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": "5",
                    "reviewCount": "3",
                    "bestRating": "5",
                    "worstRating": "1"
                }
                ,
                "offers": {
                    "@type": "Offer",
                    "url": "https://exist.ua/mahle-knecht-brand/filtr-masljanyj-oc-90-14305477/",
                    "priceCurrency": "UAH",
                     "price": "118",
                    "itemCondition": "http://schema.org/NewCondition",
                    "availability": "http://schema.org/InStock"
                }
            }

ddiff = DeepDiff(d1, d2, view='tree')
print(ddiff.to_dict().get('dictionary_item_removed'))