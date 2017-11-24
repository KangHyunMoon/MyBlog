from django.conf.urls import include, url

from core.views import Home,Hello_World, Bye_World, article_detail

urlpatterns = [
    url(r'^$', Home, name = 'MAIN'),
    url(r'^helloworld/$', Hello_World, name = 'core_Hello_World'),
    url(r'^byeworld/$', Bye_World, name = 'core_Bye_World'),
    url(r'^detail/(?P<pk>\d+)/$', article_detail, name='core_article_detail'),
]