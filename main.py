from factory.booking import Booking
from factory.user_data import *

with Booking(terminate=False) as browser:
    browser.start_page(URL)
    browser.select_currency(CURRENCY)
    browser.search_destination(DESTINATION)
    browser.choose_date(check_in_date=CHECK_IN_DATE, check_out_date=CHECK_OUT_DATE)
    browser.specify_number_of_adults(NUMBER_OF_ADULTS)
    # call the next method if there is a return statement of True
    if browser.specify_number_of_children(NUMBER_OF_CHILDREN, AGES_OF_CHILDREN):
        browser.specify_number_of_rooms(NUMBER_OF_ROOMS)
        browser.filter_result(STAR_RATING)
        browser.results()
