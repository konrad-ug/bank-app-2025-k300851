import re
from src.national_id_utils import get_year_from_national_id


class Account:
    def __init__(self, first_name, last_name, national_id, promo_code=None):
        self.first_name = first_name
        self.last_name = last_name
        self.balance = 0

        national_id_year = get_year_from_national_id(national_id)
        if national_id_year is None:
            national_id = "Invalid"
        self.national_id = national_id

        
        if promo_code is not None and re.match(r"^PROM_...$", promo_code) and national_id_year and national_id_year > 1960:
            self.balance += 50
