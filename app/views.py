from flask import render_template, request
from app import app
from app.api_models.models_jobs import model_linkedin
from app.api_models.models_jobs import model_mploy
from app.api_models.models_jobs import model_ness


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html", content=render_template('home.html'), title='HOME')
    else:
        return render_template("index.html", data='POTATO', title='BIG POTATO')


@app.route('/linkedin', methods=['GET', 'POST'])
def linkedin():
    title = 'Linked in Jobs..'
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_linkedin.get_linkedin_jobs(request.form['query_to_search'], 50)),
            title=title)
    else:
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_linkedin.get_linkedin_jobs('', 50)),
            title=title)


@app.route('/mploy', methods=['GET', 'POST'])
def mploy():
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_mploy.get_mploy_jobs(request.form['query_to_search'], 50)),
            title='HOME')
    else:
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_mploy.get_mploy_jobs('', 50)),
            title='HOME')


@app.route('/ness', methods=['GET', 'POST'])
def ness():
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_ness.get_ness_jobs(request.form['query_to_search'])),
            title='HOME')
    else:
        return render_template("index.html",
                               content=render_template('jobs_content.html', data=model_ness.get_ness_jobs(''),
                                                       title='HOME'))


@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('test_content.html',
                                    data=model_mploy.get_mploy_jobs(request.form['query_to_search'], 50)),
            title='HOME')
    else:
        return render_template("index.html",
                               content=render_template('test_content.html', data=model_mploy.get_mploy_jobs('', 50)),
                               title='HOME')
