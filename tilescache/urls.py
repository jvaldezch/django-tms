from django.conf.urls import patterns, include, url
from django.contrib import admin

from tc import views
from tc.tilecache_service import request_pat as tile_request_pat

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tilescache.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^tms%s' % tile_request_pat, views.get_tile),
    # url(r'^tc/', include('tc.urls')),
    # url(r'^wms/$', 'tc.views.wms', name='wms'),
    # url(r'^admin/', include(admin.site.urls)),
)
