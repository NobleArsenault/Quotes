from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^add_cite$', views.add_cite),
    url(r'^add_favorite/(?P<id>\d+)$', views.add_favorite),
    url(r'^remove_favorite/(?P<id>\d+)$', views.remove_favorite),
    url(r'^users/(?P<id>\d+)$', views.show_user)
    # url(r'^home/(?P<item_id>\d+)$', views.items),
    # url(r'^join/(?P<item_id>\d+)', views.join),
    # url(r'^remove/(?P<item_id>\d+)', views.remove),
]