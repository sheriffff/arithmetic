from restful_analytics.models import predict
import pytest
import numpy as np 


def test_predict_0():
    assert predict(0.0) == pytest.approx(0.0166640027622)


def test_predict_1():
    assert np.all(
        np.isclose(predict(np.array([0, 0, 0])),
                   np.array([0.01666400, 0.01666400, 0.01666400]))
    )