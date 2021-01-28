"""Compute the naturalness of a phrase using
Google Search and Translate.
"""

__author__ = 'chrislgarry@gmail.com (Chris Garry)'

import sys, locale
from flask import Flask, render_template, request, redirect
from googleapiclient.discovery import build


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/search', methods=['GET'])
def search():

    # Build a service object to interact with the CustomSearch API.
    service = build("customsearch", "v1", developerKey="")
    query = request.args.get('q')

    response = service.cse().list(
        q=query,
        cx='',
        lr='lang_ja',
        cr='countryJP',
        exactTerms=query
    ).execute()
 
    return render_template(
        'search.html',
        results=response['searchInformation']['totalResults'])


@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]
