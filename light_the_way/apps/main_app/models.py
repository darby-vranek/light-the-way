from django.db import models


class Tag(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey('Category', on_delete=models.CASCADE)
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	def __str__(self):
		return '#' + self.name


class Category(models.Model):
	name = models.CharField(max_length=100)
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	def __str__(self):
		return self.name


class Resource(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()
	description = models.TextField(default='')
	tags = models.ManyToManyField(Tag, related_name='tags')
	required_tags = models.ManyToManyField(Tag, related_name='required_tags')
	date_added = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)

	def __str__(self):
		return self.name
