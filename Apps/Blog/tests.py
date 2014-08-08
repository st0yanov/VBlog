from django.test import TestCase
from django.utils import timezone
from Apps.Blog.models import Article

# Create your tests here.
class ArticleTest(TestCase):
    def test_create_article(self):
        article = Article()

        article.title = 'First article'
        article.pub_date = timezone.now()
        article.content = 'The content of the first article'

        article.save()

        all_articles = Article.objects.all()
        self.assertEquals(len(all_articles), 1)
        only_article = all_articles[0]
        self.assertEquals(only_article, article)

        self.assertEquals(only_article.title, 'First article')
        self.assertEquals(only_article.pub_date.day, article.pub_date.day)
        self.assertEquals(only_article.pub_date.month, article.pub_date.month)
        self.assertEquals(only_article.pub_date.year, article.pub_date.year)
        self.assertEquals(only_article.pub_date.hour, article.pub_date.hour)
        self.assertEquals(only_article.pub_date.minute, article.pub_date.minute)
        self.assertEquals(only_article.pub_date.second, article.pub_date.second)
        self.assertEquals(only_article.content, 'The content of the first article')