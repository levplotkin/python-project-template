from src.app import Demo


def test_something(self):
    demo = Demo()
    demo.setVal("val")
    assert "val" == demo.getVal()
