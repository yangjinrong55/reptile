#coding:utf-8
from selenium import webdriver
import time
from data import *
driver = webdriver.Chrome()
'''测试环境'''
driver.get('')
# '''正式环境'''
# driver.get('')
def l_maximize_window():
    driver.maximize_window()
def l_input_username(username):
    driver.find_element_by_id('j_username').send_keys(username)
def l_input_password(password):
    driver.find_element_by_id('j_password').send_keys(password)
def l_click():
    driver.find_element_by_xpath('//*[@id="login-btn"]').click()
    time.sleep(1)
def l_login_out():#登录后退出
    driver.find_element_by_xpath('//*[@id="indexHeadMenu"]/span[1]').click()
    time.sleep(2)
    driver.find_element_by_css_selector('i[class="icon-signout"]').click()

def l_click_manage():#点击门店管理
    #driver.find_element_by_xpath('//*[@id="Main_div"]/div[1]/div[1]/div[1]/ul/li[2]/a/h1/em/span').click()
    #driver.find_element_by_xpath('//*[@id="Main_div"]/div[1]/div[1]/div[1]/ul/li[1]/a/h1/em').click()
    driver.find_element_by_css_selector('em[data-name="门店管理"]').click()
    time.sleep(2)
def l_click_money_meum():
    driver.find_element_by_link_text(u'收银菜单').click()
    time.sleep(2)

def l_foce_on_window():#收银窗口
    curHandle = driver.current_window_handle #获取当前窗口聚丙
    allHandle = driver.window_handles #获取所有聚丙
    """循环判断，只要不是当前窗口聚丙，那么一定就是新弹出来的窗口，这个很好理解。"""
    for h in allHandle:
        if h != curHandle:
            driver.switch_to.window(h) #切换聚丙，到新弹出的窗口
            break
def l_foce_on_window1():#详情第一个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[2]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window2():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[3]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window3():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[4]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window4():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[5]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window5():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[6]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window6():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[7]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window7():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[8]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window8():#详情第二个窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[9]
    driver.switch_to.window(h)#切换聚丙，到新弹出的窗口
def l_foce_on_window():#收银窗口
    allHandle = driver.window_handles #获取所有聚丙
    h = allHandle[1]
    #print h
    driver.switch_to.window(h) #切换聚丙，到新弹出的窗口
def l_check_money_system_title():#//*[@id="pos"]/section/header/span[2]
    title = driver.find_element_by_xpath('//*[@id="pos"]/section/header/span[2]').text
    return title

def l_click_quanliulian():#全榴莲套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[1]/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div/div').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]').click()
    for i in range(0,2):
        driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div/div').click()
    #driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/div[1]/div/div').click()
def l_click_package_true():#点击确定
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[2]/div[2]').click()
def l_submit_order():#提交订单
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/aside/div[1]/div[2]/div[2]').click()
    time.sleep(3)
def l_click_dine():#堂食选择人数
    driver.find_element_by_css_selector('span[class="el-input-number__increase"]').click()
def l_input_table_number():#输入桌号
    driver.find_element_by_xpath('//*[@id="pos"]/div[7]/div/div[2]/div/div/div[2]/div/div/div[1]').click()#A
    driver.find_element_by_xpath('//*[@id="pos"]/div[7]/div/div[2]/div/div/div[2]/div/div/div[8]').click()#4
def l_direct_settlement():#直接结算
    driver.find_element_by_css_selector('button[class="el-button el-button--warning"]').click()
    time.sleep(2)
def l_cash_payment(money):#现金支付
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[1]/td[2]/input').send_keys(money)
def l_pos_spend():#pos机
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[2]/td[2]/input').click()
def l_group_purchase_coupon(money):#团购券支付
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[3]/td[2]/input').send_keys(money)
def l_zhaohangquan_span(money):#招行券支付
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[4]/td[2]/input').send_keys(money)
def l_monthly_customer_span(money):#月结客户
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[5]/td[2]/input').send_keys(money)
def l_tihuoka_span(money):#提货卡支付
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[6]/td[2]/input').send_keys(money)
def l_xianjinquan_wuma_span(money):#现金券-无券码结算
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[7]/td[2]/input').send_keys(money)
def l_xianjinquan_youma_span():#现金券-有券码结算
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[8]/td[2]/input').send_keys()
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[8]/td[2]/button').click()
def l_meituanquan_span():#美团券支付
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[11]/td[2]/input').send_keys()
    driver.find_element_by_xpath('//*[@id="leftTable"]/tr[11]/td[2]/button').click()
def l_order_settlement():#订单结算
    driver.find_element_by_css_selector('button[onclick^="confirmAccount"]').click()
def l_order_detail():#订单详情
    time.sleep(1)
    driver.find_element_by_partial_link_text(u'下单成功').click()
    time.sleep(2)

def l_get_success_login_shopname():#获取店名
    shop_name = driver.find_element_by_xpath('//*[@id="indexHeadMenu"]/span[1]').text
    return shop_name
def l_get_success_login_name():#获取登录名字
    login_name = driver.find_element_by_xpath('//*[@id="indexHeadMenu"]/span[2]').text
    return login_name
def l_get_error_msg():#获取错误信息
    error_msg =driver.find_element_by_xpath('//*[@id="message_box_info"]/div/span').text
    return error_msg

def l_get_table_num():#获取桌号
    table_num = driver.find_element_by_xpath('//*[@id="SosOrder-table"]/tr[1]/td[6]/span').text
    return table_num
def l_get_package1_name():#获取套餐名
    package1_name = driver.find_element_by_xpath('//*[@id="dataList"]/tr[1]/td[2]').text
    return package1_name
def l_get_spend_metod():#获取支付方式
    method = driver.find_element_by_css_selector('span[class="tableNum showPayWay"]').text
    return method
def l_get_success_payment_status():#获取支付成功状态
    success_payment_status = driver.find_element_by_css_selector('span[class="tableNum payState"]').text
    return success_payment_status
def l_get_success_order_status_time():#获取订单状态,时间
    success_order_status_time = driver.find_element_by_css_selector('td[class="orderState"]').text
    return success_order_status_time
def l_get_settlement_time():#获取结算时间
    settlement_time = driver.find_element_by_xpath('//*[@id="SosOrder-table"]/tr[3]/td[4]').text
    assert_time = u'已完成'+ ' '+ settlement_time
    return assert_time
def l_get_pay_money():#获取应付金额
    pay_money = driver.find_element_by_xpath('//*[@id="count-all"]/div[2]/div[1]/span[2]').text
    return pay_money

def l_click_sirensuixinhai():#点击四人随心嗨套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[2]/div/div[1]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[1]/div/div').click()#点击披萨双拼
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div/div').click()#点击披萨双拼
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div/div/div').click()#点击9寸披萨
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]').click()#点击小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[4]').click()#点击小吃
    for i in range(0,2):
        driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/div[1]/div/div').click()#点击饮品
        driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[4]/div[2]/div[2]/div/div').click()
def l_click_chaomanzutaocan():#点击超满足套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[3]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[6]/div/div').click()#双拼
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[9]/div/div').click()#双拼
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]').click()#小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div/div').click()#饮料
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]/div/div').click()#饮料
def l_click_chaozhisuanpingtaocan():#点击超值双拼套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[4]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[3]/div/div').click()#双拼
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[6]/div/div').click()#双拼
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[1]').click()#小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[1]/div/div').click()#饮料
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[2]/div/div').click()#饮料
def l_click_yirenshishenjitaocan():#点击一人食升级套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[5]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div[2]/div/div').click()#披萨
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[8]/div/div').click()#饮料
def l_click_huiyuanquanliulian():#点击会员全榴梿优惠套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[6]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]').click()#小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[4]/div/div').click()#饮料
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[5]/div/div').click()#饮料
def l_click_huiyuanyouhuitaocan():#点击会员优惠套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[7]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]').click()#小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[5]').click()#小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[4]/div/div').click()#饮料
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[5]/div/div').click()#饮料
def l_click_yiwaihaochitaocan():#点击意外好吃套餐
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div/div[2]/div[1]/div/div[8]').click()
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[2]/div[2]/div[2]').click()#小吃
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[4]/div/div').click()#饮料
    driver.find_element_by_xpath('//*[@id="pos"]/section/section/section/main/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div[6]/div/div').click()#饮料




