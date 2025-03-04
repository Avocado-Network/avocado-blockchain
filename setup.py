from setuptools import setup

dependencies = [
    "blspy==1.0.2",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.3",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the avocado processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==7.1.2",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="avocado-blockchain",
    author="Avocado Network",
    author_email="TBD",
    description="avocado blockchain full node, farmer, timelord, and wallet.",
    url="https://avocadonetwork.net/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="avocado blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "avocado",
        "avocado.cmds",
        "avocado.clvm",
        "avocado.consensus",
        "avocado.daemon",
        "avocado.full_node",
        "avocado.timelord",
        "avocado.farmer",
        "avocado.harvester",
        "avocado.introducer",
        "avocado.plotting",
        "avocado.pools",
        "avocado.protocols",
        "avocado.rpc",
        "avocado.server",
        "avocado.simulator",
        "avocado.types.blockchain_format",
        "avocado.types",
        "avocado.util",
        "avocado.wallet",
        "avocado.wallet.puzzles",
        "avocado.wallet.rl_wallet",
        "avocado.wallet.cc_wallet",
        "avocado.wallet.did_wallet",
        "avocado.wallet.settings",
        "avocado.wallet.trading",
        "avocado.wallet.util",
        "avocado.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "avocado = avocado.cmds.avocado:main",
            "avocado_wallet = avocado.server.start_wallet:main",
            "avocado_full_node = avocado.server.start_full_node:main",
            "avocado_harvester = avocado.server.start_harvester:main",
            "avocado_farmer = avocado.server.start_farmer:main",
            "avocado_introducer = avocado.server.start_introducer:main",
            "avocado_timelord = avocado.server.start_timelord:main",
            "avocado_timelord_launcher = avocado.timelord.timelord_launcher:main",
            "avocado_full_node_simulator = avocado.simulator.start_simulator:main",
        ]
    },
    package_data={
        "avocado": ["pyinstaller.spec"],
        "avocado.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "avocado.util": ["initial-*.yaml", "english.txt"],
        "avocado.ssl": ["avocado_ca.crt", "avocado_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
