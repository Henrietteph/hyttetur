def connect_to_sheet(sheet_name: str):
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_dict(
        dict(st.secrets["gcp_service_account"]),
        scope
    )
    client = gspread.authorize(creds)
    return client.open(sheet_name).sheet1

def load_players_records(sheet):
    data = sheet.get_all_records()
    players = {row["Navn"]: int(row["Poeng"]) for row in data}
    return players

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
