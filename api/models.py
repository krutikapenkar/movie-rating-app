from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


def movie_upload_path(instance, filename):
    # Store images in /media/movies/<movie_title>/<filename>
    return f"movies/{filename}"

class Movie(models.Model):
    CATEGORY_CHOICES = [
        ('thriller', 'Thriller'),
        ('romantic', 'Romantic'),
        ('action', 'Action'),
        ('comedy', 'Comedy'),
        ('webseries', 'Web Series'),
        ('drama', 'Drama'),
    ]
    title = models.CharField(max_length=32)
    description = models.TextField(max_length=360)
    image = models.ImageField(
        upload_to=movie_upload_path, 
        null=True, 
        blank=True, 
        default='movies/default.jpg'
    )
    trailer = models.FileField(upload_to="trailers/", null=True, blank=True)
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default='drama'
    )
    is_latest = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def no_of_ratings(self):
        ratings = Rating.objects.filter(movie=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(movie=self)
        for rating in ratings:
            sum += rating.stars

        if len(ratings) > 0:
            return sum / len(ratings)
        else:
            return 0

class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'movie'], name='unique_user_movie')
        ]
        indexes = [
            models.Index(fields=['user', 'movie'])
        ]

