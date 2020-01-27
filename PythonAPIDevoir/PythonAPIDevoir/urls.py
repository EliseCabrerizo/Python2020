from django.conf.urls import url
from django.contrib import admin
from backoffice.views import home
from backoffice.views import predict

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home),
    url('predict/', predict, name='to_predict')
]
