from setuptools import setup


VERSION = "0.0.1"


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="sigsci_site_manager",
    version=VERSION,
    author="Turner ISO",
    author_email="isodev@turner.com",
    description="Utility for managing Signal Sciences sites",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=("https://github.com/turnerlabs/sigsci_site_manager"),
    packages=['sigsci_site_manager'],
    setup_requires=[
        'pytest-runner'
    ],
    install_requires=[
        'pysigsci>=2.0.3'
    ],
    tests_require=[
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'sigsci_site_manager=sigsci_site_manager.site_manager:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "Environment :: Console",
        "Topic :: Security"
    ]
)