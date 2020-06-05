from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()


setup_args = dict(
    name='pickles',
    version='0.1',
    description='A wrapper around the pickle package',
    long_description_content_type="text/markdown",
    long_description=README,
    license='Apache',
    packages=find_packages(),
    author='Nadav Borenstein',
    keywords=['pickle', 'pickles'],
    url='https://github.com/nadavborenstein/Pickles',
    download_url='https://pypi.org/project/pickles/'
)

install_requires = [

]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)