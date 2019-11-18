""" Tests for the Iris dataset """

# pylint: disable=redefined-outer-name

import pytest
import numpy as np

from iris import IrisDataset


@pytest.fixture(scope="module")
def iris():
    """ Module fixture for the IrisDataset class """
    return IrisDataset()


def test_features(iris):
    """ Test that the dataset exposes features correctly """
    assert iris.num_features == 4
    assert iris.feature_names == [
        "sepal length (cm)",
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]


def test_targets(iris):
    """ Test that the dataset exposes targets correctly """
    assert iris.num_targets == 3
    np.testing.assert_array_equal(
        iris.target_names, ["setosa", "versicolor", "virginica"]
    )


@pytest.mark.parametrize(
    "name, x_feature, y_feature, x_vals, y_vals",
    [
        ("setosa", "sepal length (cm)", "sepal width (cm)", [5.1, 4.9], [3.5, 3.0]),
        ("versicolor", "sepal length (cm)", "sepal width (cm)", [7, 6.4], [3.2, 3.2]),
        ("virginica", "sepal length (cm)", "sepal width (cm)", [6.3, 5.8], [3.3, 2.7]),
        ("setosa", "petal length (cm)", "petal width (cm)", [1.4, 1.4], [0.2, 0.2]),
        ("versicolor", "petal length (cm)", "petal width (cm)", [4.7, 4.5], [1.4, 1.5]),
        ("virginica", "petal length (cm)", "petal width (cm)", [6, 5.1], [2.5, 1.9]),
    ],
)
def test_feature_values(iris, name, x_feature, y_feature, x_vals, y_vals):
    """ Test that the setting of feature values works as expected """
    iris.x_feature = x_feature
    iris.y_feature = y_feature
    assert iris.title == "{} x {}".format(x_feature, y_feature)
    data = iris.sources[name].data
    np.testing.assert_array_almost_equal(data["x"][:2], x_vals)
    np.testing.assert_array_almost_equal(data["y"][:2], y_vals)
