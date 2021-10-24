from src.demo_app import Demo


def test_something():
    demo = Demo()
    demo.set_val("val")
    assert "val" == demo.get_val()
