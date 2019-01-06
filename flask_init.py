import os
import sys
import shutil


def create_proj_dir(dir_path):
    try:
        os.mkdir(dir_path)
    except OSError as _:
        response = input("This project name is already in use. Type 'DELETE' to overwrite."
                         " NOTE: All existing data will be overwritten. \n")

        if response == "DELETE":
            shutil.rmtree(dir_path)
            os.mkdir(dir_path)
        else:
            print("Please try again with an unused project directory.")
            sys.exit()


def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except OSError as e:
        raise e


def copy_file_template(destination_path, template_path):
    shutil.copy2(template_path, destination_path)


# create a folder for the project and add appropriate sub folders
cwd = os.getcwd()
proj_name = sys.argv[1]
proj_path = cwd + "/{}".format(proj_name)
app_path = proj_path + "/source"
template_path = "/Users/andrewlaird/PycharmProjects/dev_scripts/templates/basic_flask_app/"
create_proj_dir(proj_path)
create_dir(app_path)
create_dir(app_path + "/templates")
create_dir(app_path + "/static")
create_dir(app_path + "/static/css")
create_dir(app_path + "/static/js")

# create basic file structure
copy_file_template(proj_path, template_path + "/setup.py")
copy_file_template(app_path, template_path + "/views.py")
copy_file_template(app_path, template_path + "/__init__.py")
copy_file_template(app_path + "/static/css", template_path + "/core.css")
copy_file_template(app_path + "/static/js", template_path + "/core.js")
copy_file_template(app_path + "/templates", template_path + "/core.html")

# TODO: set up sass
# set up venv
# TODO: set up mysql
# install packages
# set up git
# commit and push project to github

# python flask_init.py [project_name]


