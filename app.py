from collections import namedtuple
import os

import gspread
from flask import Flask, render_template, request

from generate_credentials import create_cred


OrganizeData = namedtuple(
    'OrganizeData', ['cn_name', 'en_name', 'address', 'area', 'status',
                     'detail'])


CRED_FILENAME = 'google-credentials.json'


def create_app():
    app = Flask(__name__)

    # generate credentials using env vars
    # check to see if credentials file exist, if not, run
    dir_path = os.path.dirname(os.path.realpath(__file__))
    if CRED_FILENAME not in os.listdir(dir_path):
        create_cred()

    gc = gspread.service_account(filename=CRED_FILENAME)
    sheet = gc.open_by_key('1zcMeOqeNeX0aeY807KESo2Ytq3sIaeCiKWfWOXRfbDQ')
    useable_data = sheet.get_worksheet(0).get_all_values()[5:]

    # First six columns: Chinese Name, English Name, Address, Area, Status, Detail
    raw_clean_data = [data[:6] for data in useable_data]

    # TODO: see if there's a better way to deal with miscellenous rows
    clean_data = raw_clean_data[:-13]

    formatted_data = [OrganizeData(*market) for market in clean_data]

    @app.route('/')
    def index():
        return render_template('index.html', data=formatted_data)

    @app.route('/search', methods=('GET', 'POST'))
    def search():
        if request.method == 'POST':
            search_results = []
            search_input = request.form.get('search-input')

            for data in formatted_data:
                if search_input.lower() in data.en_name.lower() or (
                        search_input in data.cn_name):
                    search_results.append(data)
            if len(search_results) > 0:
                return render_template('index.html', data=search_results)
            return render_template('search.html', search=search_input)
        return render_template('index.html', data=formatted_data)

    return app


if __name__ == '__main__':
    create_app()
