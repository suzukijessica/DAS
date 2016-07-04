from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default = timezone.now
    )
    published_date = models.DateTimeField(
        blank = True, null = True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Notification(models.Model):
    post_commented = models.ForeignKey('blog.Post')
    text = models.TextField()

def notify(sender, **kwargs):
    if kwargs['created']:
        comment_post = kwargs['instance']
        notification = Notification()
        notification.post_commented = comment_post.post
        notification.text = 'Esse post tem comentario novo'
        notification.save()

post_save.connect(notify, sender=Comment)
