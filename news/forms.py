from django import forms

SITES = (
    ('', 'Choose...'),
    ('nepalitimes', 'Nepali Times'),
    ('newsapi', 'News API')
)

class NewsForm(forms.Form):
    scrape_from = forms.ChoiceField(choices=SITES)
