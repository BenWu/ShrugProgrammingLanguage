install:
	pip install -r requirements.dev.txt

test:
	nosetests --verbose --with-coverage --cover-package=shrug_lang

build:
	python setup.py sdist bdist_wheel

clean:
	rm -rf ./build ./dist ./shrug_lang.egg-info

upload:
	twine upload dist/*
