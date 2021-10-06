class Matrix:

    def __init__(self, h, w, values):
        self.values = (
            [[int(values(i, j)) for j in range(w)] for i in range(h)]
            if callable(values) else values
        )

    def __repr__(self):
        lmax = [len(str(max(v))) for v in self.rotated()]
        return '\n'.join(
            ' '.join(str(y).center(lmax[c] + 1) for c, y in enumerate(x))
            for x in self.values
        )

    def __iter__(self):
        return (w for v in self.values for w in v)

    def __add__(self, other):
        if len(self) != len(other) or len(self.values) != len(other.values):
            raise ValueError("Les matrices sont de tailles différentes")

        width = self.width
        self.values = [[v + w] for v, w in zip(self, other)]
        self.reform(width)
        return self

    def __sub__(self, other):
        if len(self) != len(other) or len(self.values) != len(other.values):
            raise ValueError("Les matrices sont de tailles différentes")

        width = self.width
        self.values = [[v - w] for v, w in zip(self, other)]
        self.reform(width)
        return self

    def __eq__(self, other):
        return all(x == y for x, y in zip(self, other))

    def __len__(self):
        return len([x for x in self])

    @property
    def width(self):
        return len(list(self.rotated()))

    @property
    def height(self):
        return self.values

    def reform(self, w):
        if not (len(self) / w).is_integer():
            raise ValueError(
                "La nouvelle matrice doit avoir "
                "la même longueur que l' ancienne !"
            )

        values = [x for x in self]
        self.values = [values[i:i + w] for i in range(0, len(self), w)]

    def rotated(self):
        return iter(zip(*self.values))


def main():
    m1 = Matrix(5, 5, lambda i, j: i == j)
    m2 = Matrix(5, 5, lambda *_: 10)
    print(m1 - m2)


if __name__ == '__main__':
    main()
