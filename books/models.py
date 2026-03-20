from django.db import models


class BookModel(models.Model):
    name = models.CharField(blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    book_file = models.FileField(upload_to="media", blank=False, null=False)

    class Meta:
        ordering = ["pub_date"]
        db_table = "BookModel"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.name} - {self.date}"
