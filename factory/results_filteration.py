from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class Resultfilter():
    def __init__(self, browser: WebDriver):
        self.browser = browser

    def apply_rating(self, star_rating: int = 0):
        rate_by_start_group = self.browser.find_element(By.CSS_SELECTOR, 'div[data-filters-group="class"]')
        get_star_children = rate_by_start_group.find_elements(By.CSS_SELECTOR, 'div[data-filters-item]')

        if len(get_star_children) > 0:
            for rating in get_star_children:
                if str(star_rating) in rating.get_attribute("data-filters-item"):
                    rating.click()



