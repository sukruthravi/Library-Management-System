from django.shortcuts import render
from django.http import HttpResponse
# import models that we will use
from AppTwo.models import User,Book
from AppTwo.forms import FormAddBook,FormDeleteBook
#for registration page
from AppTwo.forms import UserForm,UserProfileInfoForm
#for login page

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

# def index(request):
# 	return HttpResponse('<em>My Second App with i tag</em>')

def index(request):

	#render function takes in request,
	# template file path. meaning in templates directory html file path as string,
	# any context .i.e.
	# a dictionary with key value
	return render(request, 'AppTwo/index.html')

@login_required
def user_logout(request):

	logout(request)
	return HttpResponseRedirect(reverse('index'))

def help(request):
	#here in case we want to pass some html content along with the html page
	#then we can create a dictionary and pass the dictionary in context
	#don't forget to update the key value of dictionary in html page
	my_dict = {'dictkey1':'This is the string in dictionary!!'}
	return render(request, 'AppTwo/help.html',context=my_dict)

def user(request):

	#this will give list of User objects ordered by name
	u_objects = User.objects.order_by('first_name')

	user_dict = {'user_objects':u_objects}

	return render(request,'AppTwo/users.html',context=user_dict)
@login_required
def addbook_form(request):

	form = FormAddBook()

	if request.method == "POST":
		form = FormAddBook(request.POST)

		if form.is_valid():
			#do something
			form.save(commit=True)

			#let us now get the list of book objects

			book_objects = Book.objects.order_by('book_name')
			book_dict = {'book_objects':book_objects}

			return render(request,'AppTwo/displaybooks.html',context=book_dict)
		else:
			print("Error Form Invalid")

	return render(request,'AppTwo/addbook_form.html',{'form':form})

@login_required
def displaybook(request):

	#let us now get the list of book objects

	book_objects = Book.objects.order_by('book_name')
	book_dict = {'book_objects':book_objects}

	return render(request,'AppTwo/displaybooks.html',context=book_dict)

@login_required
def deletebook(request):

	form = FormDeleteBook()

	if request.method == "POST":
		form = FormDeleteBook(request.POST)

		if form.is_valid():
			#get the book_name from form and delete that object
			bk_name = form.cleaned_data['book_name']
			Book.objects.filter(book_name=bk_name).delete()

			book_objects = Book.objects.order_by('book_name')
			book_dict = {'book_objects':book_objects}

			return render(request,'AppTwo/displaybooks.html',context=book_dict)
		else:
			print("Error Form Invalid")

	return render(request,'AppTwo/delete.html',{'form':form})

def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			#website link and profile_pic

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registerd = True
		else:
			print(user_form.errors,profile_form.errors)

	else:

		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request,'AppTwo/register.html',
							{'user_form':user_form,
							'profile_form':profile_form,
							'registerd':registered})


def user_login(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("ACCOUNT NOT ACTIVE")
		else:
			print("Someone tried to login and failed!")
			print("Username: {} and password{}".format(username,password))
			return HttpResponse("invalid login details supplied!")

	else:
		return render(request,'AppTwo/login.html',{})



	# 		print('Validation Success!')
	# 		print("Book Name: "+form.cleaned_data['book_name'])
	# 		print("Author Name: "+form.cleaned_data['author_name'])
	# 		print("Summary: "+form.cleaned_data['book_summary'])
	#
	# return render(request,'AppTwo/addbook_form.html',{'form':form})
