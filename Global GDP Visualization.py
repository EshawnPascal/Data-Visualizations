import json
from country_codes import get_country_code
import pygal.maps.world as WorldMap

# Load the data into a list.
filename = 'GDP_by_Country.json'
with open(filename) as f:
    gdp_data = json.load(f)

# Build a dictionary of GDP Data...
global_gdp = {}
for gdp_dict in gdp_data:
    if gdp_dict['Year'] == '2014':
        country_name = gdp_dict['Country Name']
        gdp_value = int(float(gdp_dict['Value']))
        code = get_country_code(country_name)
        if code:
            global_gdp[code] = gdp_value

# Group countries into 3 groups by GDP
gdp_pop1, gdp_pop2, gdp_pop3 = {}, {}, {}
for cc, gdp in global_gdp.items():
    if gdp > 10**11:
        gdp_pop1[cc] = gdp # 100 Billion
    elif gdp > 10**10:
        gdp_pop2[cc] = gdp # 10 Billion
    else:
        gdp_pop3 = gdp # Less than 10 Billion

# Display world map with GDP data
wm = WorldMap.World()
wm.title = 'World GDP in 2014, by Country (USD)'
wm.add('GDP > $100B', gdp_pop1)
wm.add('GDP > $10B', gdp_pop2)
wm.add('GDP < $10B', gdp_pop3)
wm.render_to_file('Global GDP 2014.svg')


