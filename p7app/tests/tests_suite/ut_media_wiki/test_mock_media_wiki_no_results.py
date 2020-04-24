from config import WikiMediaUrl, GoogleKey
from p7app.utils.wikimedia import get_data_from_wiki_media

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
            "adr_address": "<span class=\"street-address\">Place Charles de "
                           "Gaulle</span>, <span "
                           "class=\"postal-code\">75008</span> <span "
                           "class=\"locality\">Paris</span>, <span "
                           "class=\"country-name\">France</span>",
            "formatted_address": "Place Charles de Gaulle, 75008 Paris, France"
            ,
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
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/museum"
                    "-71.png",
            "id": "b4be70a61707e7ea54e7a55c2046b87e48459a01",
            "international_phone_number": "+33 1 55 37 73 77",
            "name": "Arc de Triomphe",
            "permanently_closed": True,
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
                    "author_url": "https://www.google.com/maps/contrib"
                                  "/113868884665254056283/reviews",
                    "language": "fr",
                    "profile_photo_url": "https://lh4.ggpht.com/-NGT61MEpdV4"
                                         "/AAAAAAAAAAI/AAAAAAAAAAA/wNV1fm-R6CY"
                                         "/s128-c0x00000000-cc-rp-mo-ba4"
                                         "/photo.jpg",
                    "rating": 5,
                    "relative_time_description": "il y a 2 mois",
                    "text": "Une oeuvre d'art géante, Magnifique  même en "
                            "hiver . "
                            "Définitivement un incontournable lors "
                            "d'un séjour à Paris . Le site est très très "
                            "achalandé même en janvier . Accès très bien fait "
                            "et c'est très facile de s'y rendre en bus ou en "
                            "métro. J'aurais bien aimé en apprendre plus "
                            "sur son histoire mais le temps était limité.",
                    "time": 1580127263
                },
                {
                    "author_name": "la malle aux trésors Aline",
                    "author_url": "https://www.google.com/maps/contrib"
                                  "/116414905598837289008/reviews",
                    "language": "fr",
                    "profile_photo_url": "https://lh4.ggpht.com/-Mc6Ths7lH10"
                                         "/AAAAAAAAAAI/AAAAAAAAAAA"
                                         "/Kc63XW6jvYc/s128 "
                                         "-c0x00000000-cc-rp-mo-ba5/photo.jpg",
                    "rating": 5,
                    "relative_time_description": "il y a un mois",
                    "text": "Whaou, que dire de ce monument... Une beauté "
                            "d'architecture. Quel bonheur de découvrir ce "
                            "monument de l'intérieur. Bon c'est haut, très "
                            "haut, "
                            "préparez vos petites jambes pour ces "
                            "longs escaliers en colimaçon, mais le spectacle "
                            "là "
                            "haut en vaut plus que la peine. Le "
                            "personnel est un peu froid mais bon vu le "
                            "nombre de "
                            "personnes qui défilent cela nous a pas "
                            "étonné mais rien qui ne vaille de pas profiter "
                            "de ce "
                            "magnifique spectacle.",
                    "time": 1583209450
                },
                {
                    "author_name": "DAVID BOURE",
                    "author_url": "https://www.google.com/maps/contrib"
                                  "/116161845012973921277/reviews",
                    "language": "fr",
                    "profile_photo_url": "https://lh4.ggpht.com/-KLAwrSEPRYE"
                                         "/AAAAAAAAAAI/AAAAAAAAAAA"
                                         "/oE1Oekt6c4s/s128 "
                                         "-c0x00000000-cc-rp-mo-ba4/photo.jpg",
                    "rating": 5,
                    "relative_time_description": "il y a un mois",
                    "text": "Sortie super sympa a faire le 1 er du mois ("
                            "gratuit)...\n\nEn 40 ans, j'avais jamais eu "
                            "l'opportunité de le visiter..ce fut un très bon "
                            "moment 👍 \n\nL'arc de triomphe est une "
                            "merveille d'architecture...!\nOn a une superbe "
                            "vue "
                            "de Paris en haut ! 😊\n\n\"Ils sont fous "
                            "ces romains!\" 🙉😆",
                    "time": 1583551277
                },
                {
                    "author_name": "Laetitia LEJAL",
                    "author_url": "https://www.google.com/maps/contrib"
                                  "/104597282296513337306/reviews",
                    "language": "fr",
                    "profile_photo_url": "https://lh6.ggpht.com/-Jj5HrWIq0IQ"
                                         "/AAAAAAAAAAI/AAAAAAAAAAA"
                                         "/khO5UlWIKAk/s128 "
                                         "-c0x00000000-cc-rp-mo-ba4/photo.jpg",
                    "rating": 5,
                    "relative_time_description": "il y a un mois",
                    "text": "Incomparable, à faire !!!!!!\nGratuit chaque 1er "
                            "dimanche de chaque mois\nDu monde évidemment "
                            "mais on circule bien tout de même.\nBoutique "
                            "sympa, "
                            "bon accueil.\nDommage, manque de "
                            "sanitaires (beaucoup d'attente pour le nombres "
                            "de "
                            "visiteurs)",
                    "time": 1584612018
                },
                {
                    "author_name": "Evelyne BACLE",
                    "author_url": "https://www.google.com/maps/contrib"
                                  "/107163186082405497187/reviews",
                    "language": "fr",
                    "profile_photo_url": "https://lh4.ggpht.com/-ZAOoDX77IMg"
                                         "/AAAAAAAAAAI/AAAAAAAAAAA"
                                         "/loeLyc6od8g/s128 "
                                         "-c0x00000000-cc-rp-mo-ba7/photo.jpg",
                    "rating": 5,
                    "relative_time_description": "il y a 2 mois",
                    "text": "Magnifique  et  imposant  monument  historique  "
                            " de "
                            " Paris .  Emblème   de   la   France "
                            "commémorant   les   victoires  de  Napoléon .   "
                            "Se "
                            "trouve   la   tombe   du   soldat "
                            "inconnu  avec   la   flamme  ravivée  chaque  "
                            "soir "
                            "en   souvenir   des   deux   guerres "
                            "mondiales . Lieu   de   respect .  De  cet   "
                            "édifice "
                            "  partent  les   plus  grandes  avenues "
                            "de  Paris  formant  une  étoile . Pas  "
                            "d'ascenseur "
                            "sauf  pour  les  personnes avec  un "
                            "handicap   pour  monter  les   284   marches  . "
                            "Très "
                            "  beau   panorama  sur  tout   Paris "
                            "😍.  Endroit   de   rassemblement   et   de   "
                            "principales  manifestations  nationales .  A "
                            "voir .",
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
            "*": "The \"exsentences\" parameter may have unexpected results "
                 "when used in HTML mode.\nHTML may be "
                 "malformed and/or unbalanced and may omit inline images. "
                 "Use at your own risk. Known problems are "
                 "listed at https://www.mediawiki.org/wiki/Extension"
                 ":TextExtracts#Caveats. "
        },
        "main": {
            "*": "A POST request was made without a \"Content-Type\" header. "
                 "This does not work reliably.\nSubscribe "
                 "to the mediawiki-api-announce mailing list at "
                 "<https://lists.wikimedia.org/mailman/listinfo/mediawiki"
                 "-api-announce> for notice of API "
                 "deprecations and breaking changes. Use [["
                 "Special:ApiFeatureUsage]] to see usage of deprecated "
                 "features by your application.\nUnrecognized parameters: "
                 "gsradius, gslimit. "
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
    def mock_requests_post(URL, params=payload):
        return MockMediaWikiApiResponse()

    monkeypatch.setattr('p7app.utils.wikimedia.requests.post',
                        mock_requests_post)

    answer = get_data_from_wiki_media(user_request)

    assert answer["status"] == 'ZERO_RESULTS'
    assert answer["errors"]["wikiAPI"] == True
    assert answer["wikimedia"] == expected_assert_result
