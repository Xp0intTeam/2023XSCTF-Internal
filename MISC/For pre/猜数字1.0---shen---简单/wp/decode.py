#encode:https://www.audiocheck.net/audiocheck_dtmf.php

import os

origin_code = '1596#38952#73751#4185856'
print (len(origin_code))

result = os.popen('dtmf music.wav').read()
print (result)