from django.http import HttpResponse
from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

def index(request):
    # return HttpResponse('index')
    return render(request, 'index.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                sg = SendGridAPIClient(os.environ.get('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'))
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')