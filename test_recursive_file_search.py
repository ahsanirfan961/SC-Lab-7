import os
import tempfile
import pytest
from recursive_file_search import find_file 

@pytest.fixture
def setup_test_directory():
    """
    Creates a temporary directory structure for testing purposes.
    """
    with tempfile.TemporaryDirectory() as tmp_dir:
        os.mkdir(os.path.join(tmp_dir, "subdir1"))
        os.mkdir(os.path.join(tmp_dir, "subdir2"))
        os.mkdir(os.path.join(tmp_dir, "subdir1", "subsubdir1"))

        with open(os.path.join(tmp_dir, "testfile.txt"), "w") as f:
            f.write("This is a test file.")
        
        with open(os.path.join(tmp_dir, "subdir1", "testfile1.txt"), "w") as f:
            f.write("This is another test file.")
        
        with open(os.path.join(tmp_dir, "subdir2", "testfile2.txt"), "w") as f:
            f.write("This is yet another test file.")
        
        with open(os.path.join(tmp_dir, "subdir1", "subsubdir1", "targetfile.txt"), "w") as f:
            f.write("This is the target file.")

        yield tmp_dir  


def test_find_file_exists_in_root(setup_test_directory):
    tmp_dir = setup_test_directory
    result = find_file(tmp_dir, "testfile.txt")
    assert result == os.path.join(tmp_dir, "testfile.txt")


def test_find_file_exists_in_subdirectory(setup_test_directory):
    tmp_dir = setup_test_directory
    result = find_file(tmp_dir, "testfile1.txt")
    assert result == os.path.join(tmp_dir, "subdir1", "testfile1.txt")


def test_find_file_exists_in_nested_subdirectory(setup_test_directory):
    tmp_dir = setup_test_directory
    result = find_file(tmp_dir, "targetfile.txt")
    assert result == os.path.join(tmp_dir, "subdir1", "subsubdir1", "targetfile.txt")


def test_file_not_found(setup_test_directory):
    tmp_dir = setup_test_directory
    result = find_file(tmp_dir, "nonexistent.txt")
    assert result is None


def test_directory_does_not_exist():
    result = find_file("/non/existent/directory", "testfile.txt")
    assert result is None


def test_permission_denied(monkeypatch):
    def mock_os_listdir(path):
        raise PermissionError("Permission Denied")
    
    monkeypatch.setattr(os, "listdir", mock_os_listdir)
    result = find_file("/some/protected/directory", "testfile.txt")
    assert result is None
