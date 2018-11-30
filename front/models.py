from django.db import models

# Create your models here.
# python manage.py makemigrations 生成迁移脚本文件。
# python manage.py migrate 将迁移脚本文件映射到数据库中。


class Author(models.Model):
    """
    作者重要信息表
    """
    name = models.CharField(max_length=100)


class AuthorInfo(models.Model):
    """
    作者详细信息表，一对一（一个作者行对应唯一的详细信息行）
    """
    country = models.CharField(max_length=100)
    author = models.OneToOneField("Author", on_delete=models.CASCADE, related_name='info')


class Article(models.Model):
    """
    文章信息表，一对多（一个作者可以有多篇文章）
    """
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, related_name='articles')

    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id, self.title)


class Tag(models.Model):
    """
    文章标签信息表，多对多（一篇文章有多个标签，一个标签可以对应多篇文章）
    """
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField("Article", related_name='tags')
