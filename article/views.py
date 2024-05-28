from django.shortcuts import render
from article.models import Article


# Create your views here.
def home__page(request):
    articles = Article.objects.all()
    return render(request, "index.html", {"articles": articles})
