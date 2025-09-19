def get_scores(sheet):
    """Henter alle rader som liste av dicts"""
    return sheet.get_all_records()


def add_score(sheet, name: str, score: int):
    """Legger til en ny rad"""
    sheet.append_row([name, score])


def update_score(sheet, row_index: int, new_name: str, new_score: int):
    """
    Oppdaterer en rad i arket.
    row_index = radnummer (starter på 2 pga headers)
    """
    sheet.update(f"A{row_index}", [[new_name, new_score]])


def delete_score(sheet, row_index: int):
    """Sletter en rad"""
    sheet.delete_rows(row_index)
