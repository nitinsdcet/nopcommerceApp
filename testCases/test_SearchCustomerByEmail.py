import time
import pytest
# from Tools.scripts.patchcheck import status

from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_searchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()  #logger

    @pytest.mark.regression
    def test_serachCustomerByEmail(self, setup):
        self.logger.info("******SearchCustomerByEmail_004*************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*******Login Successful************")

        self.logger.info("**********Starting search Customer By Email ***************")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickonCustomersMenu()
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("****searching customer by emailID**********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert True == status
        self.logger.info("*******TC_SearchCustomerByEmail_004 Finished*********8")
        self.driver.close()
