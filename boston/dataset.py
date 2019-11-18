""" Module providing a dataset class with useful functionality for Bokeh """

from sklearn.datasets import load_boston
from bokeh.models import ColumnDataSource

FEATURE_INFO = {
    "CRIM": "per capita crime rate by town",
    "ZN": "proportion of residential land zoned for lots over 25,000 sq.ft.",
    "INDUS": "proportion of non-retail business acres per town",
    "CHAS": "Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)",
    "NOX": "nitric oxides concentration (parts per 10 million)",
    "RM": "average number of rooms per dwelling",
    "AGE": "proportion of owner-occupied units built prior to 1940",
    "DIS": "weighted distances to five Boston employment centres",
    "RAD": "index of accessibility to radial highways",
    "TAX": "full-value property-tax rate per $10,000",
    "PTRATIO": "pupil-teacher ratio by town",
    "B": "1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town",
    "LSTAT": "%% lower status of the population",
}


class BostonDataset:
    """ Encapsulates interactive Bokeh datasources for the Boston dataset """

    def __init__(self):
        # pylint: disable=no-member
        batch = load_boston()
        self._feature_names = batch.feature_names.tolist()
        self._features = batch.data
        self._prices = batch.target
        self._x_feature = self._feature_names[0]
        self._y_feature = self._feature_names[1]
        self._source = ColumnDataSource()
        self._update()

    def _update(self):
        x_index = self._feature_names.index(self._x_feature)
        y_index = self._feature_names.index(self._y_feature)
        x = self._features[:, x_index]
        y = self._features[:, y_index]
        self._source.data = dict(x=x, y=y, price=self._prices)

    @property
    def source(self):
        """ The data sources for the different targets in the Boston dataset """
        return self._source

    @property
    def prices(self):
        """ The target house prices """
        return self._prices

    @property
    def title(self):
        """ The current plot title given the x and y features """
        return "{} x {}".format(self._x_feature, self._y_feature)

    @property
    def num_features(self):
        """ The number of feature dimensions """
        return len(self._feature_names)

    @property
    def feature_names(self):
        """ The names of the features """
        return self._feature_names

    @property
    def x_feature(self):
        """ The current x-axis feature """
        return self._x_feature

    @property
    def x_title(self):
        """ The readable title for the x-axis """
        return FEATURE_INFO[self._x_feature]

    @x_feature.setter
    def x_feature(self, feature):
        """ Used to set the current x-axis feature.

        Description:
            This method updates the data sources to reflect the new feature.

        Args:
            feature -- the feature name
        """
        if feature != self._x_feature:
            self._x_feature = feature
            self._update()

    @property
    def y_feature(self):
        """ The current y-axis feature """
        return self._y_feature

    @property
    def y_title(self):
        """ The readable title for the y-axis """
        return FEATURE_INFO[self._y_feature]

    @y_feature.setter
    def y_feature(self, feature):
        """ Used to set the current y-axis feature.

        Description:
            This method updates the data sources to reflect the new feature.

        Args:
            feature -- the feature name
        """
        if feature != self._y_feature:
            self._y_feature = feature
            self._update()

    @property
    def name(self):
        """ The correct name for the plot """
        return "Boston Dataset"
