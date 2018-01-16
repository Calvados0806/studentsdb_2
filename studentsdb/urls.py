from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Students Urls
    url(r'^$', 'students.views.students.students_list', name='home'),
    url(r'^students/add/$', 'students.views.students.students_add', name='students_add'),
    url(r'^students/(?P<sid>\d+)/edit/$', 'students.views.students.students_edit', name='students_edit'),
    url(r'^students/(?P<sid>\d+)/delete/$', 'students.views.students.students_delete', name='students_delete'),
    # Groups Urls
    url(r'^groups/$', 'students.views.groups.groups_list', name='groups'),
    url(r'^groups/add/$', 'students.views.groups.groups_add', name="groups_add"),
    url(r'^groups/(?P<gid>\d+)/edit/$', 'students.views.groups.groups_edit', name="groups_edit"),
    url(r'^groups/(?P<gid>\d+)/delete/$', 'students.views.groups.groups_delete', name="groups_delete"),
    # Journal Urls
    url(r"^journal/$", "students.views.journal.journal_data", name="journal"),
    # Another Urls
    url(r'^admin/', include(admin.site.urls)),
]