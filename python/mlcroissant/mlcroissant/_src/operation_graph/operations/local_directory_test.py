"""local_directory_test module."""

from etils import epath

from mlcroissant._src.operation_graph.operations.local_directory import LocalDirectory
from mlcroissant._src.tests.nodes import empty_file_set


def test_str_representation():
    operation = LocalDirectory(node=empty_file_set, folder=epath.Path("/foo/bar"))
    assert str(operation) == "LocalDirectory(file_set_name)"
