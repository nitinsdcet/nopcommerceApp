import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilites


class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData//LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("************************Test_002_DDT_Login***********************")
        self.logger.info("***************************Verifying login test DDT**************************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = Login(self.driver)

        self.rows = XLUtilites.getRowCount(self.path, 'Sheet1')
        print("No. of rows in excel:", self.rows)
        lst_status = []  # empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtilites.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtilites.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtilites.readData(self.path, 'Sheet1', r, 3)
            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("***Passed***")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("***failed***")
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == "pass":
                    self.logger.info("***Failed***")
                    lst_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("***passed***")
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("******Login DDT test passed******")
            self.driver.close()
            assert True
        else:
            self.logger.info("******Login DDT test failed******")
            self.driver.close()
            assert False

        self.logger.info("***********End of login DDT test")
        self.logger.info("***********Completed Test_002_DDT_Login******")
