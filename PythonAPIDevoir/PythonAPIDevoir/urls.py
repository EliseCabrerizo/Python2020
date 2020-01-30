from django.conf.urls import url
from django.contrib import admin
from backoffice import views
from django.urls import include

urlpatterns = [
    url('admin/', admin.site.urls),
    url('prediction/', include('backoffice.urls'))
]
