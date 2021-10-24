import pytest


def test_something(demo_fixture):
    demo_fixture.set_val("val")
    assert "val" == demo_fixture.get_val()


def test_validation_raises_error(demo_fixture):
    with pytest.raises(SystemError):
        demo_fixture.validate()


@pytest.mark.e2e
def test_e2e(demo_fixture):
    pass


@pytest.mark.skip("not implemented")
def test_not_implemented(demo_fixture):
    pass
