from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from Answering.logic.answer import answerRelatedTo
from .forms import QuestionForm
from .models import Response
from Reference.models import Response as ReferenceResponse

def question(request):
    response, _ = Response.objects.get_or_create(id=1)
    referenceResponse, _ = ReferenceResponse.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            response.content = ''
            response.save()
            if question != '':
                answer = answerRelatedTo(question, question[0] == 'M', referenceResponse.subject, referenceResponse.topics)
                request.session['answer'] = answer
        return redirect('question')
    answer = request.session.get('answer', '')
    form = QuestionForm()
    return render(request, 'question.html', context={'answer': answer, 'form': form, 'FastMessageAnswer': response.content})

def FastMessageAnswer(request):
    response, _ = Response.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['question']
            if answer != '':
                response.content = answer
                response.save()
    form = QuestionForm()
    return render(request, 'FastMessageAnswer.html', context={'FastMessageAnswer': response.content, 'form': form})