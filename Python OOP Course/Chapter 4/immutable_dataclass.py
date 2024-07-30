""" Learning script. """

from dataclasses import dataclass

# TODO: The frozen in the dataclass decorator argument makes the class
# immutable
@dataclass(frozen = True)
class ImmutableClass:
    """
    Immutables class.
    """
    value_1: str = 'Value 1'
    value_2: int = 0

    def test_func(self, new_value):
        """
        Function for testing the changing values.
        """
        self.value_2 = new_value

obj = ImmutableClass()
print(obj.value_1)

# TODO: Attempting to change the value of an immutable class throws an
# exception
# obj.value_1 = 'Another value'
# print(obj.value_1)

# TODO: Even functions within the class can't change anything
obj.test_func(20)
