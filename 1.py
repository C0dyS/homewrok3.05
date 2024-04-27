import gzip
import json
import os


class Musicians:
    def __init__(self,musicians_dict = None):
        if musicians_dict is None:
            musicians_dict = {}
        self._musicians_dict = musicians_dict

    def __add__(self,other):
       if isinstance(other,tuple) and len(other) == 2:
           key,value = other
           self._musicians_dict[key] = value
       else:
           raise ValueError('Invalid input')

    def __sub__(self,key):
        if key in self._musicians_dict:
            del self._musicians_dict[key]
            print(f"Deleted key '{key}' from the musicians dictionary.")
        else:
            print(f"Key '{key}' not found in the musicians dictionary.")

    def get_single_value(self,key):
        return self._musicians_dict[key]

    def get(self):
        return self._musicians_dict


    def show_musicians(self):
        for musician, album in self._musicians_dict.items():
            print(f"{musician}: {album}")
    def edit(self,key,new_value):
        self._musicians_dict[key] = new_value


    def upload(self):
        with open('musicians.json','w') as file:
            json.dump(self._musicians_dict,file)

    def download(self):
        with open('musicians.json','r') as file:
          self._musicians_dict = json.load(file)






