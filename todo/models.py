from django.db import models

class TodoModel(models.Model):
    CHECK_CHOICES = (
        ('✅', '✅'),
        ('☑️', '☑️')
    )
    title = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=CHECK_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


