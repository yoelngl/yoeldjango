from django import forms

from .models import Hajime
# class PostForm(forms.Form):
# 	name = forms.CharField(max_length=25,widget=forms.TextInput(attrs={'class': 'form-control col-6','placeholder':'Full Name'}),required=False)
# 	description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control col-6','rows':3,'placeholder':'Description'}), required=False)

# 	def clean_name(self):
# 		name = self.cleaned_data.get('name')

# 		if name == '':
# 			raise forms.ValidationError('Field Name has required')	

# 		return name


class PostForm(forms.ModelForm):
	class Meta:
		model = Hajime
		fields = [
			'name',
			'description',
			'majors',
		]
		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control col-5','placeholder':'Input your Name'}),
			'description': forms.Textarea(attrs={'class':'form-control col-5','rows':3,'placeholder':'Input your Description'}),
			'majors': forms.Select(attrs={'class':'form-control col-5'})
		}


