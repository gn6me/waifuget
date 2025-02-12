from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name = 'waifuimgcli',
    version = '1.0',
    author = 'shiro-ko',
    author_email = 'thegn6me@gmail.com',
    license = 'GNU GPLv3',
    description = 'CLI tool to get and display anime art in the terminal',
    long_desription = long_description,
    long_description_content_type = "text/markdown",
    url = '',
    py_modules = ['waifu', 'app'],
    packages = find_packages(),
    install_requires = [requirements],
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    entry_points = '''
        [console_scripts]
        waifu=waifu:cli
    '''
)
