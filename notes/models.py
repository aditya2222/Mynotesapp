from django.db import models

# Create your models here.

class Document(models.Model):
	Subject = models.CharField(max_length=120,blank=True)
	description = models.TextField()
	document = models.FileField(upload_to='documents/')
	uploaded_at = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.Subject