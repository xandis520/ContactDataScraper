from main import *
import config
import configparser
from distutils.util import strtobool
from run import Run

#######################################################################
# GLOBALS
#######################################################################
GLOBAL_STATE = 0  # 0 if window is normal size, 1 if window is maximized


class UIFunctions(MainWindow):
    def __init__(self):
        #######################################################################
        # GLOBALS
        #######################################################################
        GLOBAL_STATE = 0

    #######################################################################
    # INTERFACE DEFINITIONS (maximize, minimize, exit etc.)
    #######################################################################
    def ui_definitions(self):
        #######################################################################
        # TOP BUTTONS
        #######################################################################
        # Minimize button
        self.ui.button_minimalize.clicked.connect(lambda: self.showMinimized())
        # Maximize button
        self.ui.button_full_screen.clicked.connect(lambda: UIFunctions.maximize_restore(self))
        # Exit button
        self.ui.button_exit.clicked.connect(QCoreApplication.instance().quit)

        #######################################################################
        # BOTTOM BUTTONS
        #######################################################################
        # Resize window grip
        self.sizegrip = QSizeGrip(self.ui.frame_resize_window)

        #######################################################################
        # SHOW ==> DROP SHADOW
        #######################################################################
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(40)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))
        self.ui.frame_main_window.setGraphicsEffect(self.shadow)

    #######################################################################
    # MAXIMIZE/RESTORE
    #######################################################################
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            GLOBAL_STATE = 1
            self.showMaximized()
            self.ui.button_full_screen.setToolTip("Restore")

        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.button_full_screen.setToolTip("Maximize")

    def return_status(self):
        return GLOBAL_STATE

    def toogle_menu(self, max_width, enable):
        if enable:
            width = self.ui.frame_left_menu.width()
            max_extend = max_width
            standard = 70

            if width == 70:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(200)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.start()

    def shadow_effects(self):
        #######################################################################
        # HOME PAGE
        #######################################################################
        # SEARCH INPUT
        self.shadow1 = QGraphicsDropShadowEffect(self)
        self.shadow1.setBlurRadius(30)
        self.shadow1.setXOffset(0)
        self.shadow1.setYOffset(0)
        self.shadow1.setColor(QColor(0, 0, 0, 60))
        self.ui.text_search.setGraphicsEffect(self.shadow1)
        # RUN BUTTON
        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(30)
        self.shadow2.setXOffset(0)
        self.shadow2.setYOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 80))
        self.ui.button_run.setGraphicsEffect(self.shadow2)

    def config_initialize(self):
        file_name = 'config_settings.cfg'
        config.create_config(file_name)
        cfg = configparser.ConfigParser()
        cfg.read(file_name)

        #######################################################################
        # GOOGLE ENGINE
        #######################################################################
        google = cfg['GOOGLE']
        # How many pages
        self.ui.spin_box_google_pages.setValue(int(google['how_many_pages']))
        # User agent
        if google['user_agent'] == 'desktop':
            self.ui.radio_desktop.setChecked(True)
        else:
            self.ui.radio_mobile.setChecked(True)
        # Save google pages
        self.ui.check_google_pages.setChecked(strtobool(google['save_google_pages']))
        # Parser
        if google['parser'] == 'html.parser':
            self.ui.radio_html.setChecked(True)
        else:
            self.ui.radio_lxml.setChecked(True)

        #######################################################################
        # GENERAL SETTINGS
        #######################################################################
        general = cfg['GENERAL']
        # Search external pages?
        self.ui.check_external.setChecked(strtobool(general['search_external']))
        # Black list links file
        self.ui.label_black_list_file.setText(general['black_list_file'])
        # Search contact data?
        self.ui.check_contact_data.setChecked(strtobool(general['search_contact_data']))
        # Type of data
        self.ui.check_phone.setChecked(strtobool(general['phone_number']))
        self.ui.check_email.setChecked(strtobool(general['email']))
        # self.ui.check_address
        # self.ui.check_city
        # self.ui.check_postal
        self.ui.check_nip.setChecked(strtobool(general['nip']))
        self.ui.check_regon.setChecked(strtobool(general['regon']))
        self.ui.check_krs.setChecked(strtobool(general['krs']))

    def config_update(self, file_name):
        #######################################################################
        # USER_AGENT
        #######################################################################
        if self.ui.radio_desktop.isChecked():
            user_agent = 'desktop'
        else:
            user_agent = 'mobile'

        #######################################################################
        # PARSER
        #######################################################################
        if self.ui.radio_html.isChecked():
            parser = 'html.parser'
        else:
            parser = 'lxml'

        #######################################################################
        # CONFIG
        #######################################################################
        config = configparser.ConfigParser()
        config['GOOGLE'] = {
            'how_many_pages': self.ui.spin_box_google_pages.text(),
            'user_agent': user_agent,
            'save_google_pages': str(self.ui.check_google_pages.isChecked()),
            'parser': parser,
        }
        config['GENERAL'] = {
            'search_external': str(self.ui.check_external.isChecked()),
            'black_list_file': self.ui.label_black_list_file.text(),
            'search_contact_data': str(self.ui.check_contact_data.isChecked()),
            'phone_number': str(self.ui.check_phone.isChecked()),
            'email': str(self.ui.check_email.isChecked()),
            'address': 'False',
            'city': 'False',
            'postal_code': 'False',
            'nip': str(self.ui.check_nip.isChecked()),
            'regon': 'False',
            'krs': 'False',
        }
        # WRITE CONFIG TO FILE
        with open(file_name, 'w') as cfg_file:
            config.write(cfg_file)

    def config_new(self, file_name):
        print('new')

    def config_load(self, file_name):
        print('load')

    def engine_run(self):
        phrase = self.ui.text_search.toPlainText()
        self.ui.text_search.clear()
        if phrase != '':
            run = Run()
            run.run(phrase)
        else:
            print('You have to insert phrase first')
