from django.db import models
from django.contrib.auth import get_user_model

class Tests(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название', null=False)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    content = models.CharField(max_length=299, verbose_name='Описание')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True,
                               default=None)


class Questions(models.Model):
    tests_id = models.ForeignKey('Tests', on_delete=models.PROTECT, verbose_name="Связанный тест")
    question = models.CharField(max_length=299, verbose_name='Вопрос', null=False)
    Image = models.ImageField(upload_to="photos/%Y/%m/%d/", null=True)

class Answers(models.Model):
    question_id = models.ForeignKey('Questions', on_delete=models.PROTECT, verbose_name="Связанный вопрос")
    answer = models.CharField(max_length=99, verbose_name='Ответ', null=False)
    flag = models.BooleanField()
