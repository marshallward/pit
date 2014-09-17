from distutils.core import setup

project_name = 'pit'
project_version = __import__(project_name).__version__
project_readme_fname = 'README.rst'

with open(project_readme_fname) as f:
    project_readme = f.read()

setup(
    name = project_name,
    version = project_version,
    description = 'Numerical model experiment tracker',
    long_description = project_readme,
    maintainer = 'Marshall Ward',
    maintainer_email = 'pit@marshallward.org',
    url = 'http://github.com/marshallward/pit',

    py_modules = ['pit'],

    classifiers = [
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ]
)
