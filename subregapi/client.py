import requests
from .models import Contact, ContactItem, ContactList, ContactId, ErrorResponse, ResellerList

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

    def _get_request(self, path, params=None):
        headers = {"Accept": "application/json", "Authorization": f"Bearer {self.api_key}"}
        url = self.base_url + path
        response = requests.get(url, headers=headers, params=params)
        #print(response.json['error'])
        return response

    def _post_request(self, path, data):
        headers = {"Accept": "application/json", "Authorization": f"Bearer {self.api_key}"}
        url = self.base_url + path
        response = requests.post(url, data=data, headers=headers)
        return response

    def _put_request(self, path, data):
        headers = {"Accept": "application/json", "Authorization": f"Bearer {self.api_key}"}
        url = self.base_url + path
        response = requests.put(url, data=data, headers=headers)
        return response

    @property
    def domains_path(self):
        return "domains"

    def get_domains(self):
        """https://api.demoreg.net/#/Domains/get_domains"""
        return self._get_request(self.domains_path)['domains']

    def check_domain(self, domain, for_user = None):
        """https://api.demoreg.net/#/Domains/get_domains__domain__check"""
        params = {"for_user": for_user} if for_user else {}
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}/check", params=params)

    def multicheck_domains(self, domains = None):
        """https://api.demoreg.net/#/Domains/post_domains_multicheck"""
        if len(domains)>0:
            data = {}
            data["domains"] = domains
            return self._post_request(f"{self.domains_path}/multicheck", data)["results"]

    def get_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/get_domains__domain_"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def register_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/post_domains__domain_"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def set_domains(self):
        """https://api.demoreg.net/#/Domains/put_domains__domain_"""
        return self._get_request(self.domains_path)

    def delete_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/delete_domains__domain_"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def renew_domain(self, domain=None):
        """https://api.demoreg.net/#/domains/post_domains__domain__renew"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def restore_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/post_domains__domain__restore"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def trasfer_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/post_domains__domain__transfer"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def account_transfer_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/post_domains__domain__account_transfer"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    def autorenew_domain(self, domain=None):
        """https://api.demoreg.net/#/Domains/put_domains__domain__autorenew"""
        if domain:
            return self._get_request(f"{self.domains_path}/{domain}")

    @property
    def dns_path(self):
        return "dns"

    def analyze_dnsrecords(self, domain=None, type=None):
        params = {"dnstype": type} if type else {}
        return self._get_request(f"{self.dns_path}/{domain}/analyze", params=params)

    def get_dnsrecords(self, domain=None):
        return self._get_request(f"{self.dns_path}/{domain}")

    @property
    def contacts_path(self):
        return "contacts"

    def get_contact(self, id=None):
        r = self._get_request(f"{self.contacts_path}/{id}")
        if r.status_code == 200:
            return Contact.from_dict(r.json())

    def get_contacts(self):
        r =  self._get_request(self.contacts_path)
        if r.status_code == 200:
            return ContactList.from_dict(r.json())

    def set_contact(self, id=None, contact=None):
        r = self._put_request(f"{self.contacts_path}/{id}", contact.to_json())
        success = r.status_code == 200
        return success

    def create_contact(self, contact):
        r = self._post_request(self.contacts_path, contact.to_json())
        print(r.status_code)
        if r.status_code == 200:
            return ContactId.from_dict(r.json())
        else:
            return None

    @property
    def resellers_path(self):
        return "resellers"

    def get_resellers(self):
        r =  self._get_request(self.resellers_path)
        if r.status_code == 200:
            return ResellerList.from_dict(r.json())

    def get_reseller_by_hostname(self, hostname=None):
        r = self._get_request(f"{self.resellers_path}/{hostname}")
        if r.status_code == 200:
            return ResellerInfo.from_dict(r.json())
        else:
            return None
