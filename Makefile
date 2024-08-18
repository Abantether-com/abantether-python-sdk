# Publish a new version to pypi
publish:
    pip install twine
    python setup.py sdist
    python -m twine upload dist/*
