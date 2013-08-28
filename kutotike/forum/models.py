# coding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    '''user account'''
    user = models.OneToOneField(User,related_name='user_profile',verbose_name=u'用户')
    birthday = models.DateField(verbose_name=u'生日',blank=True)
    point = models.IntegerField(default=0,verbose_name=u'积分')
    signature = models.CharField(max_length=1000,blank=True,verbose_name='签名')
    def __unicode__(self):
        return self.user.username

    # The post_set refer that one post class
    # and get all the items from database
    def get_total_posts(self):
        return self.user.post_set.count()

    def get_absolute_url(self):
        return self.user.get_absolute_url()

class Parents_Tag(models.Model):
    name = models.CharField(max_length=100)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name

## no manytomany,only onetoone
class Tags(models.Model):
    parents_tag = models.ForeignKey(Parents_Tag)
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=110)
    create_time = models.DateTimeField(auto_now_add=True)
    num_topics = models.IntegerField(default=0)
    num_posts = models.IntegerField(default=0)

    class Meta:
        ordering = ['create_time']

    def __unicode__(self):
        return '->'.join(self.parents_tag.name,self.name)


class Topic(models.Model):
    tags = models.ForeignKey(Tags,verbose_name=u'标签')
    name = models.CharField(max_length=1000,verbose_name=u'帖子标题')
    posts = models.ForeignKey('Post',related_name='topics_',blank=True,null=True)
    posted_by = models.ForeignKey(User)
    created_time = models.DateTimeField(auto_now_add=True)
    latest_replied_time = models.DateTimeField(auto_now_add=True)
    num_replies = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-created_time','-latest_replied_time']

    def __unicode__(self):
        return self.name

    def count_nums_replies(self):
        return self.posts.all().count()


class Post(models.Model):
    topic = models.ForeignKey(Topic,verbose_name=u'话题')
    posted_by = models.ForeignKey(User)
    poster_ip = models.IPAddressField(blank=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        if len(self.content)>=50:
            return self.content[:50]+'...'
        else:
            return self.content

    class Meta:
        ordering=['-created_time']
