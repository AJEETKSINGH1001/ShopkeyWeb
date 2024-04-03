import pytest

# This fixture is used to setup before any test runs.
def pytest_configure(config):
    config.option.verbose = True

# This fixture is used to do some teardown after all tests are run.
def pytest_unconfigure(config):
    pass
