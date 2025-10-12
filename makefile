.PHONY: clean build publish

build: clean
	python -m pip install --upgrade --quiet build twine
	python -m build

publish: build
	python -m twine check dist/*
	python -m twine upload dist/*

clean:
	rm -r build dist *.egg-info || true
