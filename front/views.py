from django.shortcuts import render, redirect, reverse
from front.models import Article, Tag, Author, AuthorInfo

# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request, 'index.html', context={"articles": articles})


def add_article(request):
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        author_name = request.POST.get("author")
        author = Author.objects.filter(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            author.save()
        article = Article(title=title, content=content, author=author)
        article.save()
        tag = request.POST.get("tag")
        tag = Tag(name=tag)
        tag.save()
        article.tags.add(tag)
        return redirect(reverse('index'))


def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail.html', context={"article": article})


def author_articles(request, author_id):
    author = Author.objects.get(id=author_id)
    return render(request, 'author_articles.html', context={"author": author})


def delete_article(request):
    if request.method == 'POST':
        article_id = int(request.POST.get('article_id'))
        article = Article.objects.get(id=article_id)
        article.delete()
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除图书的method错误！")
