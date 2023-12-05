import os

PROJECT_DIRECTORY = os.getcwd()


if __name__ == '__main__':

    # post-gen Configuration
    if ('{{cookiecutter.is_there_a_github_repository}}' == 'yes') \
        & ('{{cookiecutter.package_manager}}' == 'Poetry'):

        os.system('bash --rcfile post-gen.sh')