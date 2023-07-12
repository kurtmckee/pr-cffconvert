import os
from tests.contracts.endnote_object import Contract
from cffconvert import Citation
from cffconvert.behavior_1_2_x.endnote_object import EndnoteObject


def endnote_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return EndnoteObject(citation.cffobj, initialize_empty=True)


class TestEndnoteObject(Contract):

    def test_as_string(self):
        actual_endnote = endnote_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), "endnote.enw")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_endnote = f.read()
        assert actual_endnote == expected_endnote

    def test_author(self):
        assert endnote_object().add_author().author == '%A Test author\n'

    def test_check_cffobj(self):
        endnote_object().check_cffobj()
        # doesn't need an assert

    def test_doi(self):
        assert endnote_object().add_doi().doi == '%R 10.0000/from-identifiers\n'

    def test_keyword(self):
        assert endnote_object().add_keyword().keyword is None

    def test_name(self):
        assert endnote_object().add_name().name == '%T Test title\n'

    def test_url(self):
        assert endnote_object().add_url().url is None

    def test_year(self):
        assert endnote_object().add_year().year is None
