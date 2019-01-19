#coding:utf-8
from unittest import TestCase
from web.element import *
from web.data import *
class login(TestCase):
    @classmethod
    def setUpClass(self):
        self.n = 1
        l_maximize_window()
    @classmethod
    def setUp(self):
        self.n = self.n +1
        try:
            driver.get("http://139.199.0.169:9091/RedseaPlatform/index.jsp")
        except Exception as a:
            print(a)
    def test_login_success(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual((read_data('login',self.n,4),read_data('login',self.n,5)),(l_get_success_login_shopname(),
                                                                                    l_get_success_login_name()))
        l_login_out()
    def test_login_error_password(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual(read_data('login',self.n,4),l_get_error_msg())
        #print(l_get_error_msg())
    def test_login_error_username(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual(read_data('login',self.n,4),l_get_error_msg())
        #print(l_get_error_msg())
    def test_all_empty(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual(read_data('login',self.n,4),l_get_error_msg())
        #print(l_get_error_msg())
    def test_empty_username(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual(read_data('login',self.n,4),l_get_error_msg())
        #print(l_get_error_msg())
    def test_empty_password(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual(read_data('login',self.n,4),l_get_error_msg())
        #print(l_get_error_msg())
    def test_special_character(self):
        l_input_username(read_data('login',self.n,2))
        l_input_password(read_data('login',self.n,3))
        l_click()
        self.assertEqual(read_data('login',self.n,4),l_get_error_msg())
        #print(l_get_error_msg())


class order(TestCase):
    @classmethod
    def setUpClass(self):
        driver.get("http://139.199.0.169:9091/RedseaPlatform/index.jsp")
        l_maximize_window()
        l_input_username('xiaohuiyang')
        l_input_password('123')
        l_click()
        l_click_manage()
        l_click_money_meum()
        self.n = 1
    @classmethod
    def setUp(self):
        try:
            l_foce_on_window()
            driver.refresh()
            time.sleep(3)
            self.n = self.n+1
        except Exception as a:
            print(a)
    def test_packages1(self):
        l_maximize_window()
        l_click_quanliulian()
        l_click_package_true()#选择套餐里面的商品后点击确定
        l_submit_order()#提交订单
        l_click_dine()#选择人数
        l_input_table_number()
        l_direct_settlement()#点击直接结算
        l_cash_payment(read_data('pay_case',self.n,6))
        l_order_settlement()#点击结算
        l_order_detail()#点击订单详情
        l_foce_on_window1()
        self.assertEqual((read_data('pay_case',self.n,2),read_data('pay_case',self.n,3),
                          read_data('pay_case',self.n,4),read_data('pay_case',self.n,5),l_get_settlement_time(),str(read_data('pay_case',self.n,6))),
                         (l_get_table_num(),l_get_package1_name(),l_get_spend_metod(),
                          l_get_success_payment_status(),l_get_success_order_status_time(),l_get_pay_money()))
    def test_packages2(self):
        l_click_sirensuixinhai()
        l_click_package_true()
        l_submit_order()
        l_click_dine()
        l_input_table_number()
        l_direct_settlement()
        l_pos_spend()
        l_order_settlement()
        l_order_detail()
        l_foce_on_window2()
        self.assertEqual((read_data('pay_case',self.n,2),read_data('pay_case',self.n,3),
                          read_data('pay_case',self.n,4),read_data('pay_case',self.n,5),l_get_settlement_time(),str(read_data('pay_case',self.n,6))),
                         (l_get_table_num(),l_get_package1_name(),l_get_spend_metod(),
                          l_get_success_payment_status(),l_get_success_order_status_time(),l_get_pay_money()))
    def test_packages3(self):
        l_click_chaomanzutaocan()
        l_click_package_true()
        l_submit_order()
        l_click_dine()
        l_input_table_number()
        l_direct_settlement()
        l_group_purchase_coupon(read_data('pay_case',self.n,6))
        l_order_settlement()
        l_order_detail()
        l_foce_on_window3()
        self.assertEqual((read_data('pay_case',self.n,2),read_data('pay_case',self.n,3),
                          read_data('pay_case',self.n,4),read_data('pay_case',self.n,5),l_get_settlement_time(),str(read_data('pay_case',self.n,6))),
                         (l_get_table_num(),l_get_package1_name(),l_get_spend_metod(),
                          l_get_success_payment_status(),l_get_success_order_status_time(),l_get_pay_money()))
    def test_packages4(self):
        l_click_chaozhisuanpingtaocan()
        l_click_package_true()
        l_submit_order()
        l_click_dine()
        l_input_table_number()
        l_direct_settlement()
        l_zhaohangquan_span(read_data('pay_case',self.n,6))
        l_order_settlement()
        l_order_detail()
        l_foce_on_window4()
        self.assertEqual((read_data('pay_case',self.n,2),read_data('pay_case',self.n,3),
                          read_data('pay_case',self.n,4),read_data('pay_case',self.n,5),l_get_settlement_time(),str(read_data('pay_case',self.n,6))),
                         (l_get_table_num(),l_get_package1_name(),l_get_spend_metod(),
                          l_get_success_payment_status(),l_get_success_order_status_time(),l_get_pay_money()))
    def test_packages5(self):
        l_click_yirenshishenjitaocan()
        l_click_package_true()
        l_submit_order()
        l_click_dine()
        l_input_table_number()
        l_direct_settlement()
        l_monthly_customer_span(read_data('pay_case',self.n,6))
        l_order_settlement()
        l_order_detail()
        l_foce_on_window5()
        self.assertEqual((read_data('pay_case',self.n,2),read_data('pay_case',self.n,3),
                          read_data('pay_case',self.n,4),read_data('pay_case',self.n,5),l_get_settlement_time(),str(read_data('pay_case',self.n,6))),
                         (l_get_table_num(),l_get_package1_name(),l_get_spend_metod(),
                          l_get_success_payment_status(),l_get_success_order_status_time(),l_get_pay_money()))

    def test_packages6(self):
        l_click_huiyuanquanliulian()
        l_click_package_true()
        l_submit_order()
        l_click_dine()
        l_input_table_number()
        l_direct_settlement()
        l_tihuoka_span(read_data('pay_case',self.n,6))
        l_order_settlement()
        l_order_detail()
        l_foce_on_window6()
        self.assertEqual((read_data('pay_case',self.n,2),read_data('pay_case',self.n,3),
                          read_data('pay_case',self.n,4),read_data('pay_case',self.n,5),l_get_settlement_time(),str(read_data('pay_case',self.n,6))),
                         (l_get_table_num(),l_get_package1_name(),l_get_spend_metod(),
                          l_get_success_payment_status(),l_get_success_order_status_time(),l_get_pay_money()))






