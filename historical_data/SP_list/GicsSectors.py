def get_gics_sector_by_code(code: int) -> str:
    return codes_to_gics[code]


def get_code_by_gics_sector(gics: str) -> int:
    return gics_to_codes[gics]


def get_gics_by_company(company: str) -> str:
    return companies_to_gics[company]


def get_gics_code_by_company(company: str) -> int:
    return gics_to_codes[companies_to_gics[company]]


codes_to_gics = {
    1: "Industrials",
    2: "Health Care",
    3: "Information Technology",
    4: "Communication Services",
    5: "Consumer Discretionary",
    6: "Utilities",
    7: "Financials",
    8: "Materials",
    9: "Consumer Staples",
    10: "Real Estate",
    11: "Energy"
}

gics_to_codes = {
    "Industrials": 1,
    "Health Care": 2,
    "Information Technology": 3,
    "Communication Services": 4,
    "Consumer Discretionary": 5,
    "Utilities": 6,
    "Financials": 7,
    "Materials": 8,
    "Consumer Staples": 9,
    "Real Estate": 10,
    "Energy": 11
}

companies_to_gics = {
    "A": "Health Care",
    "AAL": "Industrials",
    "AAP": "Consumer Discretionary",
    "AAPL": "Information Technology",
    "ABBV": "Health Care",
    "ABC": "Health Care",
    "ABMD": "Health Care",
    "ABT": "Health Care",
    "ACN": "Information Technology",
    "ADBE": "Information Technology",
    "ADI": "Information Technology",
    "ADM": "Consumer Staples",
    "ADP": "Information Technology",
    "ADS": "Information Technology",
    "ADSK": "Information Technology",
    "AEE": "Utilities",
    "AEP": "Utilities",
    "AES": "Utilities",
    "AFL": "Financials",
    "AGN": "Health Care",
    "AIG": "Financials",
    "AIV": "Real Estate",
    "AIZ": "Financials",
    "AJG": "Financials",
    "AKAM": "Information Technology",
    "AKS": "Materials",
    "ALB": "Materials",
    "ALGN": "Health Care",
    "ALK": "Industrials",
    "ALL": "Financials",
    "ALLE": "Industrials",
    "ALXN": "Health Care",
    "AMAT": "Information Technology",
    "AMCR": "Materials",
    "AMD": "Information Technology",
    "AME": "Industrials",
    "AMG": "Financials",
    "AMGN": "Health Care",
    "AMP": "Financials",
    "AMT": "Real Estate",
    "AMZN": "Consumer Discretionary",
    "AN": "Industrials",
    "ANET": "Information Technology",
    "ANF": "Consumer Discretionary",
    "ANSS": "Information Technology",
    "ANTM": "Health Care",
    "AON": "Financials",
    "AOS": "Industrials",
    "APA": "Energy",
    "APD": "Materials",
    "APH": "Information Technology",
    "APTV": "Consumer Discretionary",
    "ARE": "Real Estate",
    "ARNC": "Industrials",
    "ATI": "Materials",
    "ATO": "Utilities",
    "ATVI": "Communication Services",
    "AVB": "Real Estate",
    "AVGO": "Information Technology",
    "AVP": "Consumer Staples",
    "AVY": "Materials",
    "AWK": "Utilities",
    "AXP": "Financials",
    "AYI": "Real Estate",
    "AZO": "Consumer Discretionary",
    "BA": "Industrials",
    "BAC": "Financials",
    "BAX": "Health Care",
    "BBBY": "Consumer Discretionary",
    "BBY": "Consumer Discretionary",
    "BEN": "Financials",
    "BF-B": "Consumer Staples",
    "BHF": "Financials",
    "BIG": "Consumer Staples",
    "BIIB": "Health Care",
    "BK": "Financials",
    "BKNG": "Consumer Discretionary",
    "BKR": "Energy",
    "BLK": "Financials",
    "BLL": "Materials",
    "BMY": "Health Care",
    "BR": "Information Technology",
    "BRK-B": "Financials",
    "BSX": "Health Care",
    "BWA": "Consumer Discretionary",
    "BXP": "Real Estate",
    "C": "Financials",
    "CA": "Information Technology",
    "CAG": "Consumer Staples",
    "CAH": "Health Care",
    "CAT": "Industrials",
    "CB": "Financials",
    "CBE": "Energy",
    "CBOE": "Financials",
    "CBRE": "Real Estate",
    "CCI": "Real Estate",
    "CCK": "Consumer Staples",
    "CCL": "Consumer Discretionary",
    "CDNS": "Information Technology",
    "CDW": "Information Technology",
    "CE": "Materials",
    "CELG": "Health Care",
    "CF": "Materials",
    "CFG": "Financials",
    "CHD": "Consumer Staples",
    "CHK": "Energy",
    "CHRW": "Industrials",
    "CHTR": "Communication Services",
    "CI": "Health Care",
    "CINF": "Financials",
    "CL": "Consumer Staples",
    "CLF": "Materials",
    "CLX": "Consumer Staples",
    "CMA": "Financials",
    "CMCSA": "Communication Services",
    "CME": "Financials",
    "CMG": "Consumer Discretionary",
    "CMI": "Industrials",
    "CMS": "Utilities",
    "CNC": "Health Care",
    "CNP": "Utilities",
    "CNX": "Energy",
    "COF": "Financials",
    "COG": "Energy",
    "COO": "Health Care",
    "COP": "Health Care",
    "COST": "Consumer Staples",
    "COTY": "Consumer Staples",
    "CPB": "Consumer Staples",
    "CPRI": "Consumer Discretionary",
    "CPRT": "Industrials",
    "CRM": "Information Technology",
    "CSCO": "Information Technology",
    "CSX": "Industrials",
    "CTAS": "Industrials",
    "CTL": "Communication Services",
    "CTSH": "Information Technology",
    "CTVA": "Materials",
    "CTXS": "Information Technology",
    "CVS": "Health Care",
    "CVX": "Energy",
    "CXO": "Energy",
    "D": "Utilities",
    "DAL": "Industrials",
    "DD": "Materials",
    "DE": "Industrials",
    "DFS": "Financials",
    "DG": "Consumer Discretionary",
    "DGX": "Health Care",
    "DHI": "Consumer Discretionary",
    "DHR": "Health Care",
    "DIS": "Communication Services",
    "DISCA": "Communication Services",
    "DISCK": "Communication Services",
    "DISH": "Communication Services",
    "DLR": "Real Estate",
    "DLTR": "Consumer Discretionary",
    "DNR": "Energy",
    "DO": "Energy",
    "DOV": "Industrials",
    "DOW": "Materials",
    "DRE": "Real Estate",
    "DRI": "Consumer Discretionary",
    "DTE": "Utilities",
    "DUK": "Utilities",
    "DVA": "Health Care",
    "DVN": "Energy",
    "DXC": "Information Technology",
    "EA": "Communication Services",
    "EBAY": "Consumer Discretionary",
    "ECL": "Materials",
    "ED": "Utilities",
    "EFX": "Industrials",
    "EIX": "Utilities",
    "EL": "Consumer Staples",
    "EMN": "Materials",
    "EMR": "Industrials",
    "ENDP": "Health Care",
    "EOG": "Energy",
    "EQIX": "Real Estate",
    "EQR": "Real Estate",
    "EQT": "Utilities",
    "ES": "Utilities",
    "ESS": "Real Estate",
    "ETFC": "Financials",
    "ETN": "Industrials",
    "ETR": "Utilities",
    "EVHC": "Health Care",
    "EVRG": "Utilities",
    "EW": "Health Care",
    "EXC": "Utilities",
    "EXPD": "Industrials",
    "EXPE": "Consumer Discretionary",
    "EXR": "Real Estate",
    "F": "Consumer Discretionary",
    "FANG": "Energy",
    "FAST": "Industrials",
    "FB": "Communication Services",
    "FBHS": "Industrials",
    "FCX": "Materials",
    "FDX": "Industrials",
    "FE": "Utilities",
    "FFIV": "Information Technology",
    "FHN": "Financials",
    "FII": "Financials",
    "FIS": "Information Technology",
    "FISV": "Information Technology",
    "FITB": "Financials",
    "FL": "Consumer Discretionary",
    "FLIR": "Information Technology",
    "FLR": "Energy",
    "FLS": "Industrials",
    "FLT": "Information Technology",
    "FMC": "Materials",
    "FOSL": "Consumer Discretionary",
    "FOX": "Communication Services",
    "FOXA": "Communication Services",
    "FRC": "Financials",
    "FRT": "Real Estate",
    "FSLR": "Information Technology",
    "FTI": "Energy",
    "FTNT": "Information Technology",
    "FTR": "Communication Services",
    "FTV": "Industrials",
    "GD": "Industrials",
    "GE": "Industrials",
    "GHC": "Consumer Discretionary",
    "GILD": "Health Care",
    "GIS": "Consumer Staples",
    "GL": "Financials",
    "GLW": "Information Technology",
    "GM": "Consumer Discretionary",
    "GME": "Consumer Discretionary",
    "GOOG": "Communication Services",
    "GOOGL": "Communication Services",
    "GPC": "Consumer Discretionary",
    "GPN": "Information Technology",
    "GPS": "Consumer Discretionary",
    "GRA": "Materials",
    "GRMN": "Consumer Discretionary",
    "GS": "Financials",
    "GT": "Consumer Discretionary",
    "GWW": "Industrials",
    "HAL": "Energy",
    "HAS": "Consumer Discretionary",
    "HBAN": "Financials",
    "HBI": "Consumer Discretionary",
    "HCA": "Health Care",
    "HD": "Consumer Discretionary",
    "HES": "Energy",
    "HFC": "Energy",
    "HIG": "Financials",
    "HII": "Industrials",
    "HLT": "Consumer Discretionary",
    "HOG": "Consumer Discretionary",
    "HOLX": "Health Care",
    "HON": "Industrials",
    "HP": "Energy",
    "HPE": "Information Technology",
    "HPQ": "Information Technology",
    "HRB": "Consumer Discretionary",
    "HRL": "Consumer Staples",
    "HSIC": "Health Care",
    "HST": "Real Estate",
    "HSY": "Consumer Staples",
    "HUM": "Health Care",
    "IBM": "Information Technology",
    "ICE": "Financials",
    "IDXX": "Health Care",
    "IEX": "Industrials",
    "IFF": "Materials",
    "IGT": "Consumer Discretionary",
    "ILMN": "Health Care",
    "INCY": "Health Care",
    "INFO": "Industrials",
    "INTC": "Information Technology",
    "INTU": "Information Technology",
    "IP": "Materials",
    "IPG": "Communication Services",
    "IPGP": "Information Technology",
    "IQV": "Health Care",
    "IR": "Industrials",
    "IRM": "Real Estate",
    "ISRG": "Health Care",
    "IT": "Information Technology",
    "ITT": "Industrials",
    "ITW": "Industrials",
    "IVZ": "Financials",
    "J": "Industrials",
    "JBHT": "Industrials",
    "JBL": "Information Technology",
    "JCI": "Industrials",
    "JCP": "Consumer Discretionary",
    "JEF": "Financials",
    "JKHY": "Information Technology",
    "JNJ": "Health Care",
    "JNPR": "Information Technology",
    "JPM": "Financials",
    "JWN": "Consumer Discretionary",
    "K": "Consumer Staples",
    "KEY": "Financials",
    "KEYS": "Information Technology",
    "KHC": "Consumer Staples",
    "KIM": "Real Estate",
    "KLAC": "Information Technology",
    "KMB": "Consumer Staples",
    "KMI": "Energy",
    "KMX": "Consumer Discretionary",
    "KO": "Consumer Staples",
    "KR": "Consumer Staples",
    "KSS": "Consumer Discretionary",
    "KSU": "Industrials",
    "L": "Financials",
    "LB": "Consumer Discretionary",
    "LDOS": "Information Technology",
    "LEG": "Consumer Discretionary",
    "LEN": "Consumer Discretionary",
    "LH": "Health Care",
    "LHX": "Industrials",
    "LIN": "Materials",
    "LKQ": "Consumer Discretionary",
    "LLY": "Health Care",
    "LM": "Financials",
    "LMT": "Industrials",
    "LNC": "Financials",
    "LNT": "Utilities",
    "LOW": "Consumer Discretionary",
    "LRCX": "Information Technology",
    "LSI": "Real Estate",
    "LUV": "Industrials",
    "LVS": "Consumer Discretionary",
    "LW": "Consumer Staples",
    "LYB": "Materials",
    "LYV": "Communication Services",
    "M": "Consumer Discretionary",
    "MA": "Information Technology",
    "MAA": "Real Estate",
    "MAC": "Real Estate",
    "MAR": "Consumer Discretionary",
    "MAS": "Industrials",
    "MAT": "Consumer Discretionary",
    "MCD": "Consumer Discretionary",
    "MCHP": "Information Technology",
    "MCK": "Health Care",
    "MCO": "Financials",
    "MDLZ": "Consumer Staples",
    "MDT": "Health Care",
    "MET": "Financials",
    "MGM": "Consumer Discretionary",
    "MHK": "Consumer Discretionary",
    "MKC": "Consumer Staples",
    "MKTX": "Financials",
    "MLM": "Materials",
    "MMC": "Financials",
    "MMM": "Industrials",
    "MNK": "Health Care",
    "MNST": "Consumer Staples",
    "MO": "Consumer Staples",
    "MOLX": "Industrials",
    "MOS": "Materials",
    "MPC": "Energy",
    "MRK": "Health Care",
    "MRO": "Energy",
    "MS": "Financials",
    "MSCI": "Financials",
    "MSFT": "Information Technology",
    "MSI": "Information Technology",
    "MTB": "Financials",
    "MTD": "Health Care",
    "MU": "Information Technology",
    "MUR": "Energy",
    "MXIM": "Information Technology",
    "MYL": "Health Care",
    "NAVI": "Financials",
    "NBL": "Energy",
    "NBR": "Energy",
    "NCLH": "Consumer Discretionary",
    "NDAQ": "Financials",
    "NE": "Energy",
    "NEE": "Utilities",
    "NEM": "Materials",
    "NFLX": "Communication Services",
    "NI": "Utilities",
    "NKE": "Consumer Discretionary",
    "NKTR": "Health Care",
    "NLOK": "Information Technology",
    "NLSN": "Industrials",
    "NOC": "Industrials",
    "NOV": "Energy",
    "NOW": "Information Technology",
    "NRG": "Utilities",
    "NSC": "Industrials",
    "NTAP": "Information Technology",
    "NTRS": "Financials",
    "NUE": "Materials",
    "NVDA": "Information Technology",
    "NVR": "Consumer Discretionary",
    "NWL": "Consumer Discretionary",
    "NWS": "Communication Services",
    "NWSA": "Communication Services",
    "NYT": "Communication Services",
    "O": "Real Estate",
    "ODFL": "Industrials",
    "ODP": "Consumer Discretionary",
    "OI": "Materials",
    "OKE": "Energy",
    "OMC": "Communication Services",
    "ORCL": "Information Technology",
    "ORLY": "Consumer Discretionary",
    "OXY": "Energy",
    "PAYC": "Information Technology",
    "PAYX": "Information Technology",
    "PBCT": "Financials",
    "PBI": "Industrials",
    "PCAR": "Industrials",
    "PCG": "Utilities",
    "PDCO": "Health Care",
    "PEAK": "Real Estate",
    "PEG": "Utilities",
    "PEP": "Consumer Staples",
    "PFE": "Health Care",
    "PFG": "Financials",
    "PG": "Consumer Staples",
    "PGR": "Financials",
    "PH": "Industrials",
    "PHM": "Consumer Discretionary",
    "PKG": "Materials",
    "PKI": "Health Care",
    "PLD": "Real Estate",
    "PM": "Consumer Staples",
    "PNC": "Financials",
    "PNR": "Industrials",
    "PNW": "Utilities",
    "PPG": "Materials",
    "PPL": "Utilities",
    "PRGO": "Health Care",
    "PRU": "Financials",
    "PSA": "Real Estate",
    "PSX": "Energy",
    "PVH": "Consumer Discretionary",
    "PWR": "Industrials",
    "PXD": "Energy",
    "PYPL": "Information Technology",
    "QCOM": "Information Technology",
    "QEP": "Energy",
    "QRVO": "Information Technology",
    "R": "Industrials",
    "RCL": "Consumer Discretionary",
    "RE": "Financials",
    "REG": "Real Estate",
    "REGN": "Health Care",
    "RF": "Financials",
    "RHI": "Industrials",
    "RIG": "Energy",
    "RJF": "Financials",
    "RL": "Consumer Discretionary",
    "RMD": "Health Care",
    "ROK": "Industrials",
    "ROL": "Industrials",
    "ROP": "Industrials",
    "ROST": "Consumer Discretionary",
    "RRC": "Energy",
    "RRD": "Industrials",
    "RSG": "Industrials",
    "RTN": "Industrials",
    "S": "Communication Services",
    "SBAC": "Real Estate",
    "SBL": "Information Technology",
    "SBUX": "Consumer Discretionary",
    "SCHW": "Financials",
    "SEE": "Materials",
    "SHW": "Materials",
    "SIG": "Consumer Discretionary",
    "SIVB": "Financials",
    "SJM": "Consumer Staples",
    "SLB": "Energy",
    "SLG": "Real Estate",
    "SLM": "Financials",
    "SNA": "Industrials",
    "SNPS": "Information Technology",
    "SO": "Utilities",
    "SPG": "Real Estate",
    "SPGI": "Financials",
    "SRCL": "Industrials",
    "SRE": "Utilities",
    "STE": "Health Care",
    "STT": "Financials",
    "STX": "Information Technology",
    "STZ": "Consumer Staples",
    "SUN": "Energy",
    "SWK": "Industrials",
    "SWKS": "Information Technology",
    "SWN": "Energy",
    "SYF": "Financials",
    "SYK": "Health Care",
    "SYY": "Consumer Staples",
    "T": "Communication Services",
    "TAP": "Consumer Staples",
    "TDG": "Industrials",
    "TEL": "Information Technology",
    "TER": "Information Technology",
    "TFC": "Financials",
    "TFX": "Health Care",
    "TGT": "Consumer Discretionary",
    "THC": "Health Care",
    "TIE": "Materials",
    "TIF": "Consumer Discretionary",
    "TJX": "Consumer Discretionary",
    "TMO": "Health Care",
    "TMUS": "Communication Services",
    "TPR": "Consumer Discretionary",
    "TRIP": "Communication Services",
    "TROW": "Financials",
    "TRV": "Financials",
    "TSCO": "Consumer Discretionary",
    "TSN": "Consumer Staples",
    "TTWO": "Communication Services",
    "TWTR": "Communication Services",
    "TXN": "Information Technology",
    "TXT": "Industrials",
    "UA": "Consumer Discretionary",
    "UAA": "Consumer Discretionary",
    "UAL": "Industrials",
    "UDR": "Real Estate",
    "UHS": "Health Care",
    "ULTA": "Consumer Discretionary",
    "UNH": "Health Care",
    "UNM": "Financials",
    "UNP": "Industrials",
    "UPS": "Industrials",
    "URBN": "Consumer Discretionary",
    "URI": "Industrials",
    "USB": "Financials",
    "UTX": "Industrials",
    "V": "Information Technology",
    "VAR": "Health Care",
    "VFC": "Consumer Discretionary",
    "VIAB": "Communication Services",
    "VIAC": "Communication Services",
    "VLO": "Energy",
    "VMC": "Materials",
    "VNO": "Real Estate",
    "VRSK": "Industrials",
    "VRSN": "Information Technology",
    "VRTX": "Health Care",
    "VTR": "Real Estate",
    "VZ": "Communication Services",
    "WAB": "Industrials",
    "WAT": "Health Care",
    "WBA": "Consumer Staples",
    "WCG": "Health Care",
    "WDC": "Information Technology",
    "WEC": "Utilities",
    "WELL": "Real Estate",
    "WFC": "Financials",
    "WHR": "Consumer Discretionary",
    "WLTW": "Financials",
    "WM": "Industrials",
    "WMB": "Energy",
    "WMT": "Consumer Staples",
    "WPX": "Energy",
    "WRB": "Financials",
    "WRK": "Materials",
    "WU": "Information Technology",
    "WY": "Real Estate",
    "WYNN": "Consumer Discretionary",
    "X": "Materials",
    "XEC": "Energy",
    "XEL": "Utilities",
    "XLNX": "Information Technology",
    "XOM": "Energy",
    "XRAY": "Health Care",
    "XRX": "Information Technology",
    "XYL": "Industrials",
    "YUM": "Consumer Discretionary",
    "ZBH": "Health Care",
    "ZBRA": "Information Technology",
    "ZION": "Financials",
    "ZTS": "Health Care"
}
