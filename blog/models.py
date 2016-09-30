#coding:utf8
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=100)
    age  = models.IntegerField()

class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','age')

class Article(models.Model):
    title=models.CharField(max_length=200)
    content = models.TextField()
    url = models.URLField()
    portal = models.ImageField()
    author = models.ForeignKey(Author)

class ArticleAdmin(admin.ModelAdmin):
    list_display =('title','url','author')

class User(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email    = models.EmailField(blank=True, verbose_name='邮箱')


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password','email')

admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(User,UserAdmin)
