from django.contrib import admin
from sign.models import Event,Guest
class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name','status','address','time']
    #搜索栏
    search_fields = ['name']
    list_filter = ['status']
class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname','phone','email','sign','createTime','event']
    search_fields = ['realname','phone']
    list_filter = ['sign']
# Register your models here.
admin.site.register(Event,EventAdmin)
admin.site.register(Guest,GuestAdmin)