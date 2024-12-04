q1 = input('SURVEY Are you interested in computer science? (y/n):')
q2 = input('Do you like playing computer games? (y/n):')
q3 = input('Do you have an Instagram account? (y/n):')

if q1 == 'y': q1 = True
else: q1 = False

if q2 == 'y': q2 = True
else: q2 = False

if q3 == 'y': q3 = True
else: q3 = False

print(f'SURVEY RESULTS \nInterested in computer science: {q1} \nPlaying computer games: {q2} \nHas an Instagram account: {q3}')