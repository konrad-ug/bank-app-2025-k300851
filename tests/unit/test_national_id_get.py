from src.national_id_utils import get_year_from_national_id
import pytest

class TestNationalIdGet:
    @pytest.mark.parametrize("national_id, year", 
                             [
                                 ("99060979383", 1999), 
                                 ("00213077482", 2000) #before_2000
                              ])
    def test_year_valid(self, national_id, year):
        assert get_year_from_national_id(national_id) == year

    @pytest.mark.parametrize("national_id", [
        None, "9906097938", "990609793833", "", "abcd5478987"
    ])
    def test_year_national_id_invalid(self, national_id):
        assert get_year_from_national_id(national_id) is None
