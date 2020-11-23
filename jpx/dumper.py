from jpx.jpxconfig import jpxdb_path, tmp_dir
from jpx.crawler import *
from sqlite_pandas.models import sqlite_pandas as sp

import pandas as pd
from datetime import datetime
import glob
jpxdb = sp(jpxdb_path)

def dump_codelist():
    file = glob.glob(tmp_dir + '*.xls')[0]
    df = pd.read_excel(file)
    
    col = {
        'date':None,
        'code':'unique',
        'name':'unique',
        'market':None,
        'gyosyu_kubun33_code':None,
        'gyosyu_kubun33':None,
        'gyosyu_kubun17_code':None,
        'gyosyu_kubun17':None,
        'scale_code':None,
        'scale_kubun':None,
    }
    jpxdb.drop_table('code_list')
    jpxdb.create_table('code_list', col)
    jpxdb.insert_data('code_list', df)
    print('jpx code list excel is dumped to code list table in jpx_db')
   