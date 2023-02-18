import requests

class SubregApi:
    def __init__(self, api_key):
        self._api_key = api_key
        self._base_url = "https://api.subreg.cz/"

    @property
    def api_key(self):
        return self._api_key

    @property
    def base_url(self):
        return self._base_url

    def _make_request(self, path, data):
        headers = {"Accept": "application/json", "Authorization": f"Bearer {self.api_key}"}
        url = self.base_url + path
        response = requests.get(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    @property
    def domains_path(self):
        return "domains"

    def get_domains(self, domain=None):
        data = {"domain": domain} if domain else {}
        return self._make_request(self.domains_path, data)

    @property
    def create_domain_path(self):
        return "domain/create"

    def create_domain(self, domain, registrant_id, auth_info=None, period=1, dns=[], private_whois=False):
        data = {
            "domain": domain,
            "registrant_id": registrant_id,
            "auth_info": auth_info,
            "period": period,
            "dns": dns,
            "private_whois": private_whois,
        }
        return self._make_request(self.create_domain_path, data)

    @property
    def contacts_path(self):
        return "contacts"

    def get_contacts(self, contact=None, type=None):
        data = {"contact": contact, "type": type}
        return self._make_request(self.contacts_path, data)

    @property
    def create_contact_path(self):
        return "domain/create-contact"

    def create_contact(self, contact):
        return self._make_request(self.create_contact_path, contact)

