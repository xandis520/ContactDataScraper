from main import *
import config


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
        self.shadow2.setColor(QColor(0, 0, 0, 60))
        self.ui.button_run.setGraphicsEffect(self.shadow2)

    def config_handle(self):
        config.create_config('config_settings.cfg')
        self.ui.spin_box_google_pages.setValue(14)
        # GOOGLE ENGINE
        # How many pages
        # self.ui.spin_box_google_pages
        # # User agent
        # self.ui.radio_desktop
        # self.ui.radio_mobile
        # # Save google pages
        # self.ui.check_google_pages
        # # Parser
        # self.ui.radio_html
        # self.ui.radio_lxml
        #
        # # GENERAL SETTINGS
        # # Search external pages?
        # self.ui.check_external
        # # Save google pages?
        # self.ui.check_save_google_pages
        # # Black list links file
        # self.ui.label_black_list_file
        # self.ui.button_black_list_load
        # self.ui.button_black_list_open
        # # Search contact data?
        # self.ui.check_contact_data
        # # Type of data
        # self.ui.check_phone
        # self.ui.check_email
        # # self.ui.check_address
        # # self.ui.check_city
        # # self.ui.check_postal
        # self.ui.check_nip
        # self.ui.check_regon