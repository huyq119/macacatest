# coding:utf-8
import unittest
import os
import time
from macaca import WebDriver

desired_caps = {
    'platformName': 'android',
    #'app': 'F:\\02_PhoneTesting\\Macaca\\macaca-test-sample-master\\app\\android-app-bootstrap.zip',
    'app': 'E:\\chinau\\apponline\\Stamp830.apk', # apk 在自己PC电脑上的存放路径
    'reuse': 3
}

server_url = {
    'hostname': 'localhost',
    'port': 3456
}


class MacacaTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = WebDriver(desired_caps, server_url)
        cls.driver.init()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01_login(self):

        # 输入登录账号
        self.driver.element('id','cn.com.stamp:id/login_name').send_keys('13366040193')

         # 输入登录密码
        self.driver \
            .element_by_id('cn.com.stamp:id/login_prassword')\
            .send_keys('111111a')

        # 点击登录按钮
        self.driver \
            .element_by_id('cn.com.stamp:id/login_login') \
            .click()


if __name__ == '__main__':
    unittest.main()