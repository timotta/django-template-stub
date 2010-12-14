from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^projetodjango/', include('projetodjango.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^', include('templatestub.urls')),
    #url(r'^templatestub/$', 'templatestub.views.templatestub'),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
