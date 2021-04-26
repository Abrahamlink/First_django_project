from django.db import models
from phonenumber_field.phonenumber import PhoneNumber
from django.contrib.auth.models import User
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pubdate = models.DateTimeField('Date publication', auto_now=True)
    user_id = models.ForeignKey('Participant', on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    answer_text = models.CharField(max_length=500)
    answer_pubdate = models.DateTimeField('Answer publication', auto_now=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey('Participant', on_delete=models.CASCADE)

    def __str__(self):
        return self.answer_text


class Participant(User):
    avatar = models.ImageField(null=True, blank=True)
    birthday = models.DateTimeField(default=timezone.now)
    self_description = models.TextField(max_length=1000, blank=True)
    phone_number = models.CharField(max_length=10, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='user_sender')
    host = models.ForeignKey(Participant, on_delete=models.CASCADE, related_name='host_user')
    message = models.TextField(max_length=500)
