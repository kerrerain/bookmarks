import pytest
import faker

FAKE = faker.Faker()


@pytest.fixture
def valid_link():
    return {
        "name": FAKE.name(),
        "url": FAKE.url()
    }
