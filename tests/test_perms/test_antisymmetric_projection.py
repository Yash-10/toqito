"""Tests for antisymmetric_projection function."""
import unittest
import numpy as np

from toqito.perms import antisymmetric_projection


class TestAntisymmetricProjection(unittest.TestCase):

    """Unit test for antisymmetric_projection."""

    def test_antisymmetric_projection_d_2_p_1(self):
        """Dimension is 2 and p is equal to 1."""
        res = antisymmetric_projection(2, 1).todense()
        expected_res = np.array([[1, 0], [0, 1]])

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_antisymmetric_projection_p_larger_than_d(self):
        """The `p` value is greater than the dimension `d`."""
        res = antisymmetric_projection(2, 3).todense()
        expected_res = np.zeros((8, 8))

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_antisymmetric_projection_2(self):
        """The dimension is 2."""
        res = antisymmetric_projection(2).todense()
        expected_res = np.array(
            [[0, 0, 0, 0], [0, 0.5, -0.5, 0], [0, -0.5, 0.5, 0], [0, 0, 0, 0]]
        )

        bool_mat = np.isclose(res, expected_res)
        self.assertEqual(np.all(bool_mat), True)

    def test_antisymmetric_projection_3_3_true(self):
        """The `dim` is 3, the `p` is 3, and `partial` is True."""
        res = antisymmetric_projection(3, 3, True).todense()
        self.assertEqual(np.isclose(res[5].item(), -0.40824829), True)


if __name__ == "__main__":
    unittest.main()
