# SPDX-FileCopyrightText: 2024 Martin Hauser
#
# SPDX-License-Identifier: GPL-3.0-or-later

from netbox.api.routers import NetBoxRouter

from . import views

app_name = "netbox_aci_plugin"
router = NetBoxRouter()
router.register("tenants", views.ACITenantListViewSet)
router.register("app-profiles", views.ACIAppProfileListViewSet)
router.register("bridge-domains", views.ACIBridgeDomainListViewSet)
router.register(
    "bridge-domain-subnets", views.ACIBridgeDomainSubnetListViewSet
)
router.register("endpointgroups", views.ACIEndpointGroupListViewSet)
router.register("vrfs", views.ACIVRFListViewSet)

urlpatterns = router.urls
