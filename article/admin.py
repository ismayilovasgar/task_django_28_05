from django.contrib import admin

from article.models import Article
from article.models import MyArticles

# Register your models here.
admin.site.register(Article)
admin.site.register(MyArticles)
