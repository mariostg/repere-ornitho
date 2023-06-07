from django import forms


class SearchSpeciesForm(forms.Form):
    search_term = forms.CharField(max_length=45, min_length=4)
