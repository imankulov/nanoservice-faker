from typing import Optional

from faker import Faker, config
from fastapi import FastAPI

from nanoservice_faker.custom_types import Locale, Method

app = FastAPI()


@app.get("/gen/{method}")
def gen(
    method: Method,
    count: int = 10,
    locale: Locale = config.DEFAULT_LOCALE,
    seed: Optional[str] = None,
):
    fake = Faker(locale=locale)
    if seed is not None:
        Faker.seed(seed)
    return [fake.format(method) for _ in range(count)]
