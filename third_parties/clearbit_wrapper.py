import clearbit
from dateutil.parser import parse
from requests import HTTPError

from config.settings.base import CLEARBIT_KEY


class Company(object):
    def __init__(self, company_details):
        """Set the attributes for company based on details fetched.

        Note: No need to default values to None with `get` as clearbit API
        fills them in given dictionary format with None (if any).
        """
        self.details = company_details
        self.clearbit_id = self.details['id']
        self.name = self.details['name']
        self.description = self.details['description']
        self.legal_name = self.details['legalName']
        self.domain = self.details['domain']
        self.domain_aliases = self.details['domainAliases']
        self.phone_numbers = self.details['site']['phoneNumbers']
        self.email_addresses = self.details['site']['emailAddresses']
        self.tags = self.details['tags']
        self.sector = self.details['category']['sector']
        self.industry_group = self.details['category']['industryGroup']
        self.industry = self.details['category']['industry']
        self.sub_industry = self.details['category']['subIndustry']
        self.sic_code = self.details['category']['sicCode']
        self.naics_code = self.details['category']['naicsCode']
        self.facebook_handle = self.details['facebook']['handle']
        self.twitter_handle = self.details['twitter']['handle']
        self.linkedin_handle = self.details['linkedin']['handle']
        self.tech = self.details['tech']
        self.logo = self.details['logo']
        self.phone = self.details['phone']
        self.type = self.details['type']

    @property
    def indexed_at(self):
        indexed_at = self.details['indexedAt']
        if indexed_at:
            indexed_at = parse(indexed_at)
        return indexed_at


class ClearbitCompanySearch(object):
    def __init__(self):
        self.client = clearbit
        self.client.key = CLEARBIT_KEY

    def get_company(self, query, hash_id=False):
        try:
            if hash_id:
                # uses clearbit_id to fetch the company.
                response = self.client.Company.find(id=query)
            else:
                response = self.client.Company.find(domain=query)
        except HTTPError as e:
            response = None

        if response:
            return Company(response)

        return None  # explicitly return None if no results found.
