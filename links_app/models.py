from django.db import models

from users.models import User

class Category(models.Model):
    title = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Links(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    link = models.CharField(unique=True,max_length=30)
    origin_url = models.URLField(max_length=300)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    privacy = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

    def __str__(self):
        return f'{self.link} - {self.user}'

