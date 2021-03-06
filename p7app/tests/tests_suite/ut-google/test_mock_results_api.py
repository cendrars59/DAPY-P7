from p7app.utils.google import get_data_from_google_api
from config import GoogleKey, GoogleDetailsUrl

URL = GoogleDetailsUrl


# Mocking of Google search API getting with results
def test_google_search_API_with_results(monkeypatch):
    details_payload = {
        "place_id": 'ChIJZR2qaYzVwkcRG74iJXu6kYc',
        "language": "fr",
        "key": GoogleKey
    }

    expected_results = \
        {'html_attributions': [],
         'result': {'address_components': [
             {'long_name': 'France', 'short_name': 'FR',
              'types': ['country', 'political']},
             {'long_name': 'Lille', 'short_name': 'Lille',
              'types': ['locality', 'political']},
             {'long_name': 'Nord', 'short_name': 'Nord',
              'types': ['administrative_area_level_2', 'political']},
             {'long_name': 'Hauts-de-France', 'short_name': 'Hauts-de-France',
              'types': ['administrative_area_level_1', 'political']},
             {'long_name': '59800', 'short_name': '59800',
              'types': ['postal_code']}],
             'adr_address': '<span class="postal-code">59800</span> '
                            '<span class="locality">Lille</span>, '
                            '<span class="country-name">France</span>',
             'formatted_address': '59800 Lille, France', 'geometry': {
                 'location': {'lat': 50.6327161, 'lng': 3.070834899999999},
                 'viewport': {'northeast': {'lat': 50.6340163802915,
                                            'lng': 3.072143280291502},
                              'southwest': {'lat': 50.63131841970851,
                                            'lng': 3.069445319708498}}},
             'icon': 'https://maps.gstatic.com/mapfiles/place_api'
                     '/icons/generic_business-71.png',
             'id': 'ff2f688529116b7313e83104b839815beefa2e68',
             'name': 'Mairie de Lille',
             'photos': [{'height': 4032,
                         'html_attributions': [
                             '<a '
                             'href="https'
                             '://maps'
                             '.google.com'
                             '/maps'
                             '/contrib'
                             '/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAAMHhMDmzFlUK5YopTvseRUdPB1Fx-svRy6kwq-lKvgKkKZFSEuJZDZHakd9-8yVEeSDEmmAktip5YeK-Qp7Wmuwt2MPFS5VxZA8t38SsidgkFff1uFlYTVmXLPbdZJqY0EhD67_jwzy-EzDUTuPuMUd5KGhSHd2HEqbV3JmGIk82kDTT3-7pFsQ',
                         'width': 3024},
                        {'height': 960,
                         'html_attributions': [
                             '<a '
                             'href="https'
                             '://maps'
                             '.google.com'
                             '/maps'
                             '/contrib'
                             '/103962656277132175291">Agent Smith</a>'],
                         'photo_reference': 'CmRaAAAA5OK0v_UwJvzm9obKSBRE4jXV3HubEDeKDE_0laZrY-w0qSW1AZCOO1b42w9jQPKR-_BATGQ3Lr2UXgcirMSYZrocrciLnnAv3r8hazvwLauMTjKd-fUM2zM4qabBZbtdEhCvWdzak_6ieIk1wi5NsFkjGhS-fXi3IVgzNHXgO4Murpqbq3DnUA',
                         'width': 694},
                        {'height': 4032,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAAuHXavHxDPhGTWear1VDNPYzzM59Wivxrv73yfu9PVlQSfN4qojGtmFA58GgZ5ba16CS_nlCpZtqCpCESDjIxmTLH0r4chSy7V3KAuDpDNOq6UW-RG7of-nGGCyl2waUxEhCQVk6_Cb3ChLqNAOsc7JFVGhTp_nIaZ_L4W2t5aP8OW1RXM_7WTQ',
                         'width': 3024},
                        {'height': 4032,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAA-7gUPwgPKB90_OwQO2GmKJWL8OZAGeRfOhUEwisWNIPMLoP7-Gpp2JaxKjLY4Ci2sV2thUwCdNGFZrECY_cBdolQbu-MuftoojrU1KeBReDwl74CVkCi3Iaaw2iUB3yUEhBTGDa2S0x7tjtXZIYlbcMWGhToH04ndp2g8nb0Qwtbf7_K3DqsFw',
                         'width': 3024},
                        {'height': 4032,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAAlOt3gs9PeSqVZryiLlr84DF40SDeGIbtgueUaCl4_tq8TdO6X6AiKqR3bb71wWa5hU8HU7TojatlmZCskAytmC6t1YVUo623VLP5kOMgyzbFTafAapBJMAvPKh2NWGvMEhCh3F7bVN3Ic1TkpvwL1ZQhGhSsTpBPBuoODhRyo5qpMD3zkh-Gkw',
                         'width': 3024},
                        {'height': 3264,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAAh7GmlWFwttJ9AyAzZjbIs8wfmeq4V7yLlZh5FKWl4XxQ30qP_JG_46qDV2MwUqS_aCkPv0vfoTxHEji0eHYFlb9F1BlF_pCppzT2LpZb23oBHAQPfGILFYEjtAHZJ-3iEhAkU9HIxKi4_ig-vbcjze41GhRDZx74RXFqKZNrd-X07bPmctbwhg',
                         'width': 2448},
                        {'height': 3701,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/110782744520313142229">Marta Kawecka</a>'],
                         'photo_reference': 'CmRaAAAAJ3fBOwa_xG0OMeUPhznxXKudq2l2jiVKZp8tndQI6dASesFEnC5q621EghQBoZHIk3lfGX7QKOOkhe9f8_q_Umwq63Q2HB0xTISHYYBQuZdfpWmcKxtnIjxw7oqDpj2SEhAp_OxopTOFckghk-jmaallGhSoc1-SlWtmqS27zlxCyqghXc285w',
                         'width': 2775},
                        {'height': 4032,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAASQc0AQAtJlsWbmKa2c_l22ytz-pNgf9SNADFNTasSvgo_e2J3c8I4SBrtwPP7ERI8aLi5ObMmpcwWRdTm_Yov8bcWci2Qypv07LgDRGulH2IoZcAf5aMj0hJ9H9ygpxMEhBZRXUemFfqkpFrKMPK22wwGhQewclVF0PMFtzzRrqMDyZjZ0QsNg',
                         'width': 3024},
                        {'height': 3000,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/108929525802327828540">César DESOYE</a>'],
                         'photo_reference': 'CmRaAAAAmNI9b8ImCCaQnO01kbYn85jK1x6ooj8s1CPxZNuOXI4xXv7nKYRX5cEInuN0dGpZDAxQUOYFdIUvRlHK1KtoAC1mI-70ntd0514-UjaG5g_6MrrSyaNwx_nI5AB7715xEhDLJLb3czmyiay9Wz9F94-8GhQTcZRZ-e-bmOEM5NOV9WAIZJUcew',
                         'width': 4000},
                        {'height': 4032,
                         'html_attributions': [
                             '<a href="https://maps.google.com/maps/contrib/100682700092805890513">Chris Lovely</a>'],
                         'photo_reference': 'CmRaAAAAHtNo28F0v609sEBnd5oz7bFSRO2sTZF3KdfqGCkA_ycRVCuy0czPleXe0KmeF4JHFzQlIvqxF1GN2PVVlSNUIqIxH9zlrJmjr1vDCnLw2n8mu8JOLyvTzmoPl4Eg69nhEhCpeC7mKmKt7rOpDKAAL-mlGhTX-CRDBDiyzvdRMyudHRcjrtlkmg',
                         'width': 3024}],
             'place_id': 'ChIJZR2qaYzVwkcRG74iJXu6kYc',
             'plus_code': {'compound_code': 'J3MC+38 Lille, France',
                           'global_code': '9F25J3MC+38'}, 'rating': 3.1,
             'reference': 'ChIJZR2qaYzVwkcRG74iJXu6kYc', 'reviews': [
                 {'author_name': 'Chris Lovely',
                  'author_url': 'https://www.google.com/maps/contrib'
                                '/100682700092805890513/reviews',
                  'language': 'fr',
                  'profile_photo_url': 'https://lh4.ggpht.com/-qWdRkAgeMq8'
                                       '/AAAAAAAAAAI/AAAAAAAAAAA/plhN5fiA4BY'
                                       '/s128-c0x00000000-cc-rp-mo-ba5/photo.jpg',
                  'rating': 3, 'relative_time_description': 'il y a 4\xa0mois',
                  'text': 'De belles décorations près  du marché de Noël '
                          '🙂\nMerci Madame le Maire restriction budgétaire '
                          ', pour les bus le parcours est très long, '
                          'avant ça allait très bien !',
                  'time': 1576850404}, {'author_name': 'Manon Loez',
                                        'author_url': 'https://www.google'
                                                      '.com/maps/contrib'
                                                      '/113566900549407958163/reviews',
                                        'language': 'fr',
                                        'profile_photo_url': 'https://lh5'
                                                             '.ggpht.com'
                                                             '/-vOs4ygVzi4o'
                                                             '/AAAAAAAAAAI'
                                                             '/AAAAAAAAAAA'
                                                             '/jnsyfHDe57k'
                                                             '/s128'
                                                             '-c0x00000000'
                                                             '-cc-rp-mo'
                                                             '/photo.jpg',
                                        'rating': 1,
                                        'relative_time_description': 'il y a '
                                                                     '5\xa0mois',
                                        'text': "Mauvais accueil "
                                                "téléphonique (du moins la "
                                                "conseillère que j'ai eu) je "
                                                "n'ai pas eu le temps de lui "
                                                "dire au revoir que la "
                                                "personne avait raccroché. "
                                                "C'est bien dommage pour une "
                                                "ville aussi accueillante.",
                                        'time': 1574411375},
                 {'author_name': 'Anais L.',
                  'author_url': 'https://www.google.com/maps/contrib'
                                '/104927688611368309556/reviews',
                  'language': 'fr',
                  'profile_photo_url': 'https://lh5.ggpht.com/-uJ_8z9AbnVA'
                                       '/AAAAAAAAAAI/AAAAAAAAAAA/zFm6w_om7Ro'
                                       '/s128-c0x00000000-cc-rp-mo/photo.jpg',
                  'rating': 1, 'relative_time_description': 'il y a 3\xa0mois',
                  'text': "Lille, ville ou des bâtiments poussent comme de "
                          "la mauvaise herbes mais où les stationnements "
                          "sont réduits voir néants !!! Ha si, tu dois te "
                          "taper 1km à pied pour rentrer chez toi !!! Je "
                          "paye ma taxe d'habitation et elle ne sert pas à "
                          "grand chose, à part à faire pousser des bureaux "
                          "vides ! De pire en pire, vivement le changement "
                          "de maire !!!",
                  'time': 1579003090}, {'author_name': 'Jason Oklm',
                                        'author_url': 'https://www.google'
                                                      '.com/maps/contrib'
                                                      '/108094516442109521274/reviews',
                                        'language': 'fr',
                                        'profile_photo_url': 'https://lh5'
                                                             '.ggpht.com/-SubctnrdFek/AAAAAAAAAAI/AAAAAAAAAAA/vHuwKhY5v2M/s128-c0x00000000-cc-rp-mo/photo.jpg',
                                        'rating': 5,
                                        'relative_time_description': 'il y a '
                                                                     'un '
                                                                     'mois',
                                        'text': 'Propre', 'time': 1583842382},
                 {'author_name': 'mathieu FAELENS IMMOBILIER LILLE',
                  'author_url': 'https://www.google.com/maps/contrib'
                                '/105445074127986329038/reviews',
                  'language': 'fr',
                  'profile_photo_url': 'https://lh4.ggpht.com/-Gw8cOJiyYGg'
                                       '/AAAAAAAAAAI/AAAAAAAAAAA/bFuNtEwmd4I'
                                       '/s128-c0x00000000-cc-rp-mo-ba3/photo'
                                       '.jpg',
                  'rating': 5,
                  'relative_time_description': 'il y a 10\xa0mois',
                  'text': 'C\'est toujours un plaisir d\'aller en Mairie de '
                          'Lille. C\'est un très beau monument et le '
                          'personnel municipal est dans l\'ensemble '
                          'accueillant et aimable. Je n\'ai jamais eu la '
                          'chance de rencontrer Mme Le Maire, elle était '
                          'surement comme à son accoutumé sur le "terrain" ; '
                          'et c\'est très bien.\nC\'est mon bureau de vote '
                          'et quand j\'y accède avec mes enfants pour les '
                          'élections, souvent le dimanche,  les vigiles à '
                          'l\'entrée, font leur travail rigoureusement et '
                          'avec le sourire. Au bureau de vote, tenu en parti '
                          'par des employées municipaux et des bénévoles, '
                          'la mission est assurée selon la loi, "enfin '
                          'j\'imagine que la loi dit ça ".\nPersonne n\'est '
                          'parfait et si je devais améliorer un  point ça '
                          'serait l\'accueil et les réponses qui sont '
                          'données au téléphone. Cependant, hormis durant '
                          'leurs vacances ou maladie, ce que tout le monde '
                          'comprend, on peut avoir quelqu\'un au bout du '
                          'fil. \nVive Lille ! Ville ceux qui l\'aiment et '
                          'ceux qui y habitent !!!!',
                  'time': 1560885298}], 'scope': 'GOOGLE',
             'types': ['subway_station', 'transit_station',
                       'point_of_interest', 'establishment'],
             'url': 'https://maps.google.com/?cid=9768794104810094107',
             'user_ratings_total': 55, 'utc_offset': 120,
             'vicinity': 'France'}, 'status': 'OK'}

    class MockGoogleApiResponse:
        def json(self):
            return expected_results

    def mock_requests_post(URL, params=details_payload):
        return MockGoogleApiResponse()

    monkeypatch.setattr('p7app.utils.google.requests.post', mock_requests_post)
    assert get_data_from_google_api(URL, details_payload) == expected_results
