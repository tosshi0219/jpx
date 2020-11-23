from sqlite_pandas.models import sqlite_pandas as sp
from jpx.jpxconfig import jpxdb_path
from datetime import datetime
import re

class fetcher:
    def __init__ (self):
        self.jpxdb = sp(jpxdb_path)
        self.df = self.jpxdb.get_dataframe('code_list')
        self.all_codes = list(self.df.code)
        self.all_names = [re.sub('\u3000', ' ', d) for d in self.df.name]
        self.dict_code_name = self.make_dict_code_name()
        self.market = list(self.df.market.unique())
        self.gyosyu_kubun33 = sorted(list(self.df.gyosyu_kubun33.unique()))
        self.gyosyu_kubun33_code = sorted(list(self.df.gyosyu_kubun33_code.unique()))
        self.gyosyu_kubun17 = sorted(list(self.df.gyosyu_kubun17.unique()))
        self.gyosyu_kubun17_code = sorted(list(self.df.gyosyu_kubun17_code.unique()))
        self.scale_kubun = sorted(list(self.df.scale_kubun.unique()))
        self.scale_code = sorted(list(self.df.scale_code.unique()))
        self.gyosyu33_dict = self.make_dict('gyosyu_kubun33_code', 'gyosyu_kubun33')
        self.gyosyu17_dict = self.make_dict('gyosyu_kubun17_code', 'gyosyu_kubun17')
        self.scale_dict = self.make_dict('scale_code', 'scale_kubun')
        
    def make_dict(self, _code, _name):
        _df = self.df.drop_duplicates(subset=_code)
        _df = _df.loc[:,[_code, _name]].sort_values(_code).reset_index(drop=True)
        return dict(zip(_df[_code], _df[_name]))
    
    def make_dict_code_name(self):
        dict_code_name = {}
        for i,code in enumerate(self.all_codes):
            dict_code_name[code] = self.all_names[i]
        return dict_code_name
        
if __name__ == '__main__':
    fet = fetcher()