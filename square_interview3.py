#  US, en, "Hello"
#  US, es, "Hola US"
#  SP, es, "Hola Spain"
#  JP, en, "Hello Japan"


# Relationship:
#   country to lang: n to n
#   country, lang to content : 1 to 1 


# add_content(country, lang, content)  
# - adds a country lang and its content string

# For all edge cases just print "Cannot Overwrite", "Not found" and return 

# Example: get_content(JP, fr)

# 1 Exact Match -> JP - fr
# 2 Country's Official Language -> JP-ja
# 3 English Base Copy -> JP-en
# 4 Absolute default -> Throw an error, some default string etc...


# c1 = CountryLang()
# c2 = CountryLang()
# c3 = CountryLang()

# c1.add_content(JP, en, 'How')
# c1.add_locale(JP, ja, 'random')

# c2.add_locale(JP, fr, 'Are')
# c2.add_locale(JP, en, 'string')

# c3.add_locale(JP, ja, 'more random')
# c3.add_locale(JP, en, 'You')
             
# Greated_Content([c1,c2,c3])

# Greater_Content.get_all_components(JP,fr)
              
# should return: How Are You (which is the JP,en version)

# For Better Visualization: 
# c1:        JP ja, JP en Default
# c2: JP fr,        JP en Default
# c3:        JP ja, JP en Default
    

class CountryLang:
    def __init__(self):
        self.countries = {}
        self.official = {'US':'en', 'JP': 'ja', 'SP': 'es'}
    
    def add_content(self, country, lang, content):
        if country in self.countries.keys():
            self.countries[country][lang] = content
        else:
            self.countries[country] = {lang:content}
    
    def get_content(self, country, lang):
        if not self.countries.get(country):
            return (None, None, "Country has not been added")
        if self.countries[country].get(lang):
            return (1, self.countries[country][lang])
        elif self.countries[country].get(self.official.get(country)):
            return (2, self.countries[country].get(self.official.get(country)))
        elif self.countries[country].get('en'):
            return (3, self.countries[country]['en'])
        else:
            return (None, None, "Could not find any languages close to query")

class GreaterCountryLang:
    def __init__(self, maps):
        self.maps = maps
        self.official = {'US':'en', 'JP': 'ja', 'SP': 'es'}
        
    def get_all_components(self, country, lang):
        highestL = 1
        for countryLang in self.maps:
            newL, newContent = countryLang.get_content(country, lang)
            if not newL:
                return 'Nothing found'
            elif newL > highestL:
                highestL = newL
        s = ""
        if highestL == 1:
            for countryLang in self.maps:
                l, content = countryLang.get_content(country, lang)
                s += content
            return s
        elif highestL == 2:
            for countryLang in self.maps:
                l, content = countryLang.get_content(country, self.official[country])
                s += content
            return s
        else:
            for countryLang in self.maps:
                l, content = countryLang.get_content(country, 'en')
                s += content
            return s
        
# c = CountryLang()
# c.add_content('US', 'en', 'Hello')
# c.add_content('US', 'es', 'Hola US')
# c.add_content('SP', 'es', 'Hola Spain')
# c.add_content('JP', 'en', 'Hello Japan')
# c.add_content('FR', 'yo', 'Hello France')

# print c.get_content('US', 'es')
# print c.get_content('SP', 'ja')
# print c.get_content('JP', 'fr')
# print c.get_content('PE', 'es')
# print c.get_content('FR', 'er')
# print c.countries


c1 = CountryLang()
c2 = CountryLang()
c3 = CountryLang()

c1.add_content('JP', 'en', 'How')
c1.add_content('JP', 'ja', 'random')

c2.add_content('JP', 'fr', 'Are')
c2.add_content('JP', 'en', 'string')

c3.add_content('JP', 'ja', 'more random')
c3.add_content('JP', 'en', 'You')
             
g = GreaterCountryLang([c1,c2,c3])

print g.get_all_components('JP','fr')