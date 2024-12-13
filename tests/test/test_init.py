"""Package __init__.py tests.

make test T=test_init.py
"""
from datetime import datetime
from . import TestBase


class TestInit(TestBase):
    """Infotech __init__.py."""

    def test_it_date(self):
        """Check it_date function."""
        from pipeline_gazprom_infotech import it_date

        assert it_date(datetime(2024, 1, 9)) == "09.01.2024"

    def test_codes(self):
        """Check IT codes."""
        from pipeline_gazprom_infotech.codes import NAME

        assert len(NAME) > 1
