from p7app.utils.wikimedia import *
from config import *

URL = WikiMediaUrl

user_request = dataset = {
        "messages": {
            "raw_message": "bbbbbbb adresse arc de triomphe ? rehghrgrghhreg",
            "parsed_message": "arc de triomphe "
        },
        "google": {
   "html_attributions": [],
   "result": {
      "address_components": [
         {
            "long_name": "Place Charles de Gaulle",
            "short_name": "Place Charles de Gaulle",
            "types": [
               "route"
            ]
         },
         {
            "long_name": "Paris",
            "short_name": "Paris",
            "types": [
               "locality",
               "political"
            ]
         },
         {
            "long_name": "Arrondissement de Paris",
            "short_name": "Arrondissement de Paris",
            "types": [
               "administrative_area_level_2",
               "political"
            ]
         },
         {
            "long_name": "Île-de-France",
            "short_name": "IDF",
            "types": [
               "administrative_area_level_1",
               "political"
            ]
         },
         {
            "long_name": "France",
            "short_name": "FR",
            "types": [
               "country",
               "political"
            ]
         },
         {
            "long_name": "75008",
            "short_name": "75008",
            "types": [
               "postal_code"
            ]
         }
      ],
      "adr_address": "<span class=\"street-address\">Place Charles de Gaulle</span>, <span class=\"postal-code\">75008</span> <span class=\"locality\">Paris</span>, <span class=\"country-name\">France</span>",
      "formatted_address": "Place Charles de Gaulle, 75008 Paris, France",
      "formatted_phone_number": "01 55 37 73 77",
      "geometry": {
         "location": {
            "lat": 48.8737917,
            "lng": 2.295027499999999
         },
         "viewport": {
            "northeast": {
               "lat": 48.8754163302915,
               "lng": 2.296284030291501
            },
            "southwest": {
               "lat": 48.8727183697085,
               "lng": 2.293586069708498
            }
         }
      },
      "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/museum-71.png",
      "id": "b4be70a61707e7ea54e7a55c2046b87e48459a01",
      "international_phone_number": "+33 1 55 37 73 77",
      "name": "Arc de Triomphe",
      "permanently_closed": True,
      "photos": [
         {
            "height": 3237,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/104889860001215768263\">Michael Camilleri</a>"
            ],
            "photo_reference": "CmRaAAAAMgyr5ckYEa-QJMW_SWsAcI612UKe5fkxBxVjuMJ0mur0dJOoUZhK3by9OZm81rI_1HgQ9sZQwKJsByyB_LWuuwuLWERjpimbnmGZ0u1622SbQQXEgWKjnTleS_4VhZH4EhDK77efTPmq8jaOmNaGCdlwGhSTJpgqFlb3IqhB5zBAG_06ZAPWPw",
            "width": 4942
         },
         {
            "height": 6936,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/116491272031923994830\">MAREK KOWALEWSKI</a>"
            ],
            "photo_reference": "CmRaAAAAH82_zM60wlSVXO9NM1r2XM13tL2BGOCxZVTRxaUoY81Wilyuq1vgl1rY3sghyCWfRwlFrGDHZwML9InNmQpbQ4p85pvmmKFVAqufo5R-2jNmAgXd2zCn8v6uQKtG3t7SEhBVg7vYj3mTgod2ZmTGfSTYGhS8wlaRIywit5HDdvKYIz0nE-XfXg",
            "width": 9248
         },
         {
            "height": 851,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/117992120144959411650\">Jose Manuel Ortega</a>"
            ],
            "photo_reference": "CmRaAAAAtb6N1_DUXRdacQzx1JAeJvyuIarZVLxJZ9D5chJWuonfIXU_8y4uXGJ39lFQIE2Af3ZJ3OSmcWSOkbj0WIEyPzFRopjeY0_zwrzDYZ4AyAwlpmJb-kUYFv4lsdCXUUpBEhDJSAm1o7BjMKj0U_8rMkl-GhQN0kcz6mXJWoL9Cwo-3IkitNV95Q",
            "width": 1064
         },
         {
            "height": 3072,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/117402460662180199876\">Karl Cassaigne</a>"
            ],
            "photo_reference": "CmRZAAAAvhT8PjkDL2i8OdvU128eQgq198DHKdQy0RfesPbBPYWOLaND2OytCLWxjY-QX56KvhqyhxVZRNCXW6LkHxmbf5wQ3Uffd70APz5Gujnhvk7CVBLD4BW_n8Ag6ibBEXm6EhCKtU5mynMV9c1xlTkizhUBGhRjnrGOI3LLr2VdN3xJjynC_loRmw",
            "width": 4608
         },
         {
            "height": 812,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/117992120144959411650\">Jose Manuel Ortega</a>"
            ],
            "photo_reference": "CmRaAAAA6NwWIBparavFxwuCrooCfBvR88FGgrHQDSQxbMB06OxqhRtIA_2V5VmavKdi0OdiCDPiYcxMICTTe-kFckF-EYiot6Sl86DV4Xa1Zp_fJ_74Zc4v9kcAuR7d2KFS5QesEhDGDTJasan1XGsnj2pNncLuGhRvPAuJ-uPoiQIqzfPmXTfFbqRqxA",
            "width": 1080
         },
         {
            "height": 3265,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/105721998315594007674\">Dermot Tuohey</a>"
            ],
            "photo_reference": "CmRaAAAA9njEAOvY0ioJvJeydDpEwtfFrassDTv1eRVnLS7askSXomU6c7YYAst_mjLsPRcTUxBjY3fUvZyIJY7-dQQYc3LJkwHN4jRTByXyoKtgMmZrmw2zP4wMvJGi9aobRxgGEhAdgEpGpWrWA8kopMsmyfCZGhRtpDFX27e2A8uUQEiOZVUMWXf6Cg",
            "width": 4898
         },
         {
            "height": 2988,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/114942348561696533574\">Grzegorz Wnuczyński</a>"
            ],
            "photo_reference": "CmRaAAAAYLWLmOawRUAKwa9AOc18Qbappdcl9QKQPE7D_zZwasXBK1dgpV7egxqsFn9n7bhYZvGe_eHOLaLXgQ_AwniIFML-_2zl-WO-aRR9K3adO9tfomOcvyoiCu4qBNjzMNiuEhDT7RPs1Ldxn43LFiLPo1i7GhQ3fiLFKXSOoLdjNjqUCD00oXGMUA",
            "width": 5312
         },
         {
            "height": 3456,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/112057105557586252193\">Tom Worthington</a>"
            ],
            "photo_reference": "CmRaAAAAbEIOdMV5U-XZGzOvg46G4Bt7QvBNBh0toj27U_G3sAu71pfcxXs8932rXscF1e4934ojejj5DqpeswNFHoULUS4e1IODEfqd5OvB1XKZVxcP8IIFU4p-Z3Lv8jnZ0fBuEhAKXhBI3HdAQ84geQj84BOkGhRE038oiN9wX8lYuJXhjmeB8mAT3A",
            "width": 4608
         },
         {
            "height": 1067,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/104501099239751679484\">Sebastien Gilson</a>"
            ],
            "photo_reference": "CmRaAAAAd7GKcxn2jircngKTs1pim8LlVunuTdtnqP-QYb9GmopsS_p5it-QxcLYqKM5W48ezDIUlAGcutiuZADxHU1awJLrKJLHGxmbJ1ljAGnokK6dGbLhQcRZOUxngXES_yS-EhA4kzE0_lzZZvs95PmcHkhgGhRWFHu0AkLMvzaTPu0OPHWmFEQ5ZQ",
            "width": 1600
         },
         {
            "height": 3456,
            "html_attributions": [
               "<a href=\"https://maps.google.com/maps/contrib/108293697255412776153\">Pablo Perez</a>"
            ],
            "photo_reference": "CmRaAAAA_phM6_U5pPHmKGHc4l87Ti4ypDpy12RB4Mq_nhCOdWDYWPeGpkxUUDSzr_yIugQhI_Je9h_uJE1BVf-YARVFN1-Ds38K2qlyonkNUFAeOio4q7-1H4Iblr5XrH7deh9wEhCJCWEojOW46etFkptb8WO5GhQGEswnxV3kerg0s6I5EEPgQ0zw9Q",
            "width": 4608
         }
      ],
      "place_id": "ChIJjx37cOxv5kcRPWQuEW5ntdk",
      "plus_code": {
         "compound_code": "V7FW+G2 Paris, France",
         "global_code": "8FW4V7FW+G2"
      },
      "rating": 4.7,
      "reference": "ChIJjx37cOxv5kcRPWQuEW5ntdk",
      "reviews": [
         {
            "author_name": "Jérôme Dupuis",
            "author_url": "https://www.google.com/maps/contrib/113868884665254056283/reviews",
            "language": "fr",
            "profile_photo_url": "https://lh4.ggpht.com/-NGT61MEpdV4/AAAAAAAAAAI/AAAAAAAAAAA/wNV1fm-R6CY/s128-c0x00000000-cc-rp-mo-ba4/photo.jpg",
            "rating": 5,
            "relative_time_description": "il y a 2 mois",
            "text": "Une oeuvre d'art géante, Magnifique  même en hiver . Définitivement un incontournable lors d'un séjour à Paris . Le site est très très achalandé même en janvier . Accès très bien fait et c'est très facile de s'y rendre en bus ou en métro. J'aurais bien aimé en apprendre plus sur son histoire mais le temps était limité.",
            "time": 1580127263
         },
         {
            "author_name": "la malle aux trésors Aline",
            "author_url": "https://www.google.com/maps/contrib/116414905598837289008/reviews",
            "language": "fr",
            "profile_photo_url": "https://lh4.ggpht.com/-Mc6Ths7lH10/AAAAAAAAAAI/AAAAAAAAAAA/Kc63XW6jvYc/s128-c0x00000000-cc-rp-mo-ba5/photo.jpg",
            "rating": 5,
            "relative_time_description": "il y a un mois",
            "text": "Whaou, que dire de ce monument... Une beauté d'architecture. Quel bonheur de découvrir ce monument de l'intérieur. Bon c'est haut, très haut, préparez vos petites jambes pour ces longs escaliers en colimaçon, mais le spectacle là haut en vaut plus que la peine. Le personnel est un peu froid mais bon vu le nombre de personnes qui défilent cela nous a pas étonné mais rien qui ne vaille de pas profiter de ce magnifique spectacle.",
            "time": 1583209450
         },
         {
            "author_name": "DAVID BOURE",
            "author_url": "https://www.google.com/maps/contrib/116161845012973921277/reviews",
            "language": "fr",
            "profile_photo_url": "https://lh4.ggpht.com/-KLAwrSEPRYE/AAAAAAAAAAI/AAAAAAAAAAA/oE1Oekt6c4s/s128-c0x00000000-cc-rp-mo-ba4/photo.jpg",
            "rating": 5,
            "relative_time_description": "il y a un mois",
            "text": "Sortie super sympa a faire le 1 er du mois (gratuit)...\n\nEn 40 ans, j'avais jamais eu l'opportunité de le visiter..ce fut un très bon moment 👍 \n\nL'arc de triomphe est une merveille d'architecture...!\nOn a une superbe vue de Paris en haut ! 😊\n\n\"Ils sont fous ces romains!\" 🙉😆",
            "time": 1583551277
         },
         {
            "author_name": "Laetitia LEJAL",
            "author_url": "https://www.google.com/maps/contrib/104597282296513337306/reviews",
            "language": "fr",
            "profile_photo_url": "https://lh6.ggpht.com/-Jj5HrWIq0IQ/AAAAAAAAAAI/AAAAAAAAAAA/khO5UlWIKAk/s128-c0x00000000-cc-rp-mo-ba4/photo.jpg",
            "rating": 5,
            "relative_time_description": "il y a un mois",
            "text": "Incomparable, à faire !!!!!!\nGratuit chaque 1er dimanche de chaque mois\nDu monde évidemment mais on circule bien tout de même.\nBoutique sympa, bon accueil.\nDommage, manque de sanitaires (beaucoup d'attente pour le nombres de visiteurs)",
            "time": 1584612018
         },
         {
            "author_name": "Evelyne BACLE",
            "author_url": "https://www.google.com/maps/contrib/107163186082405497187/reviews",
            "language": "fr",
            "profile_photo_url": "https://lh4.ggpht.com/-ZAOoDX77IMg/AAAAAAAAAAI/AAAAAAAAAAA/loeLyc6od8g/s128-c0x00000000-cc-rp-mo-ba7/photo.jpg",
            "rating": 5,
            "relative_time_description": "il y a 2 mois",
            "text": "Magnifique  et  imposant  monument  historique   de   Paris .  Emblème   de   la   France     commémorant   les   victoires  de  Napoléon .   Se   trouve   la   tombe   du   soldat   inconnu  avec   la   flamme  ravivée  chaque  soir  en   souvenir   des   deux   guerres   mondiales . Lieu   de   respect .  De  cet   édifice   partent  les   plus  grandes  avenues  de  Paris  formant  une  étoile . Pas  d'ascenseur  sauf  pour  les  personnes avec  un  handicap   pour  monter  les   284   marches  . Très   beau   panorama  sur  tout   Paris  😍.  Endroit   de   rassemblement   et   de   principales  manifestations  nationales .  A  voir .",
            "time": 1581831932
         }
      ],
      "scope": "GOOGLE",
      "types": [
         "tourist_attraction",
         "museum",
         "point_of_interest",
         "establishment"
      ],
      "url": "https://maps.google.com/?cid=15687558599447307325",
      "user_ratings_total": 140301,
      "utc_offset": 120,
      "vicinity": "Place Charles de Gaulle, Paris",
      "website": "http://arc-de-triomphe.monuments-nationaux.fr/"
   },
   "status": "OK"
},
        "wikimedia": None,
        "status": 'OK',
        "errors": {
            "parser": None,
            "searchAPI": None,
            "resultsAPI": None,
            "wikiAPI": None
        }
    }

payload = {
    "input": 'Mairie de Lille',
    "inputtype": "textquery",
    "key": GoogleKey
}

expected_return = {
    "continue": {
        "plcontinue": "16|0|1842_en_littérature",
        "continue": "||extracts|info"
    },
    "warnings": {
        "extracts": {
            "*": "The \"exsentences\" parameter may have unexpected results when used in HTML mode.\nHTML may be malformed and/or unbalanced and may omit inline images. Use at your own risk. Known problems are listed at https://www.mediawiki.org/wiki/Extension:TextExtracts#Caveats."
        },
        "main": {
            "*": "A POST request was made without a \"Content-Type\" header. This does not work reliably.\nSubscribe to the mediawiki-api-announce mailing list at <https://lists.wikimedia.org/mailman/listinfo/mediawiki-api-announce> for notice of API deprecations and breaking changes. Use [[Special:ApiFeatureUsage]] to see usage of deprecated features by your application.\nUnrecognized parameters: gsradius, gslimit."
        }
    },
    "query": {
        "pages": {

        }
    }
}

expected_assert_result = None


# Mocking of Media queryAPI getting with results
def test_media_wiki_API_with_results(monkeypatch):

    class MockMediaWikiApiResponse:

        status_code = 200

        def json(self):
            return expected_return

    # patching the post from requests
    def mock_requests_post(URL, params= payload):
        return MockMediaWikiApiResponse()

    monkeypatch.setattr('p7app.utils.wikimedia.requests.post', mock_requests_post)

    answer = get_data_from_wiki_media(user_request)


    assert answer["status"] == 'ZERO_RESULTS'
    assert answer["errors"]["wikiAPI"] == True
    assert answer["wikimedia"] == expected_assert_result


