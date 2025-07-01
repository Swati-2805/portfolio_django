from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact/thankyou.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
def thankyou_view(request):
    return render(request, 'contact/thankyou.html')
def home_view(request):
    return render(request, 'contact/index.html')

def about_view(request):
    return render(request, 'contact/about.html')

def projects_view(request):
    return render(request, 'contact/projects.html')
