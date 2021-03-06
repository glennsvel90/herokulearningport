from django.contrib import messages
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from . import forms

def suggestion_view(request):
    """ Make appear the suggestion page """

    form = forms.SuggestionForm()
    if request.method == 'POST':
        form = forms.SuggestionForm(request.POST)
                form.cleaned_data['suggestion'],
                '{name} <{email}>'.format(**form.cleaned_data),
                ['kenneth@teamtreehouse.com']
            )
            messages.add_message(request, messages.SUCCESS,
                                 'Thanks for your suggestion!')
            return HttpResponseRedirect(reverse('suggestion'))
    return render(request, 'suggestion_form.html', {'form': form})
