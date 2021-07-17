import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="traiire-viewer", # Replace with your own username
    version="0.0.1",
    install_requires=[
        "requests",
        "pandas",
        "pyarrow",
        "pandasgui",
        "qtstylish",
    ],
    entry_points={
        'console_scripts': [
            'traiire-viewer=src.main:main'
        ],
    },
    author="MaaS Tech Japan K.K.",
    author_email="admin@maas.co.jp",
    description="TraIIRe Reader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaaSTechJapan/TraIIRe-Viewer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)