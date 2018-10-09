from django.contrib import auth
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from sign.models import Event
from sign.models import Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

# def index(request):
#     return HttpResponse("hello world!!")
def index(request):
    return render(request,'index.html')

#登录方法
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
        #if username == 'admin' and password == 'admin123':
            #return render(request,'loginPage.html')
            auth.login(request,user)#登录
            #重定向url地址
            request.session['user'] = username
            response = HttpResponseRedirect('/loginPage/')
            #添加浏览器cookie
            #response.set_cookie('user',username,3600)
            #添加session

            return response

        # elif username != 'admin':
        #     return render(request,'index.html'),{'error':'username error!'}
        # elif password != 'admin123':
        #     return render(request,'index.html',{'error':'password error!'})
        else:
            return render(request,'index.html',{'error':'username or password error!'})
#登录界面，限制
# @login_required
# def loginPage(request):
#     # username = request.COOKIES.get('user','')
#     username = request.session.get('user', '')
#     return render(request,'loginPage.html',{'user':username})

#登录界面，限制
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'loginPage.html',{'user':username,'events':event_list})
#发布会名称搜索
@login_required
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains = search_name)
    return render(request,'loginPage.html',{'user':username,'events':event_list})


#嘉宾页面
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,3)
    #得到 当前要显示的第几页数据
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        #paginator.num_pages是获取总页数
        contacts = paginator.page(paginator.num_pages)
    return render(request,'guestMange.html',{'user':username,'guestName':contacts})

#嘉宾名字搜索
@login_required
def search_name_guest(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    #获取页面数据
    #模糊查询realname__contains
    guest_list = Guest.objects.filter(realname__contains = search_name)
    return render(request,'guestMange.html',{'user':username,'guestName':guest_list})

@login_required
def guestEvent(request,name):
    username = request.session.get('user', '')
    #event关联Event的发布会id
    guest_list = Guest.objects.filter(event=name)
    return render(request,'guestMange.html',{'user':username,'guestName':guest_list})
#退出系统
@login_required
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect('/index/')
    return response
@login_required
def sign_index(request,eid):
    event = get_object_or_404(Event,id=eid)
    return render(request,'sign_index.html',{'event':event})
@login_required
def sign_index_action(request,eid):
    event = get_object_or_404(Event,id=eid)
    phone = request.POST.get('phone','')
    print(phone)
    result = Guest.objects.filter(phone=phone)
    if not result:
        return render(request,'sign_index.html',{'event':event,'hint':'phone error!'})
    result = Guest.objects.filter(phone=phone,event_id=eid)
    if not result:
        return render(request,'sign_index.html',{'event':event,
                                                 'hint':'event id of phone error'})
    result = Guest.objects.get(phone=phone, event_id=eid)
    if result.sign:
        return render(request, 'sign_index.html', {'event': event,
                                                   'hint': 'user has sign in'})
    else:
        Guest.objects.filter(phone=phone,event_id=eid).update(sign='1')
        return render(request,'sign_index.html',{'event':event,
                                                 'hint':'sign in success!',
                                                 'guest':result})
@login_required
def add_guest(request,eid):
    event = get_object_or_404(Event,id=eid)
    return render(request,'add_guest.html',{'event':event})


