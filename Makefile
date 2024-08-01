install:
	poetry install

brain-games:
	poetry run brain-games

brain_evens:
	poetry run brain_evens

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 brain_games