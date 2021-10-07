from django import forms

SITES = (
    ('nepalitimes', 'Nepali Times'),
    ('newsapi', 'News API')
)

class NewsForm(forms.Form):
    source = forms.ChoiceField(choices=SITES)
