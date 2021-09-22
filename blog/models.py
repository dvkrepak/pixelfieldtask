from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='title')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Category')
    tags = models.ManyToManyField('Tag', verbose_name='Tags')
    author = models.ForeignKey('User', on_delete=models.PROTECT, verbose_name='Author')
    content = models.TextField(blank=True, verbose_name='Content')
    image = models.ImageField(upload_to="photos",  verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True, verbose_name='Publish date')
    for_logged_users_only = models.BooleanField(default=False, verbose_name='Only for logged users')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'
        ordering = ['-pk']


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class User(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name='Email')
    password = models.CharField(max_length=150, verbose_name='Password')
    name = models.CharField(max_length=255, unique=True, verbose_name='Name')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'