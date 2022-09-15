from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

	user = models.OneToOneField(User,on_delete=models.CASCADE)

	# additional classed
	portfolio_site = models.URLField(blank=True)

	profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

	def __str__(self):
		return self.user.username


#-------------------------------------------------------------------
# class User(models.Model):
#
# 	first_name = models.CharField(max_length=264)
# 	last_name = models.CharField(max_length=264)
# 	email = models.EmailField(max_length=254,unique=True)
#
# 	def __str__(self):
#
# 		return self.first_name + " " + self.last_name
# ---------------------------------------------------------------------
#this will be the class for adding books
class Book(models.Model):

	book_name = models.CharField(max_length=100)
	#book_name = models.CharField(max_length=100,unique=True)
	author_name = models.CharField(max_length=100)
	book_summary = models.CharField(max_length=300)
	def __str__(self):

		return self.book_name
