# -*- coding: utf-8 -*-
from django.db import models

class Exam(models.Model):
	"""Exam Model"""
	class Meta(object):
		verbose_name = u"Екзамен"
		verbose_name_plural = u"Екзамени"

	title = models.CharField(
		max_length = 256,
		blank = False,
		verbose_name = u"Назва"
	)
	date = models.DateTimeField(
		verbose_name = u"Час проведення",
		blank = False
	)
	professor = models.CharField(
		blank = False,
		verbose_name = u"Викладач",
        max_length=256
	)

	def __str__(self):
		return u"%s (%s)" %(self.title, self.professor)
