from django.shortcuts import render
from datetime import date

# Create your views here.
def home(request):
    context_dictionary = {
        'page': 'home',
    }
    return render(request, 'Blog/home.html', context_dictionary)

def about(request):
    context_dictionary = {
        'page': 'about',
    }

    born = date(1996, 4, 10)
    today = date.today()
    age = today.year-born.year-((today.month, today.day) < (born.month, born.day))

    context_dictionary['age'] = age

    return render(request, 'Blog/about.html', context_dictionary)

def about_vblog(request):
    context_dictionary = {
        'page': 'about_vblog',
    }

    return render(request, 'Blog/about_vblog.html', context_dictionary)

def portfolio(request):
    context_dictionary = {
        'page': 'portfolio',
    }
    return render(request, 'Blog/portfolio.html', context_dictionary)

def contacts(request):
    context_dictionary = {
        'page': 'contacts',
    }
    return render(request, 'Blog/contacts.html', context_dictionary)