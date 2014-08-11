from django.shortcuts import render
from datetime import date
from django.http import Http404
from Apps.Blog.models import Article

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    article_list = Article.objects.filter(published=True).order_by('-pub_date')
    paginator = Paginator(article_list, 5)

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context_dictionary = {
        'page': 'home',
        'articles': articles,
        'url': request.build_absolute_uri()
    }

    return render(request, 'Blog/home.html', context_dictionary)

def view_article(request, slug):
    try:
        article = Article.objects.get(slug=slug, published=True)
    except Article.DoesNotExist:
        raise Http404

    tags = article.tags.split(',')
    for tag in tags:
        tag.strip()

    article.tags = tags
    article.url = request.build_absolute_uri()

    context_dictionary = {
        'page': 'view_article',
        'article': article,
    }

    return render(request, 'Blog/view_article.html', context_dictionary)


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