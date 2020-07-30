from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import templates
from django.urls import reverse

import misaka  # markdown parse library
# Create your models here.

User = get_user_model()
register = template.Library()


class Group(models.Model):
    name = models.CharField(unique=True, max_length=255)
    slug = models.SlugField(allow_unicode=True, unique=True)
    description = models.TextField(default='')
    description_html = models.TextField(editable=False, default='', blank=True)
    members = models.ManyToManyField(User, through='GroupMember')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('groups:single', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']


class GroupMember(models.Model):
    group = models.ForeignKey(
        Group,
        related_name='memberships',
        on_delete=models.CASCADE, _
    )
    user = models.ForeignKey(
        User,
        related_name='user_groups',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group', 'user')