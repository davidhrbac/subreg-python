import requests

class SubregApi:
    def __init__(self, api_key, base_url = "https://api.subreg.cz/"):
        self._api_key = api_key
        self._base_url = base_url

    @property
    def api_key(self):
        return self._api_key

    @property
    def base_url(self):
        return self._base_url

    def _make_request(self, path, params=None):
        headers = {"Accept": "application/json", "Authorization": f"Bearer {self.api_key}"}
        url = self.base_url + path
        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            print(response.json()['error'])
        # TODO - add exception
        response.raise_for_status()
        return response.json()

    @property
    def domains_path(self):
        return "domains"

    def check_domain(self, domain=None):
        if domain:
            return self._make_request(f"{self.domains_path}/{domain}/check")

    def get_domains(self):
        return self._make_request(self.domains_path)

    def get_domain(self, domain=None):
        if domain:
            return self._make_request(f"{self.domains_path}/{domain}")

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
    def dns_path(self):
        return "dns"

    def analyze_dnsrecords(self, domain=None, type=None):
        params = {"dnstype": type} if type else {}
        return self._make_request(f"{self.dns_path}/{domain}/analyze", params=params)

    def get_dnsrecords(self, domain=None):
        return self._make_request(f"{self.dns_path}/{domain}")

    @property
    def contacts_path(self):
        return "contacts"

    def get_contact(self, id=None):
        return self._make_request(f"{self.contacts_path}/{id}")

    def get_contacts(self):
        return self._make_request(self.contacts_path)

    @property
    def create_contact_path(self):
        return "domain/create-contact"

    def create_contact(self, contact):
        return self._make_request(self.create_contact_path, contact)

