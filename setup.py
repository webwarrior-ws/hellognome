rom setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

requirements = [

]

test_requirements = [

]

setup(
    name='hellognome',
    version='0.1a',
    description='Test Python3 and Gtk3 with the gnome extension',
    long_description=readme,
    author='Luis Louro',
    author_email='lapisdecor@gmail.com',
    url='https://github.com/lapisdecor/hellognome',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=requirements,
    include_package_data=True,
    licence='MIT',
    zip_safe=False,
    keywords='hellognome',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    scripts=['bin/hellognome']
)
