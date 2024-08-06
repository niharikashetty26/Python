from django.db import models
from django.utils.translation import gettext_lazy as _

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_("Title"))
    author = models.CharField(max_length=100, verbose_name=_("Author"))
    published_date = models.DateField(verbose_name=_("Published Date"))
    cover = models.ImageField(upload_to='covers/', null=True, blank=True, verbose_name=_("Cover"))

    def __str__(self):
        return self.title

class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews', verbose_name=_("Book"))
    review_text = models.TextField(verbose_name=_("Review Text"))

    def __str__(self):
        return self.review_text[:50]
