import configparser
import os


def create_config(file_name):
    if not os.path.exists(file_name):
        config = configparser.ConfigParser()
        config['GOOGLE'] = {
            'how_many_pages': '10',
            'user_agent': 'desktop',
            'save_google_pages': 'True',
            'parser': 'html.parser'
        }
        config['GENERAL'] = {
            'search_external': 'True',
            'black_list_file': 'black_list.csv',
            'search_contact_data': 'True',
            'phone_number': 'True',
            'email': 'True',
            'address': 'False',
            'city': 'False',
            'postal_code': 'False',
            'nip': 'True',
            'regon': 'False',
            'krs': 'False',
        }
        with open(file_name, 'w') as cfg_file:
            config.write(cfg_file)
