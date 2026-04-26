from django.db import models


class BookModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    pub_date = models.DateTimeField(auto_now_add=True)
    book_file = models.FileField(upload_to="%Y/%m/%d/")

    class Meta:
        ordering = ["pub_date"]
        db_table = "BookModel"
        verbose_name = "Book"
        verbose_name_plural = "Books"

    def __str__(self):
        return f"{self.name} - {self.date}"
