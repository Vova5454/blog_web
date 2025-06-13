from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("slug", unique=True)
    description = models.TextField("Описание")

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField("Текст")
    pub_date = models.DateTimeField("Время выпуска")
    author = models.ForeignKey("Пользователь", 
                               User,
                               on_delete=models.CASCADE,
                               related_name="posts")
    group = models.ForeignKey("Группа", 
                              Group,
                              on_delete=models.SET_NULL,
                              blank=True, null=True,
                              related_name="posts")

    def __str__(self):
        return self.text[:15]

    class Meta:
        ordering = ("-pub_date",)
