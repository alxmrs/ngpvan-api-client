import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="ngpvan-api-client",
    version="0.0.0",
    description="A client library for accessing VAN CRM",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.7, <4",
    install_requires=["httpx >= 0.15.0, < 0.24.0", "attrs >= 21.3.0", "python-dateutil >= 2.8.0, < 3"],
    package_data={"ngpvan_api_client": ["py.typed"]},
)
