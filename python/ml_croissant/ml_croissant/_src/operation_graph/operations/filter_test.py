"""filter_test module."""

from ml_croissant._src.operation_graph.operations.filter import Filter
from ml_croissant._src.tests.nodes import empty_file_set


def test_str_representation():
    operation = Filter(node=empty_file_set)
    assert str(operation) == "Filter(file_set_name)"
