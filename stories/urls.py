from django.conf.urls import url
from . import views

app_name = 'stories'


urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^$',views.stories_view,name='stories'),
]
