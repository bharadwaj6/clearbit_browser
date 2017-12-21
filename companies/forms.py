from django import forms


class CompanySearchForm(forms.Form):
    search_query = forms.CharField(label='Company Domain', max_length=255)


class CompanyAddForm(forms.Form):
    clearbit_id = forms.CharField(label="Company ID", max_length=255)
