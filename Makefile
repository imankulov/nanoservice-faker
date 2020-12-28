web:
	poetry run uvicorn nanoservice_faker.app:app --reload

test:
	poetry run pytest tests
