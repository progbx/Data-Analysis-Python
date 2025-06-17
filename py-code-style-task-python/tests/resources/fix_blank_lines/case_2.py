class A:
    def __init__(self, a):
        self.a = a
    def get_a(self):
        return self.a
class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def get_sum(self):
        return self.a + self.b