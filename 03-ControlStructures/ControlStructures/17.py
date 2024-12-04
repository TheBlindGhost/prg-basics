time = input('What time is it?')

format_time = int(time[0:2])
post = ''


if format_time > 12:
    format_time -= 12
    post = 'pm'
else:
    post = 'am'

print(f' It is {format_time} : {time[3:6]} {post}')