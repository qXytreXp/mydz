from django.urls import path
from . import views


app_name = 'main'
urlpatterns = [
    path('', views.ScheduleView.as_view(), name='schedule'),
    path('add-lesson-post/<int:lesson_id>', views.add_task, name='add_lesson_post'),
    path('delete-lesson/<int:lesson_id>', views.delete_lesson, name='delete_lesson'),
    path('add-lesson/<int:day_id>', views.AddLessonView.as_view(), name='add_lesson'),
]