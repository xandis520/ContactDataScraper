import configparser
from datetime import datetime
from engine import *
import os


class Run:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')
        files = config['FILES']
        self.config_settings = configparser.ConfigParser()
        self.config_settings.read(files['settings_file_name'])

    def run(self, phrase):
        #######################################################################
        # LOAD SETTINGS
        #######################################################################
        # GOOGLE
        google = self.config_settings['GOOGLE']
        how_many_pages = int(google['how_many_pages'])
        user_agent = google['user_agent']
        save_google_pages = google['save_google_pages']
        parser = google['parser']

        # GENERAL
        general = self.config_settings['GENERAL']
        search_external = general['search_external']
        search_contact_data = general['search_contact_data']
        contact_data = {
            "phone": general['phone_number'],
            "email": general['email'],
            "address": general['address'],
            "city": general['city'],
            "postal_code": general['postal_code'],
            "nip": general['nip'],
            "regon": general['regon'],
        }
        contact_settings = {
            "black_list_file": general['black_list_file'],
            "contact_data": contact_data,
            "krs": general['krs']
        }
        #######################################################################
        # INITIAL MESSAGES
        #######################################################################
        print('[RUNNING PYTHON SCRAPPER VERSION alpha 0.0.1]')
        #######################################################################
        # EXECUTE
        #######################################################################
        # Make file directory if not exists
        if not os.path.exists('links'):
            os.makedirs('links')
        # File name
        now_date = datetime.now()
        file_directory = 'links/'
        file_date = now_date.strftime("%Y_%m_%d__%H%M%S_")
        file_phrase = phrase.replace(' ', '_')
        file_name_begin = file_directory + file_date + file_phrase + '_'

        #######################################################################
        # GOOGLE PAGES
        #######################################################################
        # INITIAL MESSAGE
        print('Scrapping', google['how_many_pages'], 'google pages')
        # GET PAGES
        pages = get_all_pages(phrase=phrase, parser=parser, user_agent=user_agent, how_many_pages=how_many_pages)

        # SAVE INTERNAL GOOGLE PAGES
        if save_google_pages == 'True':
            file_name = file_name_begin + 'google_pages.csv'
            save_google_pg(pages=pages['internal'], file_name=file_name)

        # SAVE EXTERNAL GOOGLE PAGES
        if search_external == 'True':
            file_name = file_name_begin + 'external_pages.csv'
            save_pages(pages=pages['external'], file_name=file_name)

        print('Finished scrapping google pages')
        #######################################################################
        # TRAVERSE PAGES
        #######################################################################
        if search_contact_data == 'True':
            print('Traversing pages to search contact data')
            traverse_pages(file_name=file_name, settings=contact_settings, parser=parser, user_agent=user_agent)
        # IN THE FUTURE
        #######################################################################
        # FINISH PROGRAM
        #######################################################################
        print('[PROGRAM FINISHED SCRAPPING SUCCESSFULLY]')
