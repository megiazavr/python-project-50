install:
    poetry install

build:
    poetry build

publish:
    poetry publish --dry-run

linter:
    poetry run flake8 gendiff

tests:
    poetry run pytest -vv

make test-coverage:
    poetry run pytest --cov=gendiff --cov-report xml tests
