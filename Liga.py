class Liga:
    def __init__(self, liga):
        self.id = liga['id']
        self.nome = liga['name']
        self.pais = liga['country']
        self.inicio = liga['starting_year']
        self.fim = liga['ending_year']
        self.partidas = liga['totalMatches']
        self.gols = liga['seasonAVG_overall']
        self.escanteios = liga['cornersAVG_overall']
        self.cartoes = liga['cardsAVG_overall']
        self.faltas = liga['foulsAVG_overall']
        self.chutes = liga['shotsAVG_overall']
        self.impedimentos = liga['offsidesAVG_overall']
        self.numeroJogadores = liga['player_count']
        self.ambosMarcam = liga['btts_matches']

class Mandante:
    def __init__(self, liga):
        self.gols = liga['seasonAVG_home']
        self.escanteios = liga['cornersAVG_home']
        self.cartoes = liga['cardsAVG_home']
        self.faltas = liga['foulsAVG_home']
        self.chutes = liga['shotsAVG_home']
        self.impedimentos = liga['offsidesAVG_home']
        self.vitorias = liga['homeWinPercentage']
        self.cleanSheets = liga['home_teams_clean_sheets']
        self.failedScore = liga['home_teams_failed_to_score']

class Visitante:
    def __init__(self, liga):
        self.gols = liga['seasonAVG_away']
        self.escanteios = liga['cornersAVG_away']
        self.cartoes = liga['cardsAVG_away']
        self.faltas = liga['foulsAVG_away']
        self.chutes = liga['shotsAVG_away']
        self.impedimentos = liga['offsidesAVG_away']
        self.vitorias = liga['awayWinPercentage']
        self.cleanSheets = liga['away_teams_clean_sheets']
        self.failedScore = liga['away_teams_failed_to_score']