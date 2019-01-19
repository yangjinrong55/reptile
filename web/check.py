#coding:utf-8
from element import *

def l_check_packages1():
    table_num = l_get_table_num()
    package1_name = l_get_package1_name()
    method = l_get_spend_metod()
    success_payment_status = l_get_success_payment_status()
    assert_time = l_get_settlement_time()
    success_order_status_time = l_get_success_order_status_time()
    print (table_num,package1_name,method,success_payment_status,success_order_status_time,assert_time)
    if table_num == u'A4' and package1_name == u'超满足全榴梿套餐' and method == u'POS机' \
            and success_payment_status == u'已支付' and success_order_status_time == assert_time:
        return True
    else:
        return False
def l_check_packages2():
    table_num = l_get_table_num()
    package1_name = l_get_package1_name()
    method = l_get_spend_metod()
    success_payment_status = l_get_success_payment_status()
    assert_time = l_get_settlement_time()
    success_order_status_time = l_get_success_order_status_time()
    print (table_num,package1_name,method,success_payment_status,success_order_status_time,assert_time)
    if table_num == u'A4' and package1_name == u'四人随心嗨套餐' and method == u'现金' \
            and success_payment_status == u'已支付' and success_order_status_time == assert_time:
        return True

    else:
        return False
def l_check_packages3():
    table_num = l_get_table_num()
    package1_name = l_get_package1_name()
    method = l_get_spend_metod()
    success_payment_status = l_get_success_payment_status()
    assert_time = l_get_settlement_time()
    success_order_status_time = l_get_success_order_status_time()
    print (table_num,package1_name,method,success_payment_status,success_order_status_time,assert_time)
    if table_num == u'A4' and package1_name == u'超满足套餐' and method == u'团购券' \
            and success_payment_status == u'已支付' and success_order_status_time == assert_time:
        return True

    else:
        return False
def l_check_packages4():
    table_num = l_get_table_num()
    package1_name = l_get_package1_name()
    method = l_get_spend_metod()
    success_payment_status = l_get_success_payment_status()
    assert_time = l_get_settlement_time()
    success_order_status_time = l_get_success_order_status_time()
    print (table_num,package1_name,method,success_payment_status,success_order_status_time,assert_time)
    if table_num == u'A4' and package1_name == u'超值双拼套餐' and method == u'招行券' \
            and success_payment_status == u'已支付' and success_order_status_time == assert_time:
        return True

    else:
        return False

def l_check_packages5():
    table_num = l_get_table_num()
    package1_name = l_get_package1_name()
    method = l_get_spend_metod()
    success_payment_status = l_get_success_payment_status()
    assert_time = l_get_settlement_time()
    success_order_status_time = l_get_success_order_status_time()
    print(table_num,package1_name,method,success_payment_status,success_order_status_time,assert_time)
    if table_num == u'A4' and package1_name == u'一人食升级套餐' and method == u'月结客户' \
            and success_payment_status == u'已支付' and success_order_status_time == assert_time:
        return True

    else:
        return False

def l_check_packages6():
    table_num = l_get_table_num()
    package1_name = l_get_package1_name()
    method = l_get_spend_metod()
    success_payment_status = l_get_success_payment_status()
    assert_time = l_get_settlement_time()
    success_order_status_time = l_get_success_order_status_time()
    print(table_num,package1_name,method,success_payment_status,success_order_status_time,assert_time)
    if table_num == u'A4' and package1_name == u'会员全榴梿优惠套餐' and method == u'提货卡' \
            and success_payment_status == u'已支付' and success_order_status_time == assert_time:
        return True

    else:
        return False