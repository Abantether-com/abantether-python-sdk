from setuptools import setup

version = "0.1.2"

setup(
    name="abantether-python-sdk",
    packages=["abantether_python_sdk"],
    license="MIT",
    version=version,
    author="abantether",
    author_email="tech@abantether.com",
    description="A python sdk to trade easily in abantether.com",
    long_description_content_type="text/markdown",
    long_description=open("README.md", "rt").read(),
    url="https://github.com/Abantether-com/abantether-python-sdk/",
    download_url=f"https://github.com/imanmousaei/coinexpy/archive/refs/tags/v{version}.tar.gz",
    keywords=[
        "abantether",
        "sdk",
        "python",
        "api",
        "exchange",
        "wrapper",
        "trade",
        "crypto",
        "bitcoin",
    ],
    install_requires=["requests==2.31.0"],
    classifiers=[
        # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
)
