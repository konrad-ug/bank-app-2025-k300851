

def get_year_from_national_id(national_id):
    if national_id is None or len(national_id) != 11 or not national_id.isnumeric():
        return None

    month = int(national_id[2:4])
    year = int(national_id[:2])
    if month > 20:
        year += 2000
    else:
        year += 1900
    return year
