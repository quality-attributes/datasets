
requirements = open('../../1. Text Cleaning/nfr-text.txt', "r").readlines()

for req in requirements:
    if '24x7' in req:
        req = req.replace('24x7', '24 hours per day 365 days per year')
    if '24/7' in req:
        req = req.replace('24/7', '24 hours per day 365 days per year')
    if 'everyday' in req:
        req = req.replace('everyday', 'every day')
    if 'sec(s)' in req:
        req = req.replace('sec(s)', 'seconds')
    if 'min(s)' in req:
        req = req.replace('min(s)', 'minutes')

with open('../pre-tag.txt', 'w') as f:
    for line in requirements:
        f.write(line)