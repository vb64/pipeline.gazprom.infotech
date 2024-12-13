"""Module tpo.py tests.

make test T=test_tpo.py
"""
from . import TestBase


class TestTpo(TestBase):
    """Infotech tpo.py."""

    def test_new(self):
        """Check new instance."""
        from pipeline_gazprom_infotech.tpo import Infotech, Inspect

        xml = Infotech()
        assert xml.root is not None

        fname = self.build("inf.xml")
        xml.save(fname)
        assert Inspect.Title in open(fname, 'r', encoding="windows-1251").read()

    def test_set_sdt(self):
        """Check set_sdt method."""
        from pipeline_gazprom_infotech.tpo import Infotech

        xml = Infotech()
        route = xml.add_route("1", 100, "xxx.dwg")
        item = xml.add_element(route, "1.1", "XXX")
        xml.set_sdt(item, None, None, None, None, None, None)

    def test_add_defect(self):
        """Check add_defect method."""
        from pipeline_gazprom_infotech.tpo import Infotech

        xml = Infotech()
        route = xml.add_route("1", 100, "xxx.dwg")
        assert xml.add_defect(
          route, "1", "1.1", "xxx", None, None, None, None, None, None, None, None
        ) is not None
