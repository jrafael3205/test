import random
import os

# List of supported device models
Oppo = [
    "CPH1869", "CPH1929", "CPH2107", "CPH2238", "CPH2389", "CPH2401", "CPH2407", "CPH2413", "CPH2415", "CPH241", 
    "CPH2419", "CPH2455", "CPH2459", "CPH2461", "CPH2471", "CPH2473", "CPH2477", "CPH8893", "CPH2321", "CPH2341", 
    "CPH2373", "CPH2083", "CPH2071", "CPH2077", "CPH2185", "CPH2179", "CPH2269", "CPH2421", "CPH2349", "CPH2271", 
    "CPH1923", "CPH1925", "CPH1837", "CPH2015", "CPH2073", "CPH2081", "CPH2029", "CPH2031", "CPH2137", "CPH1605", 
    "CPH1803", "CPH1853", "CPH1805", "CPH1809", "CPH1851", "CPH1931", "CPH1959", "CPH1933", "CPH1935", "CPH1943", 
    "CPH2061", "CPH2069", "CPH2127", "CPH2131", "CPH2139", "CPH2135"
]

Realme = [
    "RMX1931", "RMX1933", "RMX1934", "RMX1935", "RMX1937", "RMX1941", "RMX1942", "RMX1943", "RMX1945", "RMX1946", 
    "RMX1947", "RMX1951", "RMX1952", "RMX1953", "RMX1955", "RMX1971", "RMX1973", "RMX1975", "RMX1976", "RMX1977", 
    "RMX1979", "RMX1981", "RMX1983", "RMX1987", "RMX1991", "RMX1992", "RMX1993", "RMX1994", "RMX1995", "RMX1996", 
    "RMX1997", "RMX1998", "RMX1999", "RMX2001", "RMX2002", "RMX2003", "RMX2005", "RMX2006", "RMX2007", "RMX2008", 
    "RMX2009", "RMX2010", "RMX2011", "RMX2012", "RMX2013", "RMX2015", "RMX2016", "RMX2017", "RMX2019", "RMX2020", 
    "RMX2021", "RMX2022", "RMX2023", "RMX2025", "RMX2026", "RMX2027", "RMX2029", "RMX2030", "RMX2031", "RMX2032", 
    "RMX2033", "RMX2035", "RMX2036", "RMX2037", "RMX2038", "RMX2039", "RMX2040", "RMX2041", "RMX2042", "RMX2043", 
    "RMX2044", "RMX2045", "RMX2046", "RMX2047", "RMX2048", "RMX2049", "RMX2050", "RMX2051", "RMX2052", "RMX2053", 
    "RMX2054", "RMX2055", "RMX2056", "RMX2057", "RMX2058", "RMX2059", "RMX2060", "RMX2061", "RMX2062", "RMX2063", 
    "RMX2064", "RMX2065", "RMX2066", "RMX2067", "RMX2068", "RMX2069", "RMX2070", "RMX2071", "RMX2072", "RMX2073", 
    "RMX2074", "RMX2075", "RMX2076", "RMX2077", "RMX2078", "RMX2079", "RMX2080", "RMX2081", "RMX2082", "RMX2083", 
    "RMX2084", "RMX2085", "RMX2086", "RMX2087", "RMX2088", "RMX2089", "RMX2090", "RMX2091", "RMX2092", "RMX2093", 
    "RMX2094", "RMX2095", "RMX2096", "RMX2097", "RMX2098", "RMX2099", "RMX2100", "RMX2101", "RMX2102", "RMX2103", 
    "RMX2104", "RMX2105", "RMX2106", "RMX2107", "RMX2108", "RMX2109", "RMX2110", "RMX2111", "RMX2112", "RMX2113", 
    "RMX2114", "RMX2115", "RMX2116", "RMX2117", "RMX2118", "RMX2119", "RMX2120", "RMX2121", "RMX2122", "RMX2123", 
    "RMX2124", "RMX2125", "RMX2126", "RMX2127", "RMX2128", "RMX2129", "RMX2130", "RMX2131", "RMX2132", "RMX2133", 
    "RMX2134", "RMX2135", "RMX2136", "RMX2137", "RMX2138", "RMX2139", "RMX2140", "RMX2141", "RMX2142", "RMX2143", 
    "RMX2144", "RMX2145", "RMX2146", "RMX2147", "RMX2148", "RMX2149", "RMX2150", "RMX2151", "RMX2152", "RMX2153", 
    "RMX2154", "RMX2155", "RMX2156", "RMX2157", "RMX2158", "RMX2159", "RMX2160", "RMX2161", "RMX2162", "RMX2163", 
    "RMX2164", "RMX2165", "RMX2166", "RMX2167", "RMX2168", "RMX2169", "RMX2170", "RMX2171", "RMX2172", "RMX2173", 
    "RMX2174", "RMX2175", "RMX2176", "RMX2177", "RMX2178", "RMX2179", "RMX2180", "RMX2181", "RMX2182", "RMX2183", 
    "RMX2184", "RMX2185", "RMX2186", "RMX2187", "RMX2188", "RMX2190", "RMX2191", "RMX2192", "RMX2193", "RMX2195", 
    "RMX2196", "RMX2197", "RMX2198", "RMX2199"
]

Samsung = [
    "SM-G960F", "SM-G965F", "SM-G970F", "SM-G973F", "SM-G975F", "SM-G980F", "SM-G981B", "SM-G986B", "SM-G988B", 
    "SM-G9750", "SM-G9730", "SM-G9700", "SM-G9600", "SM-G9650", "SM-G9500", "SM-G9550", "SM-G9350", "SM-G9300", 
    "SM-G9200", "SM-G9280", "SM-G9100", "SM-G8500", "SM-G8700", "SM-G7200", "SM-G7100", "SM-G6000", "SM-G6100", 
    "SM-G5300", "SM-G5100", "SM-G3600", "SM-G3610", "SM-G3160", "SM-G3180", "SM-A9200", "SM-A9100", "SM-A9000", 
    "SM-A8000", "SM-A7100", "SM-A7000", "SM-A6000", "SM-A5000", "SM-A5100", "SM-A5200", "SM-A5300", "SM-A600F", 
    "SM-A605F", "SM-A705F", "SM-A715F", "SM-A750F", "SM-A805F", "SM-A905F", "SM-M105F", "SM-M205F", "SM-M305F", 
    "SM-M405F", "SM-M505F", "SM-M515F", "SM-N970F", "SM-N975F", "SM-N980F", "SM-N985F", "SM-N986B", "SM-N960F", 
    "SM-N950F", "SM-N920F", "SM-N910F", "SM-N9000", "SM-N9005", "SM-T505", "SM-T500", "SM-T295", "SM-T290", 
    "SM-T865", "SM-T860", "SM-T835", "SM-T830", "SM-T725", "SM-T720", "SM-T515", "SM-T510", "SM-T595", "SM-T590", 
    "SM-T585", "SM-T580", "SM-T555", "SM-T550", "SM-T535", "SM-T530"
]

# Randomly select a model from Oppo, Realme, or Samsung
def generate_user_agent():
    selected_model = random.choice(Oppo + Realme + Samsung)
    
    fbav = f"298.0.0.{random.randint(11, 99)}.{random.randint(100, 999)}"
    fbbv = random.randint(100000000, 999999999)
    fbdm_density = round(random.uniform(1.0, 3.0), 1)  # Random density rounded to one decimal place
    fbdm_width = 1080
    fbdm_height = 4096
    fbcr = random.choice([
        "AIS", "cricket", "MegaFon", "Viettel Telecom", "TRUE-H", "TM", "GLOBE", "null", "VIETTEL", "TELCEL", "O2-CZ", 
        "U.S. Cellular", "SUN", "TelkomSA", "Verizon", "Plus", "Claro BR", "T-Mobile", "airtel", "PLAY (T-Mobile)", 
        "VIVACOM", "lifecell", "Yoigo", "life:) BY", "vodafone.de", "Vodafone", "PosteMobile", "Verizon Wireless", 
        "Movistar", "HOME", "SAZKAmobilCZ", "Astelit-LIFE;FBMF", "AT&T", "Grameenphone", "Robi", "Banglalink", 
        "Willkommen"
    ])

    # Determine fbmf based on selected_model
    if selected_model in Oppo:
        fbmf = "Oppo"
    elif selected_model in Realme:
        fbmf = "Realme"
    elif selected_model in Samsung:
        fbmf = "Samsung"

    fbpn = random.choice(["com.facebook.katana", "com.facebook.lite"])
    fbdv = selected_model
    fbsv = random.randint(6, 14)
    fbop = random.randint(1, 10)
    fbca = random.choice(["armeabi-v7a:armeabi", "arm64-v8a:armeabi"])

    # Construct the User-Agent string
    ua = (
        f"[FBAN/FB4A;FBAV/{fbav};FBBV/{fbbv};FBDM/{{density={fbdm_density},width={fbdm_width},height={fbdm_height}}};"
        f"FBLC/{random.choice(['th_TH', 'en_GB', 'en_US', 'fr_FR', 'es_ES', 'de_DE', 'it_IT', 'ru_RU', 'zh_CN', 'ja_JP'])};"
        f"FBRV/{random.randint(100000000, 999999999)};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbmf};FBPN/{fbpn};FBDV/{fbdv};"
        f"FBSV/{fbsv};FBOP/{fbop};FBCA/{fbca};]"
    )
    
    return ua

# Generate up to 100 User-Agent strings
user_agents = [generate_user_agent() for _ in range(100)]

# Create the directory if it doesn't exist
directory = "/sdcard"
if not os.path.exists(directory):
    os.makedirs(directory)

# Save generated User-Agent strings to a text file
file_path = os.path.join(directory, "FBAN_UA.txt")
with open(file_path, "w") as file:
    for ua in user_agents:
        file.write(f"Generated User-Agent: {ua}\n")

print(f"User-Agent strings have been saved to {file_path}")

# Print the generated User-Agent strings
for ua in user_agents:
    print(f"Generated User-Agent: {ua}")
