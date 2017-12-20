from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction, IntegrityError
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View

from third_parties.clearbit_wrapper import ClearbitCompanySearch

from .models import Company
from .forms import CompanySearchForm, CompanyAddForm


@method_decorator(login_required, name='dispatch')
class CompanyAddedView(ListView):
    context_object_name = 'companies_list'
    template_name = 'companies/list.html'
    form_class = CompanyAddForm

    def get_queryset(self):
        return Company.objects.filter(user=self.request.user)

    def get(self, request):
        return render(request, self.template_name, {
            'company_list': self.get_queryset()
        })

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            clearbit_id = form.cleaned_data['clearbit_id']
            company = ClearbitCompanySearch().get_company(clearbit_id, hash_id=True)
            if company:
                try:
                    with transaction.atomic():
                        Company.objects.create(
                            description=company.description,
                            name=company.name,
                            clearbit_id=company.clearbit_id,
                            user=self.request.user,
                            updated_at=company.indexed_at,
                            logo_url=company.logo)
                        return render(request, self.template_name, {
                            'company_list': self.get_queryset()
                        })
                except IntegrityError:
                    messages.error(request,
                                   "You've added this company before.")
        else:
            messages.error(request, 'Invalid form. Please try again.')
        return render(request, self.template_name, {
            'company_list': self.get_queryset()
        })


class CompanySearchView(View):
    form_class = CompanySearchForm
    template_name = 'companies/search.html'
    context_object_name = 'company_list'

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            query = form.cleaned_data['search_query']
            company = ClearbitCompanySearch().get_company(query, hash_id=False)
            if not company:
                messages.info(request, 'No companies found. Try again.')
            return render(request, self.template_name, {'form': form, 'company_details': company})
        else:
            messages.error(request, 'Invalid form. Please try again.')

        return render(request, self.template_name, {'form': form})
