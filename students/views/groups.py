# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def groups_list(requests):
	groups = (
		{"id": 1,
		 "name": u"ПМІ-11",
		 "leader": u"Ячменєв Олег"},
		{"id": 2,
		 "name": u"ПМІ-12",
		 "leader": u"Шинкаренко Анастасія"},
		{"id": 3,
		 "name": u"ПМІ-13",
		 "leader": u"Левкович Роман"}
	)
	return render(requests, "students/groups_list.html", {"groups": groups})

def groups_add(request):
	return HttpResponse('<h1>Group Add Form</h1>')

def groups_edit(request, gid):
	return HttpResponse('<h1>Edit Group %s</h1>' % gid)

def groups_delete(request, gid):
	return HttpResponse('<h1>Delete Group %s</h1>' % gid)