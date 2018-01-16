# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def journal_data(request):
	data = (str(i) for i in range(1, 31))
	students = (
		{"id": 1,
		 "first_name": u"Віталій",
		 "last_name": u"Подоба"},
		{"id": 2,
		 "first_name": u"Андрій",
		 "last_name": u"Корост"},
		{"id": 3,
		 "first_name": u"Тарас",
		 "last_name": u"Притула"}
	)
	return render(request, "students/journal.html", {"students": students, "data": data})