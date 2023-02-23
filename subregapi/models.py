from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
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
@dataclass
class DomainList(JSONWizard):
    """
    DomainList dataclass

    """
    domains: list[DomainItem]
    count: int


@dataclass
class DomainItem:
    """
    DomainItem dataclass

    """
    name: str
    expire: date
    autorenew: int

@dataclass
class DomainCheckInfo(JSONWizard):
    """
    Data dataclass

    """
    name: str
    avail: int
    price: Price
    price_renew: PriceRenew
    price_transfer: PriceTransfer
    existing_claim_id: str

@dataclass
class Price:
    """
    Price dataclass

    """
    amount: float | str
    amount_with_trustee: float | str
    premium: int
    currency: str

@dataclass
class PriceRenew:
    """
    PriceRenew dataclass

    """
    amount: float | str
    premium: int
    currency: str

@dataclass
class PriceTransfer:
    """
    PriceTransfer dataclass

    """
    amount: float | str
    premium: int
    currency: str

@dataclass
class DomainMultiCheckList(JSONWizard):
    """
    Data dataclass

    """
    results: list[DomainMultiCheckItem]

@dataclass
class DomainMultiCheckItem:
    """
    Result dataclass

    """
    name: str
    avail: int
    error: str

@dataclass
class DomainInfo(JSONWizard):
    """
    Data dataclass

    """
    domain: str
    contacts: Contacts
    hosts: list[str]
    delegated_hosts: list[str]
    registrant: Registrant
    ex_date: date
    cr_date: date
    tr_date: date
    up_date: date
    authid: str
    status: list[str]
    autorenew: int
    premium: int
    price: float | str

@dataclass
class Contacts:
    """
    Contacts dataclass

    """
    admin: list[Admin]
    tech: list[Tech]
    billing: list[Billing]

@dataclass
class Admin:
    """
    Admin dataclass

    """
    regid: str
    id: str

@dataclass
class Tech:
    """
    Tech dataclass

    """
    regid: str
    id: str

@dataclass
class Billing:
    """
    Billing dataclass

    """
    regid: str
    id: str

@dataclass
class Registrant:
    """
    Registrant dataclass

    """
    regid: str
    id: str

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
@dataclass
class OrderList(JSONWizard):
    """
    Data dataclass

    """
    orders: list[OrderItem]


@dataclass
class OrderItem:
    """
    Order dataclass

    """
    id: int | str
    domain: str
    type: str
    status: str
    errorcode: int | str
    #lastupdate: datetime
    lastupdate: str
    message: str
    paid: int | str
    amount: float | str

@dataclass
class OrderInfo(JSONWizard):
    """
    Data dataclass

    """
    order: Order


@dataclass
class Order:
    """
    Order dataclass

    """
    id: int | str
    domain: str
    type: str
    status: str
    errorcode: int | str
    #lastupdate: datetime
    lastupdate: str
    message: str
    paid: int | str
    amount: float | str

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
