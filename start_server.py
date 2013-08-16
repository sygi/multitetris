#!/usr/bin/env python

from multitetris.backend import main
from sys import argv

if len(argv) > 1:
    try:
        main.run((argv[1], int(argv[2])))
    except:
        print "invalid argument"
else:
    main.run()
