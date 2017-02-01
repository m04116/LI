from django.conf.urls import url
from .views import authorization_page, message_page, add_comment, edit_comment, del_comment


urlpatterns = [
    url(r'^$', authorization_page, name = 'authorization_page'),
    url(r'^message/', message_page, name='message_page'),
    url(r'^add_comment/(?P<pk>[0-9]+)/$', add_comment, name = 'add_comment'),
    url(r'^edit_comment/(?P<pk>[0-9]+)/$', edit_comment, name = 'edit_comment'),
    url(r'^del_comment/(?P<pk>[0-9]+)/$', del_comment, name = 'del_comment'),
]
