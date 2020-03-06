
# Normalize Time expressions
requirements = open('../../1. Text Cleaning/nfr-text.txt', "r").readlines()

for req in range(len(requirements)):
    if '24x7' in requirements[req]:
        requirements[req] = requirements[req].replace('24x7', '24 hours per day 365 days per year')
    if '24/7' in requirements[req]:
        requirements[req] = requirements[req].replace('24/7', '24 hours per day 365 days per year')
    if 'everyday' in requirements[req]:
        requirements[req] = requirements[req].replace('everyday', 'every day')
    if 'sec(s)' in requirements[req]:
        requirements[req] = requirements[req].replace('sec(s)', 'seconds')
    if 'min(s)' in requirements[req]:
        requirements[req] = requirements[req].replace('min(s)', 'minutes')
    if 'uptime' in requirements[req]:
        requirements[req] = requirements[req].replace('uptime', 'up time')

with open('pre-tag.txt', 'w') as f:
    for line in requirements:
        f.write(line)