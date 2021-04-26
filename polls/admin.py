from django.contrib import admin
from .models import Question, Answer, Participant, Message


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pubdate', 'id')
    actions = ['pubdate']

    def pubdate(self, request, queryset):
        for el in queryset:
            if el == Question.objects.get(id=1):
                continue
            print(el)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'answer_pubdate', 'question',  'id')


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('username', 'avatar', 'birthday', 'self_description', 'phone_number')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Participant, ParticipantAdmin)
admin.site.register(Message)
