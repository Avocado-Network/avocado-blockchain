from typing import KeysView, Generator

SERVICES_FOR_GROUP = {
    "all": "avocado_harvester avocado_timelord_launcher avocado_timelord avocado_farmer avocado_full_node avocado_wallet".split(),
    "node": "avocado_full_node".split(),
    "harvester": "avocado_harvester".split(),
    "farmer": "avocado_harvester avocado_farmer avocado_full_node avocado_wallet".split(),
    "farmer-no-wallet": "avocado_harvester avocado_farmer avocado_full_node".split(),
    "farmer-only": "avocado_farmer".split(),
    "timelord": "avocado_timelord_launcher avocado_timelord avocado_full_node".split(),
    "timelord-only": "avocado_timelord".split(),
    "timelord-launcher-only": "avocado_timelord_launcher".split(),
    "wallet": "avocado_wallet avocado_full_node".split(),
    "wallet-only": "avocado_wallet".split(),
    "introducer": "avocado_introducer".split(),
    "simulator": "avocado_full_node_simulator".split(),
}


def all_groups() -> KeysView[str]:
    return SERVICES_FOR_GROUP.keys()


def services_for_groups(groups) -> Generator[str, None, None]:
    for group in groups:
        for service in SERVICES_FOR_GROUP[group]:
            yield service


def validate_service(service: str) -> bool:
    return any(service in _ for _ in SERVICES_FOR_GROUP.values())
