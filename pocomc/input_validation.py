import numpy as np


def assert_2d(x: np.ndarray):
    if len(x.shape) != 2:
        raise ValueError(f"Input should have 2 dimensions, but got {len(x.shape)}")


def assert_equal_shape(x: np.ndarray,
                       y: np.ndarray):
    if x.shape != y.shape:
        raise ValueError(f"Inputs should have equal shape, but got {x.shape} and {y.shape}")


def assert_within_interval(x: np.ndarray,
                           left: float,
                           right: float,
                           left_open: bool = False,
                           right_open: bool = False):
    if left_open and right_open:
        condition = (left < x < right)
        interval_string = f'({left}, {right})'
    elif left_open and not right_open:
        condition = (left < x <= right)
        interval_string = f'({left}, {right}]'
    elif not left_open and right_open:
        condition = (left <= x < right)
        interval_string = f'[{left}, {right})'
    else:
        condition = (left <= x <= right)
        interval_string = f'[{left}, {right}]'

    if not np.all(condition):
        x_min = np.min(x)
        x_max = np.max(x)
        raise ValueError(f"Expected input to be within interval {interval_string}, "
                         f"but got minimum = {x_min} and maximum = {x_max}")
