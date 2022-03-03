from setuptools import setup, find_packages

package_metadata = {
    'name': 'hello-world',
    'version': '0.1.2',
    'description': 'Testing out git actions with gcloud registry',
    'long_description': 'Testing out git actions with gcloud registry',
    'url': 'https://github.com/rhimmelbauer/django-user-notifications/',
    'author': 'Roberto Himmelbauer',
    'author_email': 'robertoh89@gmail.com',
    'license': 'MIT license',
    'classifiers': [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
    ],
    'keywords': ['python', 'gcloud'],
}

setup(
    packages=find_packages(include=['hello_world', 'hello_world.*']),
    include_package_data=True,
    **package_metadata
)