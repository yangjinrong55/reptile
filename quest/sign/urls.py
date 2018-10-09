from django.conf.urls import url
from sign import views_if
#app_name = 'sign'
urlpatterns = [
    url(r'^add_event/',views_if.add_event,name='add_event')
]