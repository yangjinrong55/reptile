from django.http import JsonResponse
from sign.models import Event
from django.core.exceptions import ValidationError,ObjectDoesNotExist

#添加发布会的接口
def add_event(request):
    eid = request.POST.get('eid','')
    name = request.POST.get('name','')
    limit = request.POST.get('limit','')
    status = request.POST.get('status','')
    address = request.POST.get('address','')
    time = request.POST.get('time','')
    if id=='' or name=='' or limit=='' or status=='' or address=='' or time=='':
        return JsonResponse({'status':10021,'message':'parameter error!'})
    result = Event.objects.filter(id=eid)
    if result:
        return JsonResponse({'status':10022,'message':'event id already!'})
    result = Event.objects.filter(name=name)
    if result:
        return JsonResponse({'status':10023,'message':'event name already exists!'})
    if status == '':
        status = 1
    try:
        Event.objects.create(id=eid,name=name,limit=limit,status=int(status),address=address,time=time)
    except ValidationError as e:
        error = 'time format error:It must be in YYYY-MM-DD HH:MM:SS format.'
        return JsonResponse({'status':10024,'message':error})
    return JsonResponse({'status':200,'message':'add event success'})

def add_guest(request):
    pass


