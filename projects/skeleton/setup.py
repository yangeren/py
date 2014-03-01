try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

coding = {
	'description': 'TheFirstPython',
	'author': 'Wanghan',
	'url': 'https://github.com/yangeren/py',
	'download_url': 'https://github.com/yangeren',
	'author_email':'xiaoyaoyangeren@163.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages':['NAME'],
	'scripts': [],
	'name': 'projectname'
}

setup(**config)