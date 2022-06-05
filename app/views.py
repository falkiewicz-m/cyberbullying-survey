from django.shortcuts import render
from .forms import surveyPL, surveyEN
from django.forms.formsets import formset_factory
from .models import QuestionPL, QuestionEN, ChoicePL, ChoiceEN, Current_answerPL, Current_answerEN

def surveyPLview(request):
    if request.method == 'POST':
        form1 = surveyPL(request.POST)
        DbAnswer = Current_answerPL()
        if form1.is_valid():
            for fnum, item in enumerate(form1.fields, start=1):
                str_a = 'answers_' + str(fnum)
                str_b = 'a' + str(fnum)
                choice_str_a = form1.cleaned_data[str_a]
                g = ChoiceM.objects.get(question_fk = fnum, choice_text = choice_str_a)
                g.numberOfVotes += 1
                g.save()
                setattr(DbAnswer, str_b, g.id)
                DbAnswer.save()
            return render(request, 'thanksPL.html', {'form1': form1 })

    elif request.method == 'GET':
        form1 = surveyPL()
        return render(request, 'surveyPL.html', {'form1': form1 })

def surveyENview(request):
    if request.method == 'POST':
        form1 = surveyEN(request.POST)
        DbAnswer = Current_answerEN()
        if form1.is_valid():
            for fnum, item in enumerate(form1.fields, start=1):
                str_a = 'answers_' + str(fnum)
                str_b = 'a' + str(fnum)
                choice_str_a = form1.cleaned_data[str_a]
                g = ChoiceM.objects.get(question_fk = fnum, choice_text = choice_str_a)
                g.numberOfVotes += 1
                g.save()
                setattr(DbAnswer, str_b, g.id)
                DbAnswer.save()
            return render(request, 'thanksEN.html', {'form1': form1 })

    elif request.method == 'GET':
        form1 = surveyPL()
        return render(request, 'surveyEN.html', {'form1': form1 })

def excludeCSRF(dict, csrft):
    return {k:v for k,v in dict if k not in csfrt}

def indexPLview(request):
    return render(request, 'indexPL.html')

def indexENview(request):
    return render(request, 'indexEN.html')

def thanksPLview(request):
    return render(request, 'thanksPL.html')

def thanksENview(request):
    return render(request, 'thanksEN.html')

def resultsPLview(request):
    return render(request, 'resultsPL.html')

def resultsENview(request):
    return render(request, 'resultsEN.html')
