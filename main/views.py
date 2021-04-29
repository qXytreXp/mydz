from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from django.views.generic import View
from .models import Day, Lesson


class ScheduleView(View):
    def get(self, request):
        days = Day.objects.all()

        return render(request, 'index.html', context={'days':days})


def add_task(request, lesson_id):
    if request.user.is_authenticated and request.user.is_editor:
        task = request.POST['task']

        lesson = Lesson.objects.get(id=lesson_id)
        if task and task.isspace() != True:
            lesson.task = task
        lesson.save()

        return redirect('/')
    return HttpResponseNotFound('Сторінку по такому шляху, не знайдено.')


def delete_lesson(request, lesson_id):
    if request.user.is_authenticated and request.user.is_editor:
        try: 
            lesson = Lesson.objects.get(id=lesson_id)
            lesson.delete()
        except Lesson.DoesNotExist:
            return redirect('/')
        return redirect('/')
    return HttpResponseNotFound('Сторінку по такому шляху, не знайдено.')
    

class AddLessonView(View):
    def get(self, request, day_id):
        if request.user.is_authenticated and request.user.is_editor:
            return render(request, 'add_lesson.html', context={'day_id': day_id})
        return HttpResponseNotFound('Сторінку по такому шляху, не знайдено.')

    def post(self, request, day_id):
        if request.user.is_authenticated and request.user.is_editor:
            errors = set()

            lesson_name = request.POST['name']
            task = request.POST['task']
            
            if lesson_name == '' or lesson_name.isspace():
                errors.add('Назву уроку не введено')

            if lesson_name and lesson_name.isspace() != True: 
                lesson = Lesson()
                lesson.lesson = lesson_name

                if task and task.isspace() != True:
                    lesson.task = task
                lesson.save()

                day = Day.objects.get(id=day_id)
                day.lessons.add(lesson)
                day.save()

                return redirect('/')
            return render(request, 'add_lesson.html', context={'errors': errors, 'day_id': day_id}) 
        return HttpResponseNotFound('Сторінку по такому шляху, не знайдено.')   


