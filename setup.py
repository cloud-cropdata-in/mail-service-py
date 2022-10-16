import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='mail-service-py',
    version='0.0.1',
    author='Rishabh Oswal',
    author_email='rishabh.oswal@cropdata.in',
    description='Mail Service Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/cloud-cropdata-in/mail-service-py.git',
    project_urls={
        "Bug Tracker": "https://github.com/cloud-cropdata-in/mail-service-py.git"
    },
    license='MIT',
    packages=['mail-service-py'],
    install_requires=['requests'],
)
