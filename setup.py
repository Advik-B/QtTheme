import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="QtTheme",
    version="1.0.0",
    author="Advik",
    author_email="advik.b@gmail.com",
    description="Themes for Qt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Advik-B/QtTheme",
    project_urls={
        "Bug Tracker": "https://github.com/Advik-B/QtTheme/issues/new/choose",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": ".", "themes": "themes"},
    python_requires=">=3.9",
    requires=["QtPy"],
)
