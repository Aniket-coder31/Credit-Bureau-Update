# models.py
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    answer_a = models.CharField(max_length=50)
    score_a = models.IntegerField()
    answer_b = models.CharField(max_length=50)
    score_b = models.IntegerField()
    answer_c = models.CharField(max_length=50)
    score_c = models.IntegerField()
    answer_d = models.CharField(max_length=50)
    score_d = models.IntegerField()

    def __str__(self):
        return self.text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=1)
    score = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.question.text} - {self.answer}'
