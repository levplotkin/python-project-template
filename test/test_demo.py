import pytest

from src.demo_app import Demo


@pytest.fixture
def demo_fixture():
    "Provides a Demo object"
    return Demo()


def test_something(demo_fixture):
    demo_fixture.set_val("val")
    assert "val" == demo_fixture.get_val()


def test_validation_raises_error(demo_fixture):
    with pytest.raises(SystemError):
        demo_fixture.validate()
