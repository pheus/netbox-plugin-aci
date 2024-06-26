# SPDX-FileCopyrightText: 2024 Martin Hauser
#
# SPDX-License-Identifier: GPL-3.0-or-later

from netbox.search import SearchIndex, register_search

from .models.tenant_app_profiles import ACIAppProfile, ACIEndpointGroup
from .models.tenant_networks import (
    ACIVRF,
    ACIBridgeDomain,
    ACIBridgeDomainSubnet,
)
from .models.tenants import ACITenant


@register_search
class ACITenantIndex(SearchIndex):
    """NetBox search definition for ACI Tenant model."""

    model = ACITenant

    fields: tuple = (
        ("name", 100),
        ("name_alias", 300),
        ("description", 500),
    )
    display_attrs: tuple = (
        "name",
        "name_alias",
        "description",
        "nb_tenant",
    )


@register_search
class ACIAppProfileIndex(SearchIndex):
    """NetBox search definition for ACI Application Profile model."""

    model = ACIAppProfile

    fields: tuple = (
        ("name", 100),
        ("name_alias", 300),
        ("description", 500),
    )
    display_attrs: tuple = (
        "name",
        "name_alias",
        "description",
        "aci_tenant",
        "nb_tenant",
    )


@register_search
class ACIVRFIndex(SearchIndex):
    """NetBox search definition for ACI VRF model."""

    model = ACIVRF

    fields: tuple = (
        ("name", 100),
        ("name_alias", 300),
        ("description", 500),
    )
    display_attrs: tuple = (
        "name",
        "alias",
        "description",
        "aci_tenant",
        "nb_tenant",
        "nb_vrf",
    )


@register_search
class ACIBridgeDomainIndex(SearchIndex):
    """NetBox search definition for ACI Bridge Domain model."""

    model = ACIBridgeDomain

    fields: tuple = (
        ("name", 100),
        ("name_alias", 300),
        ("description", 500),
    )
    display_attrs: tuple = (
        "name",
        "name_alias",
        "description",
        "aci_vrf",
        "nb_tenant",
    )


@register_search
class ACIBridgeDomainSubnetIndex(SearchIndex):
    """NetBox search definition for ACI Bridge Domain Subnet model."""

    model = ACIBridgeDomainSubnet

    fields: tuple = (
        ("name", 100),
        ("name_alias", 300),
        ("description", 500),
    )
    display_attrs: tuple = (
        "name",
        "name_alias",
        "description",
        "aci_bridge_domain",
        "gateway_ip_address",
        "nb_tenant",
    )


@register_search
class ACIEndpointGroupIndex(SearchIndex):
    """NetBox search definition for ACI Endpoint Group model."""

    model = ACIEndpointGroup

    fields: tuple = (
        ("name", 100),
        ("name_alias", 300),
        ("description", 500),
    )
    display_attrs: tuple = (
        "name",
        "name_alias",
        "description",
        "aci_app_profile",
        "aci_bridge_domain",
        "nb_tenant",
    )
