from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.views import static

urlpatterns = [
    url(r'^', include('reno_app.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^static/(?P<path>.*)',
	static.serve,
	{'document_root': settings.STATIC_ROOT}),
]
