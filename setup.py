import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zh-hans-hant",
    version="0.0.1",
    author="Emojipypi",
    author_email = "contact-forward@thost3.de",
    description="Convert Chinese strings between variants, using Chinese Wikipedia's convertion database",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Emojigit/zh-hans-hant",
    project_urls={
        "Bug Tracker": "https://github.com/Emojigit/zh-hans-hant/issues",
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Other Audience",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Internationalization",
    ],
    # package_dir={"mwng": "mwng"},
    packages=["zhst"],
    python_requires=">=3.6",
    install_requires=["requests"]
)
