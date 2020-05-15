from collections import namedtuple

import gspread
from flask import Flask, render_template


OrganizeData = namedtuple(
    'OrganizeData', ['cn_name', 'en_name', 'address', 'area', 'status',
                     'detail'])


app = Flask(__name__)


@app.route('/')
def index():
    gc = gspread.service_account(filename='credentials.json')
    sheet = gc.open_by_key('1zcMeOqeNeX0aeY807KESo2Ytq3sIaeCiKWfWOXRfbDQ')
    useable_data = sheet.get_worksheet(0).get_all_values()[5:]

    # First six columns: Chinese Name, English Name, Address, Area, Status, Detail
    raw_clean_data = [data[:6] for data in useable_data]

    # TODO: see if there's a better way to deal with miscellenous rows
    clean_data = raw_clean_data[:-13]

    formatted_data = [OrganizeData(*market) for market in clean_data]

    return render_template('index.html', data=formatted_data)
