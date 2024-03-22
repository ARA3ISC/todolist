from django.db import models

# Create your models here.

class Item(models.Model):
	STATUS = {
		'P': 'In progress',
		'D': 'Done',
	}
	title = models.CharField(max_length=255, null=True)
	text = models.CharField(max_length=255, null=True)
	status = models.CharField(max_length=1, choices=STATUS, default=STATUS['P'])

	def __str__(self):
		return self.title
