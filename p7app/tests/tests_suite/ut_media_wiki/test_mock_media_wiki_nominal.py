from p7app.utils.wikimedia import get_data_from_wiki_media
from config import WikiMediaUrl, GoogleKey

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
                           "Gaulle</span>, "
                           "<span class=\"postal-code\">75008</span> <span "
                           "class=\"locality\">Paris</span>, "
                           "<span class=\"country-name\">France</span>",
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
            "icon": "https://maps.gstatic.com/mapfiles/place_api/icons"
                    "/museum-71.png",
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
                                         "/AAAAAAAAAAI/AAAAAAAAAAA/wNV1fm"
                                         "-R6CY/s128 "
                                         "-c0x00000000-cc-rp-mo-ba4/photo.jpg",
                    "rating": 5,
                    "relative_time_description": "il y a 2 mois",
                    "text": "Une oeuvre d'art géante, Magnifique  même en "
                            "hiver . "
                            "Définitivement un incontournable lors d'un "
                            "séjour à Paris . Le site est très très "
                            "achalandé même "
                            "en janvier . Accès très bien fait et c'est "
                            "très facile de s'y rendre en bus ou en métro. "
                            "J'aurais "
                            "bien aimé en apprendre plus sur son "
                            "histoire mais le temps était limité.",
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
                            "préparez vos petites jambes pour ces longs "
                            "escaliers en colimaçon, mais le spectacle là "
                            "haut en "
                            "vaut plus que la peine. Le personnel est un "
                            "peu froid mais bon vu le nombre de personnes qui "
                            "défilent cela nous a pas étonné mais rien qui "
                            "ne vaille de pas profiter de ce magnifique "
                            "spectacle.",
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
                            "moment "
                            "👍 \n\nL'arc de triomphe est une "
                            "merveille d'architecture...!\nOn a une superbe "
                            "vue de "
                            "Paris en haut ! 😊\n\n\"Ils sont fous ces "
                            "romains!\" 🙉😆",
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
                            "bon accueil.\nDommage, manque de sanitaires "
                            "(beaucoup d'attente pour le nombres de visiteurs)"
                    ,
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
                            "Paris .  Emblème   de   la   France "
                            "commémorant   les   victoires  de  Napoléon .   "
                            "Se "
                            "trouve   la   tombe   du   soldat   inconnu "
                            "avec   la   flamme  ravivée  chaque  soir  en   "
                            "souvenir   des   deux   guerres   mondiales . "
                            "Lieu   de   respect .  De  cet   édifice   "
                            "partent  les "
                            "  plus  grandes  avenues  de  Paris "
                            "formant  une  étoile . Pas  d'ascenseur  sauf  "
                            "pour "
                            "les  personnes avec  un  handicap   pour "
                            "monter  les   284   marches  . Très   beau   "
                            "panorama "
                            "sur  tout   Paris  😍.  Endroit   de "
                            "rassemblement   et   de   principales  "
                            "manifestations "
                            "nationales .  A  voir .",
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
            "16": {
                "pageid": 16,
                "ns": 0,
                "title": "Arc de triomphe de l'Étoile",
                "index": -1,
                "links": [
                    {
                        "ns": 0,
                        "title": "16e arrondissement de Paris"
                    },
                    {
                        "ns": 0,
                        "title": "17e arrondissement de Paris"
                    },
                    {
                        "ns": 0,
                        "title": "1806 en architecture"
                    },
                    {
                        "ns": 0,
                        "title": "1810"
                    },
                    {
                        "ns": 0,
                        "title": "1811"
                    },
                    {
                        "ns": 0,
                        "title": "1814"
                    },
                    {
                        "ns": 0,
                        "title": "1815"
                    },
                    {
                        "ns": 0,
                        "title": "1829 en littérature"
                    },
                    {
                        "ns": 0,
                        "title": "1836"
                    },
                    {
                        "ns": 0,
                        "title": "1836 en architecture"
                    }
                ],
                "extract": "<p>L’<b>arc de triomphe de l’Étoile</b>, souvent "
                           "appelé simplement l’<b>Arc de "
                           "triomphe</b>, dont la construction, décidée par "
                           "l'empereur <span>Napoléon <abbr "
                           "class=\"abbr\" title=\"premier\"><span>I</span"
                           "><sup>er</sup></abbr></span>, "
                           "débuta en 1806 et s'acheva en 1836 sous "
                           "Louis-Philippe, est situé à Paris, dans les <abbr "
                           "class=\"abbr\" title=\"Huitième\">8<sup>e</sup"
                           "></abbr>, <abbr class=\"abbr\" "
                           "title=\"Seizième\">16<sup>e</sup></abbr>, "
                           "et <abbr class=\"abbr\" "
                           "title=\"Dix-septième\">17<sup>e</sup></abbr> "
                           "arrondissements.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-21T17:08:31Z",
                "lastrevid": 169552320,
                "length": 56222,
                "fullurl": "https://fr.wikipedia.org/wiki"
                           "/Arc_de_triomphe_de_l%27%C3%89toile",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Arc_de_triomphe_de_l%27%C3%89toile&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Arc_de_triomphe_de_l%27%C3%89toile",
                "preload": ""
            },
            "17324": {
                "pageid": 17324,
                "ns": 0,
                "title": "Place Charles-de-Gaulle",
                "index": 0,
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n<p>La <b>place "
                           "Charles-de-Gaulle</b>, aussi appelée la "
                           "<b>place de l’Étoile</b>, est un rond-point "
                           "situé à Paris, à cheval sur les "
                           "8<sup>e</sup>, 16<sup>e</sup> et 17<sup>e</sup> "
                           "arrondissements. Malgré le fait qu'elle a "
                           "été officiellement rebaptisée en 1970, son "
                           "ancien nom <i>de l'Étoile</i> reste plus "
                           "fréquent. Au centre de cette place se trouve "
                           "l'Arc de Triomphe.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-19T11:03:20Z",
                "lastrevid": 169398239,
                "length": 25304,
                "fullurl": "https://fr.wikipedia.org/wiki/Place_Charles-de"
                           "-Gaulle",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Place_Charles-de-Gaulle&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki/Place_Charles"
                                "-de-Gaulle",
                "preload": ""
            },
            "117229": {
                "pageid": 117229,
                "ns": 0,
                "title": "Charles de Gaulle - Étoile (métro de Paris)",
                "index": 1,
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n<p><b>Charles "
                           "de Gaulle - Étoile</b> est une station "
                           "des lignes 1, 2 et 6 du métro de Paris, "
                           "implantée sous la place Charles-de-Gaulle. "
                           "Initialement appelée <b>Étoile</b>, elle est "
                           "située à la limite des 8<sup>e</sup>, "
                           "16<sup>e</sup> et 17<sup>e</sup> arrondissements "
                           "de Paris.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-19T11:04:14Z",
                "lastrevid": 169187817,
                "length": 19299,
                "fullurl": "https://fr.wikipedia.org/wiki/Charles_de_Gaulle_"
                           "-_%C3%89toile_(m%C3%A9tro_de_Paris)",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Charles_de_Gaulle_-_%C3%89toile_( "
                           "m%C3%A9tro_de_Paris)&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Charles_de_Gaulle_-_%C3%89toile_("
                                "m%C3%A9tro_de_Paris)",
                "preload": ""
            },
            "169220": {
                "pageid": 169220,
                "ns": 0,
                "title": "Tombe du Soldat inconnu (France)",
                "index": 2,
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n\n<p>La "
                           "<b>tombe du Soldat inconnu</b> est une "
                           "sépulture installée à Paris sous l'arc de "
                           "triomphe de l'Étoile depuis le <time "
                           "class=\"nowrap date-lien\" "
                           "datetime=\"1920-11-11\" "
                           "data-sort-value=\"1920-11-11\">11 "
                           "novembre 1920</time>. Elle accueille le corps "
                           "d'un soldat non identifié, mort lors de la "
                           "Première Guerre mondiale et reconnu français, "
                           "pour commémorer symboliquement l'ensemble "
                           "des soldats morts pour la France au cours de "
                           "l'histoire.\n</p><p>La sépulture, "
                           "entourée de bornes de métal noir reliées entre "
                           "elles par des chaînes, se compose d'une "
                           "dalle de granite de Vire sur laquelle est "
                           "inscrite l'épitaphe&#160;: <q "
                           "class=\"citation\">Ici repose un soldat français "
                           "mort pour la Patrie — 1914 - 1918</q>. "
                           "En 1923, une flamme éternelle est ajoutée, "
                           "ravivée tous les jours.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-23T16:38:17Z",
                "lastrevid": 169478115,
                "length": 22588,
                "fullurl": "https://fr.wikipedia.org/wiki"
                           "/Tombe_du_Soldat_inconnu_(France)",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Tombe_du_Soldat_inconnu_(France)&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Tombe_du_Soldat_inconnu_(France)",
                "preload": ""
            },
            "609765": {
                "pageid": 609765,
                "ns": 0,
                "title": "Gare de Charles-de-Gaulle - Étoile",
                "index": 3,
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n<p>La <b>gare "
                           "de Charles-de-Gaulle - Étoile</b> est une "
                           "gare ferroviaire française de la ligne A du RER, "
                           "située à la limite des 8<sup>e</sup>, "
                           "16<sup>e</sup> et 17<sup>e</sup> arrondissements "
                           "de Paris.\n</p><p>Elle est mise en "
                           "service en 1970 par la Régie autonome des "
                           "transports parisiens (RATP).</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-20T22:57:03Z",
                "lastrevid": 167537264,
                "length": 8871,
                "fullurl": "https://fr.wikipedia.org/wiki/Gare_de_Charles-de"
                           "-Gaulle_-_%C3%89toile",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Gare_de_Charles-de-Gaulle_-_%C3%89toile&action "
                           "=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Gare_de_Charles-de-Gaulle_-_%C3%89toile",
                "preload": ""
            },
            "5172066": {
                "pageid": 5172066,
                "ns": 0,
                "title": "Hôtel Landolfo de Carcano",
                "index": 4,
                "extract": "<p>L'<b>hôtel Landolfo de Carcano</b> est un "
                           "hôtel particulier dans le <abbr "
                           "class=\"abbr\" title=\"Huitième\">8<sup>e</sup"
                           "></abbr>&#160;arrondissement de Paris, 1, "
                           "rue de Tilsitt, qui donne sur la place de "
                           "l'Étoile. \n</p><p>Construit en 1867 par "
                           "Charles Rohault de Fleury, il doit son nom à sa "
                           "commanditaire et première propriétaire, "
                           "Anne-Marie Adèle Caussin dite <i>Madame de "
                           "Cassin</i> , et qui épousa le Marquis Landolfo "
                           "de Carcano en 1889. \n</p><p>Il est actuellement "
                           "le siège de l'Ambassade du Qatar en "
                           "France.\n</p><p>Il fait partie des douze hôtels "
                           "particuliers dits <i>des Maréchaux, "
                           "</i> qui ont été dessinés par Jacques-Ignace "
                           "Hittorff en 1853, sur ordre de l'Empereur "
                           "Napoléon III, lors des grands travaux de "
                           "réaménagement de l'Étoile, "
                           "devenue officiellement place Charles-de-Gaulle "
                           "en 1970.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-20T11:24:54Z",
                "lastrevid": 169470089,
                "length": 4999,
                "fullurl": "https://fr.wikipedia.org/wiki/H%C3"
                           "%B4tel_Landolfo_de_Carcano",
                "editurl": "https://fr.wikipedia.org/w/index.php?title=H%C3"
                           "%B4tel_Landolfo_de_Carcano&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki/H%C3"
                                "%B4tel_Landolfo_de_Carcano",
                "preload": ""
            },
            "5464600": {
                "pageid": 5464600,
                "ns": 0,
                "title": "Passage du Souvenir",
                "index": 5,
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n<p>Le "
                           "<b>passage du Souvenir</b>, ou <b>passage "
                           "souterrain de l'Arc de Triomphe</b>, est un "
                           "passage piéton souterrain entre l'avenue des "
                           "Champs-Élysées à l'est et l'avenue de la "
                           "Grande-Armée à l'ouest.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-19T09:24:40Z",
                "lastrevid": 155225125,
                "length": 2589,
                "fullurl": "https://fr.wikipedia.org/wiki/Passage_du_Souvenir",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Passage_du_Souvenir&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Passage_du_Souvenir",
                "preload": ""
            },
            "5821701": {
                "pageid": 5821701,
                "ns": 0,
                "title": "Ambassade du Qatar en France",
                "index": 6,
                "extract": "<p class=\"mw-empty-elt\">\n</p>\n<p>L'<b"
                           ">ambassade du Qatar en France</b> est la "
                           "représentation diplomatique de l'État du Qatar "
                           "auprès de la République française. Elle "
                           "est située dans le <abbr class=\"abbr\" "
                           "title=\"Huitième\">8<sup>e</sup></abbr>&#160"
                           ";arrondissement de Paris, la capitale du "
                           "pays. \n</p><p>Son ambassadeur est, depuis <time "
                           "class=\"nowrap\" datetime=\"2017-02\" "
                           "data-sort-value=\"2017-02\">février 2017</time>, "
                           "Khalid Bin Rashid Al-Mansouri.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-19T09:26:34Z",
                "lastrevid": 169347893,
                "length": 6710,
                "fullurl": "https://fr.wikipedia.org/wiki"
                           "/Ambassade_du_Qatar_en_France",
                "editurl": "https://fr.wikipedia.org/w/index.php?title"
                           "=Ambassade_du_Qatar_en_France&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki"
                                "/Ambassade_du_Qatar_en_France",
                "preload": ""
            },
            "6731270": {
                "pageid": 6731270,
                "ns": 0,
                "title": "Hôtel de Günzburg",
                "index": 7,
                "extract": "<p><b>L'Hôtel de Günzburg</b> est un hôtel "
                           "particulier situé à Paris en France.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-20T11:24:54Z",
                "lastrevid": 169470142,
                "length": 4364,
                "fullurl": "https://fr.wikipedia.org/wiki/H%C3%B4tel_de_G%C3"
                           "%BCnzburg",
                "editurl": "https://fr.wikipedia.org/w/index.php?title=H%C3"
                           "%B4tel_de_G%C3%BCnzburg&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki/H%C3"
                                "%B4tel_de_G%C3%BCnzburg",
                "preload": ""
            },
            "12185664": {
                "pageid": 12185664,
                "ns": 0,
                "title": "Barrière de l'Étoile",
                "index": 8,
                "extract": "<p>La <b> barrière de l’Étoile</b>,  <b>barrière "
                           "des Champs-Elysées</b> ou <b>barrière de "
                           "Neuilly</b>, était une barrière d'octroi de "
                           "l'enceinte des Fermiers généraux ouverte en "
                           "1788 et démolie en 1860.</p>",
                "contentmodel": "wikitext",
                "pagelanguage": "fr",
                "pagelanguagehtmlcode": "fr",
                "pagelanguagedir": "ltr",
                "touched": "2020-04-19T11:57:58Z",
                "lastrevid": 168801612,
                "length": 7913,
                "fullurl": "https://fr.wikipedia.org/wiki/Barri%C3%A8re_de_l"
                           "%27%C3%89toile",
                "editurl": "https://fr.wikipedia.org/w/index.php?title=Barri"
                           "%C3%A8re_de_l%27%C3%89toile&action=edit",
                "canonicalurl": "https://fr.wikipedia.org/wiki/Barri%C3"
                                "%A8re_de_l%27%C3%89toile",
                "preload": ""
            }
        }
    }
}

expected_assert_result = {
    "pageid": 16,
    "ns": 0,
    "title": "Arc de triomphe de l'Étoile",
    "index": -1,
    "links": [
        {
            "ns": 0,
            "title": "16e arrondissement de Paris"
        },
        {
            "ns": 0,
            "title": "17e arrondissement de Paris"
        },
        {
            "ns": 0,
            "title": "1806 en architecture"
        },
        {
            "ns": 0,
            "title": "1810"
        },
        {
            "ns": 0,
            "title": "1811"
        },
        {
            "ns": 0,
            "title": "1814"
        },
        {
            "ns": 0,
            "title": "1815"
        },
        {
            "ns": 0,
            "title": "1829 en littérature"
        },
        {
            "ns": 0,
            "title": "1836"
        },
        {
            "ns": 0,
            "title": "1836 en architecture"
        }
    ],
    "extract": "<p>L’<b>arc de triomphe de l’Étoile</b>, souvent "
               "appelé simplement l’<b>Arc de "
               "triomphe</b>, dont la construction, décidée par "
               "l'empereur <span>Napoléon <abbr "
               "class=\"abbr\" title=\"premier\"><span>I</span"
               "><sup>er</sup></abbr></span>, "
               "débuta en 1806 et s'acheva en 1836 sous "
               "Louis-Philippe, est situé à Paris, dans les <abbr "
               "class=\"abbr\" title=\"Huitième\">8<sup>e</sup"
               "></abbr>, <abbr class=\"abbr\" "
               "title=\"Seizième\">16<sup>e</sup></abbr>, "
               "et <abbr class=\"abbr\" "
               "title=\"Dix-septième\">17<sup>e</sup></abbr> "
               "arrondissements.</p>",
    "contentmodel": "wikitext",
    "pagelanguage": "fr",
    "pagelanguagehtmlcode": "fr",
    "pagelanguagedir": "ltr",
    "touched": "2020-04-21T17:08:31Z",
    "lastrevid": 169552320,
    "length": 56222,
    "fullurl": "https://fr.wikipedia.org/wiki"
               "/Arc_de_triomphe_de_l%27%C3%89toile",
    "editurl": "https://fr.wikipedia.org/w/index.php?title"
               "=Arc_de_triomphe_de_l%27%C3%89toile&action=edit",
    "canonicalurl": "https://fr.wikipedia.org/wiki"
                    "/Arc_de_triomphe_de_l%27%C3%89toile",
    "preload": ""
}


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
    print(answer)

    assert answer["status"] == 'OK'
    assert answer["wikimedia"] == expected_assert_result
