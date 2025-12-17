from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pack-id-tool",
    version="1.0.1",
    author="Cribl",
    author_email="support@cribl.io",
    description="A CLI tool to modify Cribl pack IDs in .crbl files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gcribl/pack-cli",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "pack-id=pack_id_tool.cli:main",
        ],
    },
)

