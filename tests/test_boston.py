""" Tests for the Boston house prices dataset """

# pylint: disable=redefined-outer-name

import pytest
import numpy as np

from boston import BostonDataset


@pytest.fixture(scope="module")
def boston():
    """ Module fixture for the BostonDataset class """
    return BostonDataset()


def test_features(boston):
    """ Test that the dataset exposes features correctly """
    assert boston.num_features == 13
    assert boston.feature_names == [
        "CRIM",
        "ZN",
        "INDUS",
        "CHAS",
        "NOX",
        "RM",
        "AGE",
        "DIS",
        "RAD",
        "TAX",
        "PTRATIO",
        "B",
        "LSTAT",
    ]


@pytest.mark.parametrize(
    "x_feature, y_feature, x_vals, y_vals",
    [
        ("CRIM", "ZN", [0.00632, 0.02731], [18.0, 0.0]),
        ("INDUS", "CHAS", [2.31, 7.07], [0.0, 0.0]),
        ("NOX", "RM", [0.538, 0.469], [6.575, 6.421]),
        ("AGE", "DIS", [65.2, 78.9], [4.09, 4.9671]),
        ("RAD", "TAX", [1.0, 2.0], [296.0, 242.0]),
        ("PTRATIO", "B", [15.3, 17.8], [396.9, 396.9]),
        ("B", "CRIM", [396.9, 396.9], [0.00632, 0.02731]),
    ],
)
def test_feature_values(boston, x_feature, y_feature, x_vals, y_vals):
    """ Test that the setting of feature values works as expected """
    boston.x_feature = x_feature
    boston.y_feature = y_feature
    assert boston.title == "{} x {}".format(x_feature, y_feature)
    data = boston.source.data
    np.testing.assert_array_almost_equal(data["x"][:2], x_vals)
    np.testing.assert_array_almost_equal(data["y"][:2], y_vals)
