# -*- coding: utf-8 -*-

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=core,authentication,importer',
    '--cover-erase',
    # '--exe',
    # '--with-doctest',
    # '--all-modules',
    # '--logging-clear-handlers',
    # '-d', # Add detail to error output
    # '--cover-html',
    # '-s', # print stdout
    # '--cover-tests', # test tests
    '--nologcapture',
    '--verbosity=2',
    '--cover-package=busineme, api',
    # '--cover-min-percentage=80',
]
