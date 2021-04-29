from django.db import models


class Lesson(models.Model):
	lesson = models.CharField(max_length=50)
	task = models.TextField('Домашнє завдання', max_length=200, default='Нічого')


	def __str__(self):
		return f'{self.lesson}'


class Day(models.Model):
	day = models.CharField(max_length=50)
	lessons = models.ManyToManyField(Lesson, blank=True)

	def __str__(self):
		return f'{self.day}'
		