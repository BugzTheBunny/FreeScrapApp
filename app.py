from flask import render_template, request
from flask import Flask
# Job imports
from api_models.models_jobs import model_linkedin, model_ness, model_mploy
# Education imports
from api_models.modles_education import model_udemy, model_campus_gov

app = Flask(__name__)


def get_courses(query):
    full_course_list_to_return = []
    udemy_courses = model_udemy.get_udemy_courses(query)
    for course in udemy_courses:
        full_course_list_to_return.append(course)
    return full_course_list_to_return


def get_jobs(query):
    return f'{query} THIS'


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
            print('EMPTY STRING')
        return render_template("index.html", data='POTATO', title='BIG POTATO', header=render_template('header.html'))


@app.route('/linkedin', methods=['GET', 'POST'])
def linkedin():
    title = 'LinkedIn'
    if request.method == ['GET']:
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
            header=render_template('header.html'),
            content=render_template('courses_content.html',
                                    data=model_udemy.get_udemy_courses(''), title=title))


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
