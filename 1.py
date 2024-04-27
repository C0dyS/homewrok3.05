import gzip
import json
import os


class Country:
    def __init__(self,country_dict = None):
        if country_dict is None:
            country_dict = {}
        self._country_dict = country_dict

    def __add__(self,other):
       if isinstance(other,tuple) and len(other) == 2:
           key,value = other
           self._country_dict[key] = value
       else:
           raise ValueError('Invalid input')

    def __sub__(self,key):
        if key in self._country_dict:
            del self._country_dict[key]
            print(f"Deleted key '{key}' from the country dictionary.")
        else:
            print(f"Key '{key}' not found in the country dictionary.")

    def get_single_value(self,key):
        return self._country_dict[key]

    def get(self):
        return self._country_dict


    def show_countries(self):
        for country, capital in self._country_dict.items():
            print(f"{country}: {capital}")
    def edit(self,key,new_value):
        self._country_dict[key] = new_value


    def upload(self):
        with open('countries.json','w') as file:
            json.dump(self._country_dict,file)

    def download(self):
        with open('countries.json','r') as file:
          self._country_dict = json.load(file)






countries = {
    "United States": "Washington, D.C.",
    "United Kingdom": "London",
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "Canada": "Ottawa",
    "Australia": "Canberra",
    "Japan": "Tokyo",
    "China": "Beijing"
}

class_test = Country(countries)

print(class_test.show_countries())
class_test - 'China'
print(class_test.show_countries())
class_test + ('a','b')
print(class_test.show_countries())
class_test.upload()

print('__________________')
class_test2 = Country()
class_test2.download()
print(class_test2.show_countries())