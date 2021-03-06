airportcodes = {
"AGU": "Aguascalientes",
"CDI": "Baja California",
"ESE": "Baja California",
"MXL": "Baja California",
"SFH": "Baja California",
"TIJ": "Baja California",
"CSL": "Baja California Sur",
"CUA": "Baja California Sur",
"GUB": "Baja California Sur",
"LAP": "Baja California Sur",
"LTO": "Baja California Sur",
"MUG": "Baja California Sur",
"PVP": "Baja California Sur",
"SJD": "Baja California Sur",
"CME": "Campeche",
"CPE": "Campeche",
"CJT": "Chiapas",
"PJP": "Chiapas",
"PQM": "Chiapas",
"SZT": "Chiapas",
"TAP": "Chiapas",
"TGM": "Chiapas",
"TGZ": "Chiapas",
"CJS": "Chihuahua",
"CUU": "Chihuahua",
"NCG": "Chihuahua",
"ACN": "Coahuila",
"LOV": "Coahuila",
"PDS": "Coahuila",
"SLW": "Coahuila",
"TRC": "Coahuila",
"CLQ": "Colima",
"ZLO": "Colima",
"ZLO": "Colima",
"MEX": "Ciudad de México",
"DGO": "Durango",
"TLC": "Estado de México",
"BJX": "Guanajuato",
"CYW": "Guanajuato",
"ACA": "Guerrero",
"PIE": "Guerrero",
"ZIH": "Guerrero",
"PCA": "Hidalgo",
"GDL": "Jalisco",
"LOM": "Jalisco",
"PVR": "Jalisco",
"TUX": "Jalisco",
"ZAP": "Jalisco",
"JJC": "México",
"SLM": "México",
"AZG": "Michoacán",
"LZC": "Michoacán",
"MLM": "Michoacán",
"UPN": "Michoacán",
"ZMM": "Michoacán",
"CVJ": "Morelos",
"TNY": "Nayarit",
"TPQ": "Nayarit",
"MTY": "Nuevo León",
"NTR": "Nuevo León",
"HUX": "Oaxaca",
"IZT": "Oaxaca",
"OAX": "Oaxaca",
"PXM": "Oaxaca",
"SCX": "Oaxaca",
"TCN": "Puebla",
"QRO": "Querétaro",
"CTM": "Quintana Roo",
"CUN": "Quintana Roo",
"CZM": "Quintana Roo",
"ISJ": "Quintana Roo",
"TUY": "Quintana Roo",
"SLP": "San Luis Potosí",
"TCN": "San Luis Potosí",
"TSL": "San Luis Potosí",
"CNA": "Sonora",
"CUL": "Sinaloa",
"LMM": "Sinaloa",
"MZT": "Sinaloa",
"NAV": "Sonora",
"PPE": "Sonora",
"TCP": "Sinaloa",
"UAC": "Sonora",
"XAL": "Sonora",
"CEN": "Sonora",
"GYM": "Sonora",
"HMO": "Sonora",
"NOG": "Sonora",
"CPX": "Tabasco",
"VSA": "Tabasco",
"CVM": "Tamaulipas",
"MAM": "Tamaulipas",
"MMC": "Tamaulipas",
"NLD": "Tamaulipas",
"REX": "Tamaulipas",
"TAM": "Tamaulipas",
"JAL": "Veracruz",
"MTT": "Veracruz",
"PAZ": "Veracruz",
"VER": "Veracruz",
"CZA": "Yucatán",
"MID": "Yucatán",
"TZM": "Yucatán",
"ZCL": "Zacatecas",
"LIM" : "Lima",
'DFW' : "Dallas",
"HAV" : "Havana",
"NY" : "New York",
"YYZ" : "Toronto",
"CCI" : "Concórdia",
"AMS" : "Amsterdam",
"CLT" : "Charlotte",
"YVR" : "Vancouver",
"IAH" : "Houston"
}

def getCityName(s):
    """
        Function that converts a iata code to the real name of a city.
        : param s: String IATA CODE
        :return: String name of a city.
    """
    if s in airportcodes:
        return airportcodes[s]
    return s