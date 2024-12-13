"""Module tpo.py tests.

make test T=test_tpo.py
"""
from datetime import datetime
import pytest
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

    def test_get_abc(self):
        """Check get_abc function."""
        from pipeline_gazprom_infotech.tpo import get_abc

        assert "критический" in get_abc('A')
        assert "ремонт" in get_abc('B')
        assert "малозначительный" in get_abc('')

    def test_set_titul(self):
        """Check set_titul method."""
        from pipeline_gazprom_infotech.tpo import Infotech
        from pipeline_gazprom_infotech import InfotechError
        from pipeline_gazprom_infotech.codes.pypeline import PIPELINE_BY_NAMES

        xml = Infotech()

        with pytest.raises(InfotechError) as err:
            xml.set_titul("wrong_pipeline_name", None, None, "", "", "", "", {})
        assert 'не найден в словаре' in str(err.value)

        pipeline_name = list(PIPELINE_BY_NAMES.keys())[0]
        with pytest.raises(InfotechError) as err:
            xml.set_titul(pipeline_name, None, None, "", "", "", "", {})
        assert 'дата начала' in str(err.value)
        assert 'дата окончания' in str(err.value)

        now = datetime.now()
        assert xml.set_titul(pipeline_name, now, now, "", "", "", "", {}) is None
