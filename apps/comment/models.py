from django.db import models
from django.db.models.signals import pre_save, post_save
from django.conf import settings


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    post = models.ForeignKey('blog.Blog', on_delete=models.CASCADE)
    top_level_comment_id = models.IntegerField(null=True, blank=True)
    message = models.TextField()
    is_reply = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.author.full_name:
            return f'{self.author.full_name}s comment'
        return self.author.username

    @property
    def get_children(self):
        children = Comment.objects.filter(top_level_comment_id=self.id).exclude(id=self.id)
        return children


def comment_pre_save(instance, sender, *args, **kwargs):
    if instance.parent is not None:
        instance.is_reply = True


def comment_post_save(instance, sender, created, *args, **kwargs):
    if created:
        if instance.top_level_comment_id is None:
            top_level_comment_id = instance.id
            parent = instance
            while True and parent.parent is not None:
                top_level_comment_id = parent.parent.id
                parent = parent.parent
            instance.top_level_comment_id = top_level_comment_id
            instance.save()


pre_save.connect(comment_pre_save, sender=Comment)
post_save.connect(comment_post_save, sender=Comment)
