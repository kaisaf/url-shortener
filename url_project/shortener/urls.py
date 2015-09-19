from django.conf.urls import include, url

urlpatterns = [
#    url(r'^admin/', include(admin.site.urls)),
    url(r'^shortener/(?P<path>\w+)', 'shortener.views.shortener'),
    url(r'^(?P<path>\w+)', 'shortener.views.shortener_redirect'),
    url(r'^', 'shortener.views.index'),
]
