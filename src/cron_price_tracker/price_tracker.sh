SHELL=/bin/bash
source /home/ubuntu/env/bin/activate
cd /home/ubuntu/TrackPrice/src
python manage.py runscript monitor_price
