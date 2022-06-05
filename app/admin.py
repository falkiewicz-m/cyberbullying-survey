from django.contrib import admin
from .models import QuestionPL, QuestionEN, ChoicePL, ChoiceEN, Current_answerPL, Current_answerEN

admin.site.register(QuestionPL)
admin.site.register(QuestionEN)
admin.site.register(ChoicePL)
admin.site.register(ChoiceEN)
admin.site.register(Current_answerPL)
admin.site.register(Current_answerEN)