# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from tqdm import tqdm
import re
import time
import sys
from jpx.jpxconfig import jpxdb_path, tmp_dir

transition_time = 1

#JPX統計資料画面にアクセス
def access_home(_driver):
    _driver.get('https://www.jpx.co.jp/markets/statistics-equities/misc/01.html')
    wait = WebDriverWait(_driver, 10)
    time.sleep(transition_time)
    print('JPX統計資料画面にアクセス')
    return _driver

def download_codelist(_driver):
    text = _driver.find_element_by_xpath('//*[@id="readArea"]/div[4]/div/table/tbody/tr/th').text
    excel_link = _driver.find_element_by_xpath('//*[@id="readArea"]/div[4]/div/table/tbody/tr/td/a').click()
    print('{}ダウンロード完了'.format(text))
    
if __name__ == '__main__':
    #headless mode
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument('--disable-extensions')       # すべての拡張機能を無効にする。ユーザースクリプトも無効にする
    options.add_argument('--proxy-server="direct://"') # Proxy経由ではなく直接接続する
    options.add_argument('--proxy-bypass-list=*')      # すべてのホスト名
    prefs = {'download.default_directory' : tmp_dir}  #defalutのダウンロード先の設定
    options.add_experimental_option('prefs',prefs)
    # options.add_argument('--no-sandbox')
    # options.add_argument("--single-process")
    # options.add_argument("--disable-application-cache")
    # options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

#     download_profit_csv(driver)
#     _from = '2020/10/1'
#     _to = '2020/12/31'
#     crawl_kessan_schedule(driver, _from, _to)
