#just like Models, forms are classes in Django
from django import forms

#validator to validate data
from django.core import validators

#most of the time we use a form to generate some HTML
class SuggestionForm(forms.Form):

	#we have three fields currently
	name = forms.CharField()
	email = forms.EmailField()

	#so that we verify both emails are correct
	verify_email = forms.EmailField(label='verify email')

	#the widget is how the thing is represented to HTML
	suggestions = forms.CharField(widget=forms.Textarea)

	#this will help us prevent from submissions of the form by bots
	#there will be a hidden input, an invisibe field, normally called honey pot and if anything
	#is in that honeypot, then it is likely that it is a bot. so it will not submit the view

	#this field is not required, and is hidden (we want the field to be blankable - no one should
	#fill it up). The label attribute is for humans, that if they see it by any chance, 
	#they know to leave it empty

	#we will see three step to do this:

	#1

	#honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label='Leave Empty')

	#now when django calls the is_valid(), it runs through every single field, and looks for functions
	#such as clean_nameOfTheField in the form (such that clean_name(), clean_email()). If it doesnt
	#find the function, it does the cleaning itself.

	#here, we overide the cleaning method for one individual field. This will be the method called
	#when is_vaild() is called by Django to clean the fields.

	"""
	def clean_honeypot(self):
		honeypot = self.cleaned_data['honeypot']
		if len(honeypot): #if there is something in the honeypot, which shouldn't be -
			raise forms.ValidationError('honeypot should be left empty. Bad bot!')

		return honeypot #then we send back the field itself, no matter what
	"""

	#note that the above method to use honeypot is not the best way because we have to repeat the
	#function again if we want another field to be validated for any bot attacks

	#so we will use validator to validate data:

	#2

	honeypot = forms.CharField(required=False, widget=forms.HiddenInput, label='Leave Empty',
								validators=[validators.MaxLengthValidator(0)])
	#all of above methods lets us validate single field at a time

	#so for validating every single field in the form, we use form's clean method 

	#this clean method is for entire form, not just a single field
	#also, other validation could go in the clean method too.
	def clean(self):

		#gets all the cleaned data
		cleaned_data = super().clean()
		email = cleaned_data['email'] # or cleaned_data.get('email')
		verify = cleaned_data['verify_email']

		if email != verify:
			raise forms.ValidationError('Both email should match!')
		#we dont need to return anything from the 'clean()' method

