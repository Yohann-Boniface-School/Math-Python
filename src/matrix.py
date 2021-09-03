"""
The given exercise was to make a Matrix which we could retrieve
columns and rows number as well as min, max and sum.
"""

from typing import Any, Callable


class InvalidMatrix(Exception):

    def __init__(self):
        self.message = "Matrix arguments must be list of integers"


class Matrix(list):
    """A Single Depth Matrix Implementation class."""

    def __init__(self, *args):
        """Initialize a new Matrix with each argument as a line."""

        if not all(isinstance(line, list) for line in args):
            raise InvalidMatrix()

        # All values must by ints
        if not all(isinstance(item, int) for line in args for item in line):
            raise InvalidMatrix()

        super(Matrix, self).__init__(list(args))

    def __repr__(self, compact=False) -> str:
        """Return the matrix representation."""
        align = len(str(self.max))

        return f'<Matrix(%s)>' % ', '.join(
            '[%s]' % ', '.join(f'{n:={align}}' for n in line)
            for line in self
        )

    def __layer_map(self, func: Callable[[Any], Any]) -> int:
        """Inner method to apply function to lines then matrix."""
        try:
            return func(map(func, self))

        except ValueError:
            return 0

    @property
    def max(self) -> int:
        """Return the biggest element within this matrix."""
        return self.__layer_map(max)

    @property
    def min(self) -> int:
        """Return the minimal value within the matrix."""
        return self.__layer_map(min)

    @property
    def sum(self) -> int:
        return self.__layer_map(sum)

    @property
    def cols_count(self) -> int:
        """Return the number of columns in this matrix."""
        return len(self[0]) if self.rows_count else 0

    @property
    def rows_count(self) -> int:
        """Return the number of rows in this matrix."""
        return len(self)
