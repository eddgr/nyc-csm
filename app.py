from collections import namedtuple
import os

import gspread
from flask import Flask, render_template, request

from generate_credentials import check_credentials, CREDENTIAL_FILENAME


OrganizeData = namedtuple(
    'OrganizeData', ['cn_name', 'en_name', 'address', 'area', 'status',
                     'detail'])


def _unique_list(raw_list):
    unique_list = []
    for list_item in raw_list:
        if list_item not in unique_list:
            unique_list.append(list_item)
    return unique_list


def create_app():
    app = Flask(__name__)

    check_credentials()

    gc = gspread.service_account(filename=CREDENTIAL_FILENAME)
    sheet = gc.open_by_key('1zcMeOqeNeX0aeY807KESo2Ytq3sIaeCiKWfWOXRfbDQ')
    useable_data = sheet.get_worksheet(0).get_all_values()[5:]

    # First six columns: Chinese Name, English Name, Address, Area, Status, Detail
    raw_clean_data = [data[:6] for data in useable_data]

    # TODO: see if there's a better way to deal with miscellenous rows
    clean_data = raw_clean_data[:-13]

    formatted_data = [OrganizeData(*market) for market in clean_data]
    formatted_area = _unique_list([market.area for market in formatted_data])

    @app.context_processor
    def inject_options():
        return dict(options=formatted_area)

    @app.route('/', methods=('GET', 'POST'))
    def index():
        if request.method == 'POST':
            filter_value = request.form.get('filter-value')

            if filter_value == 'All':
                results = formatted_data
            else:
                results = [data for data in formatted_data
                           if filter_value in data.area]

            return render_template('index.html', data=results,
                                   filterValue=filter_value)
        return render_template('index.html', data=formatted_data)

    @app.route('/search', methods=('GET', 'POST'))
    def search():
        if request.method == 'POST':
            search_input = request.form.get('search-input')

            search_results = []
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
