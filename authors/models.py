from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    pub_date = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField('books.BookModel', related_name="authors", blank=True)

    class Meta:
        ordering = ["pub_date"]
        db_table = "AuthorModel"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.name} ({self.date_of_birth})"
