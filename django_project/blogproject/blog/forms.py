from django import forms 

choices = [
    ('education', 'Education'),
    ('sports', 'Sports'),
    ("entertain", 'Entertainment'),
    ("political", "Politices"),
    ("space", "Space"),
    ("science", 'Science')
]

class Blog(forms.Form):
    title = forms.CharField()
    post = forms.CharField(widget=forms.Textarea)
    categories = forms.ChoiceField(choices=choices)


#<option value='edu'> Education </option>