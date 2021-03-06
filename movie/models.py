from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


class Genre(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        genres = ['Action', 'Animation', 'Comedy', 'Crime', 'Drama', 'Experimental', 'Fantasy', 'Historical', 'Horror',
                  'Romance', 'Science Fiction', 'Thriller', 'Western', 'Other', ]
        errors = {}
        title = self.title
        if title not in genres:
            errors['title'] = _(f"Must be one of genre from {genres}")
        if errors:
            raise ValidationError(errors)


class Director(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    first_name = models.CharField(max_length=200, blank=True, null=True)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    number = models.CharField(max_length=10, blank=True, null=True)
    dob = models.DateField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=230, blank=True, null=True)
    gender = models.CharField(choices=GENDER, max_length=30, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.number}, {self.website}"


class Studio(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    prefix = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title


def new_movie_save(instance, filename):
    return 'movies/{0}/{1}'.format(instance.title, filename)


class NewMovie(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    prefix = models.CharField(max_length=500, blank=True, null=True)
    subtitle = models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    director = models.ManyToManyField(Director, blank=True)
    studio = models.ForeignKey('Studio', on_delete=models.SET_NULL, null=True)
    release_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to=new_movie_save, null=True, blank=True)
    review = models.TextField()
    genre = models.ManyToManyField(Genre, blank=True)
    asin = models.CharField(max_length=200, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        # return f"{self.title} by {self.director.first_name} released on {self.release_date}"
        return self.title

    # def display_genre(self):
    #     return ', '.join(genre.title for genre in self.genre.all()[:3])
    # display_genre.short_description = 'Genre'
    #
    # def display_director(self):
    #     return ', '.join(director.first_name for director in self.director.all()[:3])
    # display_director.short_description = 'Director'
