from django.shortcuts import render

# from article.models import Article
from article.models import MyArticles


# Create your views here.
def home__page(request):
    # articles = Article.objects.all()
    articles = MyArticles.objects.all()
    # return render(request, "index.html", {"articles": articles})
    return render(request, "index.html", {"articles": articles})
