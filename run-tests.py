#!/usr/bin/env python

import imp
import os

def is_python_test(filename):
    return os.path.splitext(filename)[1] == '.py' and filename.lower().startswith('test')

current_directory = os.path.dirname(os.path.abspath(__file__))

for (dirpath, dirname, filenames) in os.walk(current_directory):
    for filename in filenames:
        if is_python_test(filename):
            relpath = os.path.relpath(os.path.join(dirpath, filename), current_directory)
            test = __import__(os.path.splitext(relpath)[0].replace('/', '.').replace('\\', '.'), fromlist='main')
            print 'Running tests in %s' % relpath
            test.main()
