car_speed = int(input('How fast are you driving?')) 
speed_limit_min = 40
speed_limit_max = 140

if car_speed < speed_limit_min or car_speed > 140:
    print('Warning: invalid car speed!!')
else:
    print('Your speed is good!!!')