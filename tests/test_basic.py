"""Basic tests for awiesm.pycmor_helpers."""

import awiesm.pycmor_helpers


def test_version():
    """Test that version is defined."""
    assert hasattr(awiesm.pycmor_helpers, "__version__")
    assert isinstance(awiesm.pycmor_helpers.__version__, str)
