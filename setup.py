from setuptools import setup, find_packages
 
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name                = 'tistory-uploader',
    version             = '0.11',
    description         = 'markdown file uploader for tistory',
    long_description    = long_description,
    long_description_content_type   =   "text/markdown",
    author              = 'momentjin',
    author_email        = 'momentjin@gmail.com',
    url                 = 'https://github.com/momentjin/tistory-uploader',
    download_url        = 'https://github.com/momentjin/tistory-uploader/archive/master.zip',
    install_requires    =  [],
    packages            = find_packages(exclude = []),
    keywords            = ['tistory', 'markdown'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)