from django.db import models
from accounts.models import User
import jdatetime


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, unique=True)
<<<<<<< HEAD
    parent = models.ForeignKey(
        to="self", null=True, blank=True, on_delete=models.SET_NULL
    )
=======
    parent = models.ForeignKey(to='self', null=True, blank=True, on_delete=models.SET_NULL)
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def jcreated_at(self):
<<<<<<< HEAD
        return jdatetime.datetime.fromgregorian(
            datetime=self.created_at
        ).strftime("%Y-%m-%d %H:%M:%S")

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.updated_at
        ).strftime("%Y-%m-%d %H:%M:%S")
=======
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y-%m-%d %H:%M:%S')

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y-%m-%d %H:%M:%S')
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def jcreated_at(self):
<<<<<<< HEAD
        return jdatetime.datetime.fromgregorian(
            datetime=self.created_at
        ).strftime("%Y-%m-%d %H:%M:%S")

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.updated_at
        ).strftime("%Y-%m-%d %H:%M:%S")
=======
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y-%m-%d %H:%M:%S')

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y-%m-%d %H:%M:%S')
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("published", "Published"),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, null=True, unique=True)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to="posts/%Y/%m/%d/")
    body = models.TextField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="draft"
    )
    visit = models.IntegerField(default=0)
<<<<<<< HEAD
    user = models.ForeignKey(
        to=User, related_name="posts", null=True, on_delete=models.SET_NULL
    )
    tag = models.ManyToManyField(to=Tag, related_name="posts", default=None)
    category = models.ManyToManyField(
        to=Category, related_name="posts", default=None, null=True
    )
=======
    user = models.ForeignKey(to=User, related_name='posts', null=True, on_delete=models.SET_NULL)
    tag = models.ManyToManyField(to=Tag, related_name='posts', default=None)
    category = models.ManyToManyField(to=Category, related_name='posts', default=None, null=True)
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def jcreated_at(self):
<<<<<<< HEAD
        return jdatetime.datetime.fromgregorian(
            datetime=self.created_at
        ).strftime("%Y-%m-%d %H:%M:%S")

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.updated_at
        ).strftime("%Y-%m-%d %H:%M:%S")
=======
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y-%m-%d %H:%M:%S')

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y-%m-%d %H:%M:%S')
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205


class Comment(models.Model):
    message = models.TextField()
    user = models.ForeignKey(
        to=User, related_name="comments", on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        to=Post, related_name="comments", on_delete=models.CASCADE
    )
    parent = models.ForeignKey(
        to="self", related_name="replies", on_delete=models.CASCADE
    )
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message

    def jcreated_at(self):
<<<<<<< HEAD
        return jdatetime.datetime.fromgregorian(
            datetime=self.created_at
        ).strftime("%Y-%m-%d %H:%M:%S")

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(
            datetime=self.updated_at
        ).strftime("%Y-%m-%d %H:%M:%S")
=======
        return jdatetime.datetime.fromgregorian(datetime=self.created_at).strftime('%Y-%m-%d %H:%M:%S')

    def jupdated_at(self):
        return jdatetime.datetime.fromgregorian(datetime=self.updated_at).strftime('%Y-%m-%d %H:%M:%S')
>>>>>>> d78be232b16d1b2a980ac2491ed17361dd7eb205
