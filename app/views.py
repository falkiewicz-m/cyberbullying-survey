from django.shortcuts import render
from .forms import surveyPL, surveyEN
from django.forms.formsets import formset_factory
from .models import QuestionPL, QuestionEN, ChoicePL, ChoiceEN, Current_answerPL, Current_answerEN
from .content import content


def surveyPLview(request):
    context = {
    'lang': 'pl',
    'title': 'Ankieta',
    'content' : content[2],
    'currentURL': '/pl/survey/',
    'otherURL': '/en/survey/'
    }
    # if request.method == 'POST':
    #     form1 = surveyPL(request.POST)
    #     DbAnswer = Current_answerPL()
    #     if form1.is_valid():
    #         for fnum, item in enumerate(form1.fields, start=1):
    #             str_a = 'answers_' + str(fnum)
    #             str_b = 'a' + str(fnum)
    #             choice_str_a = form1.cleaned_data[str_a]
    #             g = ChoiceM.objects.get(question_fk = fnum, choice_text = choice_str_a)
    #             g.numberOfVotes += 1
    #             g.save()
    #             setattr(DbAnswer, str_b, g.id)
    #             DbAnswer.save()
    #         return render(request, 'thanksPL.html', {'form1': form1 })
    #
    # elif request.method == 'GET':
    #     form1 = surveyPL()
    #     return render(request, 'surveyPL.html', {'form1': form1 })
    return render(request, 'surveyPL.html', {'context': context })
def surveyENview(request):
    context = {
    'lang': 'en',
    'title': 'Survey',
    'content' : content[3],
    'currentURL': '/en/survey/',
    'otherURL': '/pl/survey/'
    }
    #     form1 = surveyEN(request.POST)
    #     DbAnswer = Current_answerEN()
    #     if form1.is_valid():
    #         for fnum, item in enumerate(form1.fields, start=1):
    #             str_a = 'answers_' + str(fnum)
    #             str_b = 'a' + str(fnum)
    #             choice_str_a = form1.cleaned_data[str_a]
    #             g = ChoiceM.objects.get(question_fk = fnum, choice_text = choice_str_a)
    #             g.numberOfVotes += 1
    #             g.save()
    #             setattr(DbAnswer, str_b, g.id)
    #             DbAnswer.save()
    #         return render(request, 'thanksEN.html', {'form1': form1 })
    #
    # elif request.method == 'GET':
    #     form1 = surveyPL()
    #     return render(request, 'surveyEN.html', {'form1': form1 })
    return render(request, 'surveyEN.html', {'context': context })
def excludeCSRF(dict, csrft):
    return {k:v for k,v in dict if k not in csfrt}

def indexPLview(request):
    context = {
        'lang': 'pl',
        'title': 'Strona główna',
        'content' : content[0],
        'currentURL': '/pl/',
        'otherURL': '/en/'
    }

    return render(request, 'indexPL.html', {'context' : context })

def indexENview(request):
    context = {
        'lang': 'en',
        'title': 'Main page',
        'content' : content[1],
        'currentURL': '/en/',
        'otherURL': '/pl/'
    }
    return render(request, 'indexEN.html', {'context' : context })

def thanksPLview(request):
    context = {
        'lang': 'pl',
        'title': 'Dziękuję!',
        'content' : content[4],
        'currentURL': '/pl/thanks/',
        'otherURL': '/en/thanks/'
        }
    return render(request, 'thanksPL.html', {'context' : context })

def thanksENview(request):
    context = {
        'lang': 'en',
        'title': 'Thanks!',
        'content' : content[5],
        'currentURL': '/en/thanks/',
        'otherURL': '/pl/thanks/'
    }
    return render(request, 'thanksEN.html', {'context' : context })

def resultsPLview(request):
    context = {
        'lang': 'pl',
        'title': 'Wyniki',
        'content' : content[6],
        'currentURL': '/pl/results',
        'otherURL': '/en/results'
    }
    return render(request, 'resultsPL.html', {'context' : context })

def resultsENview(request):
    context = {
        'lang': 'en',
        'title': 'Results',
        'content' : content[7],
        'currentURL': '/en/results/',
        'otherURL': '/pl/results'
    }
    return render(request, 'resultsEN.html', {'context' : context })
