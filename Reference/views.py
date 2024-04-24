from django.shortcuts import render

from Reference.forms import ReferenceForm
from Reference.models import Response

def reference(request):
    response, _ = Response.objects.get_or_create(id=1)
    if request.method == 'POST':
        form = ReferenceForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            topics = form.cleaned_data['topics']
            if subject != '' and topics != '':
                response.subject = subject
                response.topics = topics
                response.save()
    form = ReferenceForm()
    return render(request, 'reference.html', context={'subject': response.subject, 'topics': response.topics})