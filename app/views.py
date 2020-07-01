from flask import render_template, request
from app import app
# Job imports
from app.api_models.models_jobs import model_linkedin
from app.api_models.models_jobs import model_mploy
from app.api_models.models_jobs import model_ness
# Education imports
from app.api_models.modles_education import model_campus_gov
from app.api_models.modles_education import model_udemy


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html", content=render_template('home.html'), title='HOME')
    else:
        return render_template("index.html", data='POTATO', title='BIG POTATO')


@app.route('/linkedin', methods=['GET', 'POST'])
def linkedin():
    title = 'Linked'
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_linkedin.get_linkedin_jobs(request.form['query_to_search'], 100)),
            title=title)
    else:
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_linkedin.get_linkedin_jobs('', 100)),
            title=title)


@app.route('/mploy', methods=['GET', 'POST'])
def mploy():
    title = 'MPloy'
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_mploy.get_mploy_jobs(request.form['query_to_search'], 100)),
            title=title)
    else:
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_mploy.get_mploy_jobs('', 100)),
            title=title)


@app.route('/ness', methods=['GET', 'POST'])
def ness():
    title = 'Ness'
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('jobs_content.html',
                                    data=model_ness.get_ness_jobs(request.form['query_to_search'])),
            title=title)
    else:
        return render_template("index.html",
                               content=render_template('jobs_content.html', data=model_ness.get_ness_jobs(''),
                                                       title=title))


@app.route('/campus', methods=['GET', 'POST'])
def campus():
    title = 'Campus'
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('courses_content.html',
                                    data=model_campus_gov.get_campus_courses(request.form['query_to_search']),
                                    title=title))
    else:
        return render_template(
            "index.html",
            content=render_template('courses_content.html',
                                    data=model_campus_gov.get_campus_courses(''), title=title))


@app.route('/udemy', methods=['GET', 'POST'])
def udemy():
    title = 'Udemy'
    if request.method == 'POST':
        return render_template(
            "index.html",
            content=render_template('courses_content.html',
                                    data=model_udemy.get_udemy_courses(request.form['query_to_search']),
                                    title=title))
    else:
        return render_template(
            "index.html",
            content=render_template('courses_content.html',
                                    data=model_udemy.get_udemy_courses(''), title=title))


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
