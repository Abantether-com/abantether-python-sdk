# Publish a new version to pypi
publish:
	pip install twine
	rm -rf dist abantether_python_sdk.egg-info
	python setup.py sdist
	python -m twine upload dist/*
