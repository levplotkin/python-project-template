class Demo:
    def __init__(self):
        self.val = "default-value"

    def get_val(self):
        return self.val

    def set_val(self, param):
        self.val = param


demo = Demo()
demo.set_val("demo ready")
print(demo.get_val())
