from django import forms


widgets={
	'username':forms.TextInput(attrs=
	{'class':"form-control",
	"placeholder":"enter user name"}),

	'Email':forms.TextInput(attrs=
	{'class':"form-control",
	"placeholder":"enter Email"})}