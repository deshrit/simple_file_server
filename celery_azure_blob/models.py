from django.db import models

# Create your models here.
class File(models.Model):
    uploaded_at = models.DateTimeField(auto_now=True)
    file_name = models.CharField(max_length=254)
    file_ext = models.CharField(max_length=50)
    blob_name = models.CharField(max_length=37, db_index=True)
    file_url = models.CharField(max_length=254)
    is_deleted = models.BooleanField(default=False)