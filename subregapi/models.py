from __future__ import annotations
from dataclasses import dataclass
from dataclass_wizard import JSONWizard

# General dataclasses BEGIN
@dataclass
class ErrorResponse(JSONWizard):
    """
    ErrorResponse dataclass

    """
    error: str
    code_major: int
    code_minor: int

# General dataclasses END

# Domains API dataclasses BEGIN
# Domains API dataclasses END

# Contacts API dataclasses BEGIN
@dataclass
class Contact(JSONWizard):
    """
    Contact dataclass

    """
    id: str
    name: str
    surname: str
    org: str
    street: str
    city: str
    pc: str
    sp: str
    cc: str
    email: str
    phone: str
    fax: str
    need_validation: int

@dataclass
class ContactList(JSONWizard):
    """
    ContactList dataclass

    """
    contacts: list[ContactItem]
    count: int

@dataclass
class ContactItem:
    """
    ContactItem dataclass

    """
    name: str
    surname: str
    org: str
    street: str
    city: str
    pc: str
    sp: str
    cc: str
    email: str
    phone: str
    fax: str
    params: str
    authorized: str
    id: str

@dataclass
class ContactId(JSONWizard):
    """
    ContactId dataclass

    """
    contactid: str

# Contacts API dataclasses END

# Hosts API dataclasses BEGIN
@dataclass
class Hostname(JSONWizard):
    """
    Hostname dataclass

    """
    hostname: str
    ipv4: list[str]
    ipv6: list[str]

# Hosts API dataclasses END

# Orders API dataclasses BEGIN
# Orders API dataclasses END

# DNS API dataclasses BEGIN
# DNS API dataclasses END

# Resellers API dataclasses BEGIN
@dataclass
class ResellerList(JSONWizard):
    """
    ResellerList dataclass

    """
    resellers: list[Reseller]


@dataclass
class ResellerItem:
    """
    ResellerItem dataclass

    """
    hostname: str
    title: str
    website: str
    email: str
    phone: str
    postal_address: str
    facebook: str
    twitter: str
    linkedin: str
    langs: list[str]
    default_lang: str
    currencies: list[str]
    default_currency: str
    bank_accounts: list
    paypal_account: str
    default_pricelist: str
    vat_rate: int
    top_tlds: list[str]
    default_nameservers: list[str]
    contact_form_email: str
    authorization_email_: str

@dataclass
class ResellerInfo(JSONWizard):
    """
    ResellerInfo dataclass

    """
    reseller: Reseller


@dataclass
class Reseller:
    """
    Reseller dataclass

    """
    hostname: str
    title: str
    website: str
    email: str
    phone: str
    postal_address: str
    facebook: str
    twitter: str
    linkedin: str
    langs: list[str]
    default_lang: str
    currencies: list[str]
    default_currency: str
    bank_accounts: list
    paypal_account: str
    default_pricelist: str
    vat_rate: int
    top_tlds: list[str]
    default_nameservers: list[str]
    contact_form_email: str
    authorization_email_: str

# Resellers API dataclasses END
