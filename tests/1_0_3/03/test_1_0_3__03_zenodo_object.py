import os
from tests.contracts.zenodo_object import Contract
from cffconvert import Citation
from cffconvert.behavior_1_0_x.zenodo_object import ZenodoObject


def zenodo_object():
    fixture = os.path.join(os.path.dirname(__file__), "CITATION.cff")
    with open(fixture, "rt", encoding="utf-8") as f:
        cffstr = f.read()
        citation = Citation(cffstr)
        return ZenodoObject(citation.cffobj, initialize_empty=True)


class TestZenodoObject(Contract):

    def test_as_string(self):
        actual_zenodo = zenodo_object().add_all().as_string()
        fixture = os.path.join(os.path.dirname(__file__), ".zenodo.json")
        with open(fixture, "rt", encoding="utf-8") as f:
            expected_zenodo = f.read()
        assert actual_zenodo == expected_zenodo

    def test_check_cffobj(self):
        zenodo_object().check_cffobj()
        # doesn't need an assert

    def test_creators(self):
        assert zenodo_object().add_creators().creators == [
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Attema, Jisk"
            },
            {
                "affiliation": "Netherlands eScience Center",
                "name": "Diblen, Faruk",
                "orcid": "0000-0002-0989-929X"
            }
        ]

    def test_keywords(self):
        assert zenodo_object().add_keywords().keywords == [
            'visualization',
            'big data',
            'visual data analytics',
            'multi-dimensional data'
        ]

    def test_license(self):
        assert zenodo_object().add_license().license == {"id": "Apache-2.0"}

    def test_publication_date(self):
        assert zenodo_object().add_publication_date().publication_date == '2017-10-07'

    def test_title(self):
        assert zenodo_object().add_title().title == 'spot'

    def test_upload_type(self):
        assert zenodo_object().add_upload_type().upload_type == 'software'

    def test_version(self):
        assert zenodo_object().add_version().version == '0.1.0'
