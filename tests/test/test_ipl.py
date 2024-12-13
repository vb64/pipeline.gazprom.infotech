"""Module ipl.py tests.

make test T=test_ipl.py
"""
from . import TestBase


class TestIpl(TestBase):
    """Infotech ipl.py."""

    def test_new(self):
        """Check new IPL instance."""
        from pipeline_gazprom_infotech.ipl import Infotech, Inspect, PigPass, Weld, LineObj, Defect

        xml = Infotech()
        assert xml.root is not None

        assert xml.set_ipl({Inspect.Pipeline: "xxx"}) is None
        assert xml.add_pigpass({PigPass.TypeId: "111"}) is not None
        assert xml.add_weld({Weld.TypeId: "222"}) is not None
        assert xml.add_lineobj({LineObj.TypeId: "333"}) is not None
        assert xml.add_defekt({Defect.TypeId: "444"}) is not None

        fname = self.build("ipl_empty.xml")
        xml.save(fname)
        text = open(fname, 'r', encoding="windows-1251").read()
        assert Inspect.Title in text
        assert PigPass.Title in text
        assert Weld.Title in text
        assert LineObj.Title in text
        assert Defect.Title in text
