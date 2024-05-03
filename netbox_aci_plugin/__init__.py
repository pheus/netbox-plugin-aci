"""Top-level package for NetBox ACI Plugin."""

__author__ = """Martin Hauser"""
__email__ = "git@pheus.dev"
__version__ = "0.0.1"


from netbox.plugins import PluginConfig


class ACIConfig(PluginConfig):
    name = "netbox_aci_plugin"
    verbose_name = "NetBox ACI Plugin"
    description = "NetBox plugin for documenting Cisco ACI specific objects."
    version = __version__
    author = __author__
    author_email = __email__
    base_url = "aci"
    min_version = "4.0.0-beta2"
    max_version = "4.0.99"


config = ACIConfig