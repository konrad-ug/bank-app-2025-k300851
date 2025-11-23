from src.national_id_utils import get_year_from_national_id


class TestNationalIdGet:
    def test_year_before_2000(self):
        national_id = "99060979383"
        assert get_year_from_national_id(national_id) == 1999

    def test_year_after_2000(self):
        national_id = "00213077482"
        assert get_year_from_national_id(national_id) == 2000

    def test_year_national_id_invalid(self):
        national_ids = [
            None, "9906097938", "990609793833", "", "abcd5478987"
        ]
        for national_id in national_ids:
            assert get_year_from_national_id(national_id) is None
