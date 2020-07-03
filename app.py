from flask import render_template, request
from flask import Flask
from random import shuffle
# Job imports
from api_models.models_jobs import model_linkedin, model_ness, model_mploy
# Education imports
from api_models.modles_education import model_udemy, model_campus_gov
import random

app = Flask(__name__)


def get_courses(query):
    full_course_list_to_return = []
    udemy_courses = model_udemy.get_udemy_courses(query)
    campus_courses = model_campus_gov.get_campus_courses(query)
    if udemy_courses:
        for course in udemy_courses:
            full_course_list_to_return.append(course)
    if campus_courses:
        for course in campus_courses:
            full_course_list_to_return.append(course)
    random.shuffle(full_course_list_to_return)
    return full_course_list_to_return


def get_jobs(query):
    """
    This handles the data that should be returned after the jobs search.
    :param query:
    :return:
    """
    full_jobs_list_to_return = []
    ness_jobs = model_ness.get_ness_jobs(query)
    linked_jobs = model_linkedin.get_linkedin_jobs(query, 100)
    mploy_jobs = model_mploy.get_mploy_jobs(query, 100)
    for job in ness_jobs:
        full_jobs_list_to_return.append(job)
    for job in linked_jobs:
        full_jobs_list_to_return.append(job)
    for job in mploy_jobs:
        full_jobs_list_to_return.append(job)
    random.shuffle(full_jobs_list_to_return)
    return full_jobs_list_to_return


@app.route('/', methods=['GET', 'POST'])
def index():
    content = render_template('home.html')
    header = render_template('header.html')
    footer = render_template('footer.html')
    if request.method == 'GET':
        return render_template("index.html", content=content, header=header,
                               footer=footer)
    else:
        query = request.form['search_query']
        if query != '':
            if request.form['option'] == 'course':
                return render_template('index.html',
                                       header=header,
                                       footer=footer,
                                       content=render_template('courses_content.html', data=get_courses(query)))
            elif request.form['option'] == 'job':
                return render_template('index.html',
                                       header=header,
                                       footer=footer,
                                       content=render_template('jobs_content.html', data=get_jobs(query)))
        else:
            return render_template('index.html',
                                   header=header,
                                   footer=footer,
                                   content='No Input...and no pretty page yet.')


@app.route('/about', methods=['GET', 'POST'])
def about_page():
    if request.method == 'POST' or request.method == 'GET':
        return render_template(
            "index.html",
            header=render_template('header.html'),
            content=render_template('about.html'))
    else:
        return render_template("index.html",
                               content=render_template('test_content.html', data=model_mploy.get_mploy_jobs('', 50)),
                               title='HOME')


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


if __name__ == '__main__':
    app.run(debug=True)
