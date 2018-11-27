from django.db import models

# Create your models here.
# python manage.py makemigrations 生成迁移脚本文件。
# python manage.py migrate 将迁移脚本文件映射到数据库中。


class Author(models.Model):
    name = models.CharField(max_length=100)


class AuthorInfo(models.Model):
    country = models.CharField(max_length=100)
    author = models.OneToOneField("Author", on_delete=models.CASCADE, related_name='info')


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE, null=True, related_name='articles')

    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id, self.title)


class Tag(models.Model):
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField("Article", related_name='tags')
