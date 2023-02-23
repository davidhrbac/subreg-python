from __future__ import annotations
from dataclasses import dataclass
from dataclass_wizard import JSONWizard

# General dataclasses BEGIN
@dataclass
class ErrorResponse(JSONWizard):
    """
    Data dataclass

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
    Data dataclass

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
    Data dataclass

    """
    contacts: list[ContactItem]
    count: int

@dataclass
class ContactItem:
    """
    Contact dataclass

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
    Data dataclass

    """
    contactid: str

# Contacts API dataclasses END

# Hosts API dataclasses BEGIN
# Hosts API dataclasses END

# Orders API dataclasses BEGIN
# Orders API dataclasses END

# DNS API dataclasses BEGIN
# DNS API dataclasses END

# Resellers API dataclasses BEGIN
# Resellers API dataclasses END
