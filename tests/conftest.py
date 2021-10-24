import pytest

from demo_app.demo_app import Demo


@pytest.fixture
def demo_fixture():
    "Provides a Demo object"
    return Demo()