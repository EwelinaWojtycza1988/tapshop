from pypom import Region
from selenium.webdriver.common.action_chains import ActionChains


class BaseRegion(Region):

    def __init__(self, page, root=None):
        super().__init__(page, root)
        self.actions = ActionChains(page.driver)


