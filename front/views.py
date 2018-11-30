from django.shortcuts import render, redirect, reverse
from front.models import Article, Tag, Author, AuthorInfo

# Create your views here.


def index(request):
    """
    首页视图函数，显示所有文章信息
    :param request:
    :return:
    """
    articles = Article.objects.all()
    return render(request, 'index.html', context={"articles": articles})


def add_article(request):
    """
    添加文章视图函数，发布一篇文章
    :param request:
    :return:
    """
    if request.method == 'GET':
        return render(request, 'add_article.html')
    else:
        title = request.POST.get("title")
        content = request.POST.get("content")
        author_name = request.POST.get("author")
        # 从数据库中查找该作者是否已经存在，如果不存在则添加到数据库中
        author = Author.objects.filter(name=author_name).first()
        if not author:
            author = Author(name=author_name)
            author.save()
        # 文章信息存储到数据库中
        article = Article(title=title, content=content, author=author)
        article.save()
        # 文章标签存储到数据库中
        tag = request.POST.get("tag")
        tag = Tag(name=tag)
        tag.save()
        article.tags.add(tag)
        return redirect(reverse('index'))


def article_detail(request, article_id):
    """
    文章详情页视图函数
    :param request:
    :param article_id:
    :return:
    """
    # 根据文章 id 查找文章
    article = Article.objects.get(id=article_id)
    return render(request, 'article_detail.html', context={"article": article})


def author_articles(request, author_id):
    """
    作者信息详情页视图函数
    :param request:
    :param author_id:
    :return:
    """
    # 根据作者 id 查找作者
    author = Author.objects.get(id=author_id)
    return render(request, 'author_articles.html', context={"author": author})


def delete_article(request):
    """
    删除文章视图函数
    :param request:
    :return:
    """
    if request.method == 'POST':
        article_id = int(request.POST.get('article_id'))
        article = Article.objects.get(id=article_id)
        article.delete()
        return redirect(reverse('index'))
    else:
        raise RuntimeError("删除图书的method错误！")
