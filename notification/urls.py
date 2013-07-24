from django.conf.urls.defaults import *

from notification.views import Notices, mark_all_seen, single

urlpatterns = patterns('',
    url(r'^$', Notices.as_view(), name="notification_notices"),
    url(r'^(\d+)/$', single, name="notification_notice"),
    url(r'^mark_all_seen/$', mark_all_seen, name="notification_mark_all_seen"),
)
