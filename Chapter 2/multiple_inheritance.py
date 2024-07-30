""" Module for learning about multiple inheritance. """

class A:
    """
    Example class.
    """
    def __init__(self):
        super().__init__()
        self.foo = 'foo'
        self.name = 'Class A'


class B:
    """
    Example class.
    """
    def __init__(self):
        super().__init__()
        self.bar = 'bar'
        self.name = 'Class B'


class C(A, B):
    """
    Example class.
    """
    def __init__(self):
        super().__init__()


    def show_props(self):
        """
        Showing specific properties.
        """
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
# In this case, when we call the name, we can see that both classes has
# the name attribute, so, in this case, the class will inherit from the
# first class that we passed, for this case, will be the A class.
c.show_props()
# We can see the order in which the hierarchy will  be if we use the mro
# property (Method Resolution Object)
print(C.__mro__)
