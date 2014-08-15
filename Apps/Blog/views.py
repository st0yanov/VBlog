# -*- coding: utf-8 -*- 

from django.shortcuts import render
from datetime import date
from django.http import HttpResponse, Http404
from Apps.Blog.models import Article, Portfolio

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from haystack.query import SearchQuerySet
import simplejson as json

from django.utils.html import escape

from Apps.Blog.forms import ContactForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.conf import settings

# Create your views here.
def home(request):
    # Get last 5 articles
    article_list = Article.objects.filter(published=True).order_by('-pub_date')
    paginator = Paginator(article_list, 5)

    page = request.GET.get('page')

    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    # Social Data
    social_data = [
        {
            'name': 'rss',
            'href': '#',
            'title': 'RSS',
        },
        {
            'name': 'facebook',
            'href': 'https://www.facebook.com/Veskoyy',
            'title': 'Facebook профил'
        },
        {
            'name': 'twitter',
            'href': 'https://twitter.com/VeskoyCom',
            'title': 'Twitter профил'
        },
        {
            'name': 'linkedin',
            'href': 'https://www.linkedin.com/pub/veselin-stoyanov/a1/a4/44b',
            'title': 'LinkedIn профил'
        },
        {
            'name': 'gplus',
            'href': 'https://plus.google.com/u/0/104236216198044213208',
            'title': 'Google+ профил'
        },
        {
            'name': 'github',
            'href': 'https://github.com/veskoy',
            'title': 'GitHub профил'
        },
        {
            'name': 'youtube',
            'href': 'https://www.youtube.com/user/VeskoyCom',
            'title': 'YouTube профил'
        },
    ]

    context_dictionary = {
        'page': 'home',
        'articles': articles,
        'url': request.build_absolute_uri(),
        'social_data': social_data,
    }

    return render(request, 'Blog/home.html', context_dictionary)

def search_articles(request):
    search_text = request.POST.get('search_text', '')

    if len(search_text) > 1:
        articles = SearchQuerySet().filter_or(content_auto=search_text).filter_or(tags=search_text).filter_or(content=search_text).order_by('-pub_date')[:10]
        suggestions = []
        for article in articles:
            suggestions.append({'title': escape(article.object.title), 'url': escape(article.object.get_absolute_url())})
        ok = True
    else:
        suggestions = None
        ok = False
    
    response_data = json.dumps({
        'ok': ok,
        'articles': suggestions,
    })

    return HttpResponse(response_data, content_type='application/json')

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
    projects_list = Portfolio.objects.all().order_by('-pub_date')

    context_dictionary = {
        'page': 'portfolio',
        'projects': projects_list
    }
    return render(request, 'Blog/portfolio.html', context_dictionary)

def contacts(request):
    success = False
    
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            sender_email = form.cleaned_data['sender_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            email_dictionary = {
                'name': name,
                'sender_email': sender_email,
                'sender_ip': get_client_ip(request),
                'subject': subject,
                'message': message,
            }

            email_plaintext = render_to_string('Blog/emails/contact_plaintext.txt', email_dictionary)
            email_html = render_to_string('Blog/emails/contact.html', email_dictionary)

            msg = EmailMultiAlternatives(subject, email_plaintext, sender_email, [settings.CONTACT_EMAIL])
            msg.attach_alternative(email_html, 'text/html')
            if msg.send():
                success = True

    else:
        form = ContactForm()

    context_dictionary = {
        'page': 'contacts',
        'form': form,
        'success': success
    }
    return render(request, 'Blog/contacts.html', context_dictionary)

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip