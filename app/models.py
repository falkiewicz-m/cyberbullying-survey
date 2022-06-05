from django.db import models

class QuestionPL(models.Model):
    question_text = models.CharField(max_length=200)

class ChoicePL(models.Model):
    question_fk = models.ForeignKey(QuestionPL, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    numberOfVotes = models.IntegerField(default=0)

class Current_answerPL(models.Model):
    a1 = models.IntegerField(blank=True, null=True)
    a2 = models.IntegerField(blank=True, null=True)
    a3 = models.IntegerField(blank=True, null=True)
    a4 = models.IntegerField(blank=True, null=True)
    a5 = models.IntegerField(blank=True, null=True)
    a6 = models.IntegerField(blank=True, null=True)
    a7 = models.IntegerField(blank=True, null=True)
    a8 = models.IntegerField(blank=True, null=True)
    a9 = models.IntegerField(blank=True, null=True)
    a10 = models.IntegerField(blank=True, null=True)
    a11 = models.IntegerField(blank=True, null=True)
    a12 = models.IntegerField(blank=True, null=True)
    a13 = models.IntegerField(blank=True, null=True)
    a14 = models.IntegerField(blank=True, null=True)
    a15 = models.IntegerField(blank=True, null=True)
    a16 = models.IntegerField(blank=True, null=True)
    a17 = models.IntegerField(blank=True, null=True)
    a18 = models.IntegerField(blank=True, null=True)
    a19 = models.IntegerField(blank=True, null=True)
    a20 = models.IntegerField(blank=True, null=True)

class QuestionEN(models.Model):
    question_text = models.CharField(max_length=200)

class ChoiceEN(models.Model):
    question_fk = models.ForeignKey(QuestionEN, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    numberOfVotes = models.IntegerField(default=0)

class Current_answerEN(models.Model):
    a1 = models.IntegerField(blank=True, null=True)
    a2 = models.IntegerField(blank=True, null=True)
    a3 = models.IntegerField(blank=True, null=True)
    a4 = models.IntegerField(blank=True, null=True)
    a5 = models.IntegerField(blank=True, null=True)
    a6 = models.IntegerField(blank=True, null=True)
    a7 = models.IntegerField(blank=True, null=True)
    a8 = models.IntegerField(blank=True, null=True)
    a9 = models.IntegerField(blank=True, null=True)
    a10 = models.IntegerField(blank=True, null=True)
    a11 = models.IntegerField(blank=True, null=True)
    a12 = models.IntegerField(blank=True, null=True)
    a13 = models.IntegerField(blank=True, null=True)
    a14 = models.IntegerField(blank=True, null=True)
    a15 = models.IntegerField(blank=True, null=True)
    a16 = models.IntegerField(blank=True, null=True)
    a17 = models.IntegerField(blank=True, null=True)
    a18 = models.IntegerField(blank=True, null=True)
    a19 = models.IntegerField(blank=True, null=True)
    a20 = models.IntegerField(blank=True, null=True)