import pytest

from src.matrix import Matrix


@pytest.fixture
def test_matrix():
    return Matrix(
        [1, 2, 3],
        [4, 5, 6]
    )


class TestMatrix:

    def test_count(self, test_matrix):
        assert test_matrix.cols_count == 3
        assert test_matrix.rows_count == 2

    def test_values(self, test_matrix):
        assert test_matrix.min == 1
        assert test_matrix.max == 6
        assert test_matrix.sum == 21
