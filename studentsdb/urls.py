from django.conf.urls import include, url, patterns
from django.contrib import admin
from .settings import MEDIA_ROOT, DEBUG

from students.views.students import StudentUpdateView

urlpatterns = [
#----------Students Urls----------
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<pk>\d+)/edit/$', StudentUpdateView.as_view(), name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),
#----------Groups Urls----------
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add', name="groups_add"),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name="groups_edit"),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name="groups_delete"),
#----------Journal Urls----------
    url(r"^journal/$", "students.views.journal.journal_data", name="journal"),
#----------Another Urls----------
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact-admin/$', 'students.views.contact_admin.contact_admin', name='contact_admin')
]
if DEBUG:
    # serve files from media folder
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
    'document_root': MEDIA_ROOT}))
