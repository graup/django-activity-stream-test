from django.conf.urls import url
from actstream import views
from .feeds import CustomUserJSONActivityFeed


urlpatterns = [
    url(r'^my/notifications/json/$',
        CustomUserJSONActivityFeed.as_view(name='unread_notifications'),
        name='notification_feed_json'),

    url(r'^actors/(?P<content_type_id>[^/]+)/(?P<object_id>[^/]+)/$',
        views.actor, name='actstream_actor'),
    url(r'^actors/(?P<content_type_id>[^/]+)/$',
        views.model, name='actstream_model'),
    url(r'^my/activity/detail/(?P<action_id>[^/]+)/$', views.detail,
        name='actstream_detail'),
]
