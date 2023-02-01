import geo

ip = geo.getIP()
print(ip)

country = geo.getCountry(ip, 'plain')
print(country)

geoData = geo.getGeoData(ip)
print(geoData)

ptrData = geo.getGeoData(ip)
print(ptrData)

geo.showIpDetails('216.239.32.0')

geo.geoCountryDetails('216.239.32.0')
