from django.conf.urls import include, url
from django.contrib import admin
from office.views import ProtocolList, ProtocolDetail, AddProtocol

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ProtocolList.as_view(), name='protocol-list'),
    url(r'^protocol/(?P<slug>[\w\-_]+)/$', ProtocolDetail.as_view(), name='protocol-detail'),
    url(r'^add_protocol/?$', AddProtocol.as_view(), name='add-protocol'),
]
