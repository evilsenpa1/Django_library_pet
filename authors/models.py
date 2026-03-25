from django.db import models


class AuthorModel(models.Model):
    name = models.CharField(blank=False, null=False)
    date_of_birth = models.DateField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    books = models.ManyToManyField('books.BookModel', related_name="authors", blank=True)

    class Meta:
        ordering = ["pub_date"]
        db_table = "AuthorModel"
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.name} ({self.date_of_birth})"
