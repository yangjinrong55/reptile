from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User

# Create your tests here.
#测试Event,Guest表的数据插入
class ModelTest(TestCase):
    def setUp(self):
        Event.objects.create(id=1,name='发布会',limit=30,status=True,address='深圳',time='2018-09-12 14:34:23')
        Guest.objects.create(id=1,event_id=1,realname='小明',phone='103949',email='1289@qq.com',sign=True,createTime='2018-09-12 14:34:23')
    def test_event(self):
        #查找Event表的内容
        result = Event.objects.get(name='发布会')
        self.assertEqual(result.limit,30)
        self.assertTrue(result.status)
    def test_guest(self):
        result = Guest.objects.get(realname='小明')
        self.assertEqual(result.phone,'10349')
        self.assertTrue(result.sign)

#测试登录首页
class IndexPageTest(TestCase):
    def test_index_page(self):
        '''测试index视图'''
        response = self.client.get('/index/')
        self.assertEqual(response.status_code,200)
        #self.assertEqual(response.content,b'<!DOCTYPE html>\n<html lang="en">\n<hea[661 chars]tml>')
        self.assertTemplateUsed(response,'index.html')

#测试登录动作
class LoginActionTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','admin@qq.com','admin123456')
    def test_login_username(self):
        '''测试登录动作'''
        user = User.objects.get(username='admin')
        self.assertEqual(user.username,'admin')
        #密码验证为哈希值
        #self.assertEqual(user.password,'pbkdf2_sha256$120000$BQbZ1pvj9EfV$ejb5WEN1RgJSQsXrDV52HLJXCq8KbN+ivNNwPkkp37I')
    def test_login_no_password(self):
        '''用户名密码为空'''
        test_data = {'username':'','password':''}
        response = self.client.post('/login/',data=test_data)
        self.assertEqual(response.status_code,200)
        #断言内容在返回的内容中
        self.assertIn(b'username',response.content)
    def test_login_success(self):
        '''用户名密码为空'''
        test_data = {'username':'admin','password':'admin'}
        response = self.client.post('/loginPage/',data=test_data)
        self.assertEqual(response.status_code,302)

class UserEventTest(TestCase):
    def setUp(self):
        User.objects.create_user('admin','33@qq.com','admin12')
        Event.objects.create(id=1,name='xiaomi',limit=30,status=True,address='shenzhen',time='2018-09-12 14:34:23')
        self.login_user = {'username':'admin','password':'admin12'}
    def test_event(self):
        response = self.client.post('/login/',data=self.login_user)
        response = self.client.post('/loginPage/').content
        response = response.decode('utf-8')
        #self.assertEqual(response.status_code,200)
        self.assertIn('xiaomi',response)
        self.assertIn('shenzhen',response)
        self.assertIn('客户管理系统',response)
        self.assertIn('admin',response)
    def test_search(self):
        response = self.client.post('/login/',data=self.login_user)
        response = self.client.post('/search_name/',{'name':'xiaomi'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'xiaom', response.content)
        self.assertIn(b'shenzhen', response.content)

class SignTest(TestCase):
    def setUp(self):
        User.objects.create_user('user','user@qq.com','user123')
        Event.objects.create(id=1, name='我的发布会', limit=30, status=True, address='深圳', time='2018-09-12 14:34:23')
        Guest.objects.create(id=1, event_id=1, realname='小明', phone='103949', email='1289@qq.com', sign=True,
                             createTime='2018-09-12 14:34:23')
        self.login_user = {'username':'user','password':'user123'}
    #测试签到成功
    def test_sign_success(self):
        response1 = self.client.post('/login/',data=self.login_user)
        response = self.client.post('/sign_index_action/1/',{'phone':'103949'}).content
        response = response.decode('utf-8')
        self.assertEqual(response1.status_code,302)
        self.assertIn('user has sign in',response)

    # 测试手机号错误进行签到
    def test_sign_phone_error(self):
        response1 = self.client.post('/login/', data=self.login_user)
        response = self.client.post('/sign_index_action/1/', {'phone': '10394'}).content
        response = response.decode('utf-8')
        self.assertEqual(response1.status_code, 302)
        self.assertIn('phone error!', response)











