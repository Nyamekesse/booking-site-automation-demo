import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from config import URL, driver_wait_in_seconds


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\selenium-chrome-drivers\chromedriver_win32", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(driver_wait_in_seconds)
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def start_page(self):
        self.get(URL)
        try:
            if self.find_element(By.ID, "onetrust-accept-btn-handler").is_displayed():
                accept_cookie = self.find_element(By.ID, "onetrust-accept-btn-handler")
                accept_cookie.click()
        except Exception as e:
            # self.quit()
            print(e)

    def select_currency(self, currency: str = None):
        try:
            currency_display_pane = self.find_element(By.CSS_SELECTOR,
                                                      'button[data-tooltip-text="Choose your currency"]')
            currency_display_pane.click() if currency_display_pane.is_displayed() else print('target node not found')
            if not currency:
                raise Exception
            else:
                selected_currency_type = WebDriverWait(self, driver_wait_in_seconds).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    f'a[data-modal-header-async-url-param="changed_currency=1&selected_currency={currency.upper()}"]')))
                selected_currency_type.click()
        except Exception as e:
            # self.quit()
            print(e)

    def search_destination(self, destination: str = None):
        if not destination:
            raise Exception
        else:
            try:
                search_field = self.find_element(By.ID, 'ss')
                if search_field.is_displayed():
                    search_field.clear()
                    search_field.send_keys(destination)
                    choose_first_option = WebDriverWait(self, driver_wait_in_seconds).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, 'li[data-i="0"]')))
                    choose_first_option.click()
            except Exception as e:
                # self.quit()
                print(e)

    def choose_date(self, check_in_date: str, check_out_date: str):
        if not check_in_date or not check_out_date:
            raise Exception
        else:
            try:
                start_date = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_in_date}"]')
                start_date.click()
                end_date = self.find_element(By.CSS_SELECTOR, f'td[data-date="{check_out_date}"]')
                end_date.click()
            except Exception as e:
                # self.quit()
                print(e)

    def specify_adults_number(self, number: int):
        continue_loop = True
        if not number:
            raise Exception
        else:
            try:
                target_element = WebDriverWait(self, driver_wait_in_seconds).until(
                    EC.presence_of_element_located((By.ID, "xp__guests__toggle")))
                if target_element.is_displayed():
                    target_element.click()
                    # first decrease the default count to 1 before setting the specified count
                    while continue_loop:
                        set_adults_num_to_one = self.find_element(By.CSS_SELECTOR,
                                                                  'button[aria-label="Decrease number of Adults"]')
                        set_adults_num_to_one.click()
                        # select the field holding the adult number
                        adult_element = self.find_element(By.ID, 'group_adults')
                        # get tje current adult number
                        current_adult_number = int(adult_element.get_attribute('value'))
                        if current_adult_number == 1:
                            continue_loop = False

                    set_preferred_adult_num = self.find_element(By.CSS_SELECTOR,
                                                                'button[aria-label="Increase number of Adults"]')
                    for _ in range(number - 1):
                        set_preferred_adult_num.click()

            except Exception as e:
                # self.quit()
                print(e)

    def __click_search(self):
        self.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def __set_children_age(self, age_lists: list, number: int) -> bool:
        """
        method sets the individual children ages
        :param age_lists:
        :param number:
        :return:
        """
        current_age_position = 0
        if len(age_lists) != number:
            raise Exception("Number of age list must be equal to number of children")
        else:
            # grab all tags with name="age"
            all_set_age_tags = self.find_elements(By.NAME, "age")
            # loop through individual available select age tag
            for single_tag_age in all_set_age_tags:
                current_age_tag = Select(single_tag_age)
                # loop through all the age options
                for ages in current_age_tag.options:
                    # avoiding the first option which is "Age needed"
                    if "Age needed" not in ages.text:
                        if int(ages.get_attribute('value')) == age_lists[current_age_position]:
                            ages.click()  # click and select the particular age if it is equal the one passed
                current_age_position += 1  # increase position by 1
            return True

    def specify_children_number(self, number: int, list_of_children_ages: list) -> bool:
        continue_loop = True
        if not number:
            raise Exception("Number should not be empty")
        else:
            try:
                # first decrease the default count to 0 before setting the specified count
                # select the field holding the children number
                children_element = self.find_element(By.ID, 'group_children')
                # get the current children number casted to integer
                current_children_number = int(children_element.get_attribute('value'))
                while continue_loop:
                    if current_children_number == 0:
                        continue_loop = False
                    else:
                        set_children_num_to_zero = self.find_element(By.CSS_SELECTOR,
                                                                     'button[aria-label="Decrease number of Children"]')
                        set_children_num_to_zero.click()

                set_preferred_children_num = self.find_element(By.CSS_SELECTOR,
                                                               'button[aria-label="Increase number of Children"]')
                for _ in range(number):
                    set_preferred_children_num.click()
                # call method to set individual ages for children
                set_ages = self.__set_children_age(number=number, age_lists=list_of_children_ages)
                # click the search button to search
                if set_ages:
                    return True

            except Exception as e:
                # self.quit()
                print(e)

    def specify_number_of_rooms(self, number: int) -> None:
        continue_loop = True
        if not number:
            raise Exception("Number should not be empty")
        else:
            try:
                # first decrease the default count to 1 before setting the specified count
                # select the field holding the room number
                room_element = WebDriverWait(self, driver_wait_in_seconds).until(
                    EC.presence_of_element_located((By.ID, "no_rooms")))
                # get the current children number casted to integer
                current_number_of_rooms = int(room_element.get_attribute('value'))
                while continue_loop:
                    if current_number_of_rooms == 1:
                        continue_loop = False
                    else:
                        set_number_of_rooms_to_one = self.find_element(By.CSS_SELECTOR,
                                                                       'button[aria-label="Decrease number of Rooms"]')
                        set_number_of_rooms_to_one.click()

                set_preferred_number_of_rooms = self.find_element(By.CSS_SELECTOR,
                                                                  'button[aria-label="Increase number of Rooms"]')
                for _ in range(number - 1):
                    set_preferred_number_of_rooms.click()
                # continue to search when done
                self.__click_search()
            except Exception as e:
                print(e)
