import os
import pytest


@pytest.fixture
def os_environ():
    """
    Copy os.environ, and restore it after the test runs.  Use this
    whenever you expect code to edit environment variables.
    """

    old_env = os.environ.copy()
    yield
    os.environ = old_env