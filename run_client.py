#!/usr/bin/env python
import sys, os
sys.path.append(os.path.dirname(__file__))

import multitetris.frontend.running_game as game
if len(sys.argv) > 1:
    game.run(sys.argv[1])
else:
    game.run()
