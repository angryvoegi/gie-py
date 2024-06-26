import enum
from typing import Union


def lookup_lso(s: Union['ALSILSO', str]) -> 'ALSILSO':
    if isinstance(s, ALSILSO):
        # If it already is an ASGICompany object, we're happy
        return s
    else:  # It is a string
        try:
            # do lookup
            return ALSILSO[s]
        except KeyError:
            # It is not, it may be a direct code
            try:
                return [obj for obj in ALSILSO if obj.value == s][0]
            except IndexError:
                raise ValueError('Invalid lso string')


def lookup_terminal(s: Union['ALSITerminal', str]) -> 'ALSITerminal':
    if isinstance(s, ALSITerminal):
        # If it already is an ASGICompany object, we're happy
        return s
    else:  # It is a string
        try:
            # do lookup
            return ALSITerminal[s]
        except KeyError:
            # It is not, it may be a direct code
            try:
                return [obj for obj in ALSITerminal if obj.value == s][0]
            except IndexError:
                raise ValueError('Invalid terminal string')


def lookup_country(s: Union['ALSICountry', str]) -> 'ALSICountry':
    if isinstance(s, ALSICountry):
        # If it already is an AGSICountry object, we're happy
        return s
    else:  # It is a string
        try:
            # do lookup
            return ALSICountry[s]
        except KeyError:
            # It is not, it may be a direct code
            try:
                return [obj for obj in ALSICountry if obj.value == s][0]
            except IndexError:
                raise ValueError('Invalid country string')


class ALSICountry(enum.Enum):
    """
    ENUM contains 2 things: code and full name

    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, full_name: str):
        self._full_name = full_name

    def __str__(self):
        return self.value

    @property
    def full_name(self):
        return self._full_name

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            'country': self.code
        }

    BE = "BE", "Belgium"
    DE = "DE", "Germany"
    ES = "ES", "Spain"
    FI = "FI", "Finland"
    FR = "FR", "France"
    GB = "GB", "Great Britain"
    GR = "GR", "Greece"
    HR = "HR", "Croatia"
    IT = "IT", "Italy"
    LT = "LT", "Lithuania"
    NL = "NL", "Netherlands"
    PL = "PL", "Poland"
    PT = "PT", "Portugal"


class ALSILSO(enum.Enum):
    """
    ENUM containing 2 things about an Area: code, country
    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, country: str):
        self._country = country

    def __str__(self):
        return self.value

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            'country': self.country,
            'company': self.code,
        }

    fluxys_lng = '21X000000001006T', 'BE'
    rwe_supply_trading = '11XRWETRADING--0', 'DE'
    deutsche_energy_terminal = '21X000000001403J', 'DE'
    deutsche_regas = '37X000000000265F', 'DE'
    bbg = '21X000000001352A', 'ES'
    enagas_transporte = '21X000000001254A', 'ES'
    saggas = '18XTGPRS-12345-G', 'ES'
    reganosa = '18XRGNSA-12345-V', 'ES'
    all_spanish_terminals = '21X0000000013368', 'ES'
    musel = '21X000000000134P', 'ES'
    hamina = '66X-00000000024H', 'FI'
    floating_lng_terminal_finland = '66X000000000027Z', 'FI'
    elengy = '21X0000000010679', 'FR'
    dunkerque_lng = '21X000000001331I', 'FR'
    fosmax_lng = '21X000000001070K', 'FR'
    totalenergies_lng = '63X218318139939Y', 'FR'
    national_grid_grain_lng = '21X-GB-A-A0A0A-7', 'GB'
    south_hook_lng = '21X0000000013554', 'GB'
    desfa = '21X-GR-A-A0A0A-G', 'GR'
    gastrade = '21X738265265081N', 'GR'
    lng_croatia = '31X-LNG-HR-----7', 'HR'
    gnl_italia = '26X00000117915-0', 'IT'
    olt_offshore_lng_toscana = '21X000000001109G', 'IT'
    adriatic_lng = '21X000000001360B', 'IT'
    snam_fsru = '59XFSRUITALIASTY', 'IT'
    klaipedos_nafta = '21X0000000013740', 'LT'
    gate_terminal = '21X000000001063H', 'NL'
    eems_energy = '52X000000000088H', 'NL'
    gaz_system = '21X-PL-A-A0A0A-B', 'PL'
    ren_atlantico = '21X0000000013619', 'PT'


class ALSITerminal(enum.Enum):
    """
    ENUM containing 3 things about an Area: code, country, code company
    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, country: str, company: str):
        self._country = country
        self._company = company

    def __str__(self):
        return self.value

    @property
    def company(self):
        return self._company

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            'country': self.country,
            'company': self.company,
            'facility': self.code
        }

    zeebrugge = '21W0000000001245', 'BE', '21X000000001006T',
    ostsee_terminal = '37W000000000106C', 'DE', '37X000000000265F'
    brunsbuettel = '37W000000000107A', 'DE', '21X000000001403J',
    wilhelmshafen = '21W000000000129W', 'DE', '21X000000001403J',
    wilhelmshafen_2 = '37W000000000111J', 'DE', '21X000000001403J'
    stade_terminal = '37W000000000110L', 'DE', '21X000000001403J'
    mukran = '37W000000000114D', 'DE', '37X000000000265F'
    bilbao = '21W0000000000362', 'ES', '21X000000001352A'
    barcelona = '21W000000000039X', 'ES', '21X000000001254A'
    cartagena = '21W000000000038Z', 'ES', '21X000000001254A'
    huelva = '21W0000000000370', 'ES', '21X000000001254A'
    sagunto = '21W0000000000354', 'ES', '18XTGPRS-12345-G'
    mugardos = '21W0000000000338', 'ES', '18XRGNSA-12345-V'
    tvb_virtual_balancing_lng_tank = '18W000000000GVMT', 'ES', '21X0000000013368'
    el_musel = '21W0000000000346', 'ES', '21X000000001254A'
    fos_tonkin = '63W179356656691A', 'FR', '21X0000000010679'
    montoir_de_bretagne = '63W631527814486R', 'FR', '21X0000000010679'
    dunkerque = '21W0000000000451', 'FR', '21X000000001331I'
    fos_cavaou = '63W943693783886F', 'FR', '21X000000001070K'
    le_havre = '63W835858561887S', 'FR', '63X218318139939Y'
    inkoo_terminal = '21W000000000130A', 'FI', '66X000000000027Z'
    hamina = '66W000000000001U', 'FI', '66X-00000000024H'
    isle_of_grain = '21W000000000099F', 'GB', '21X-GB-A-A0A0A-7'
    south_hook = '21W0000000000419', 'GB', '21X0000000013554'
    revythoussa = '21W000000000040B', 'GR', '21X-GR-A-A0A0A-G'
    alexandroupolis = '21W0000000001318', 'GR', '21X738265265081N'
    krk_fsru = '31W-0000-G-000-Z', 'HR', '31X-LNG-HR-----7'
    panigaglia = '59W0000000000011', 'IT', '26X00000117915-0'
    fsru_olt_offshore_lng_toscana = '21W0000000000443', 'IT', '21X000000001109G'
    porto_levante = '21W000000000082W', 'IT', '21X000000001360B'
    piombino = '59WFSRUGOLARTUNH', 'IT', '59XFSRUITALIASTY'
    fsru_independence = '21W0000000001253', 'LT', '21X0000000013740'
    rotterdam_gate = '21W0000000000079', 'NL', '21X000000001063H'
    eems_energy = '52W000000000001W', 'NL', '52X000000000088H'
    swinoujscie = '21W000000000096L', 'PL', '21X-PL-A-A0A0A-B'
    sines = '16WTGNL01------O', 'PT', '21X0000000013619'
