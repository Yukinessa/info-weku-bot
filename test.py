import json

def command_list(text):
    cmd_list = open('data/command.txt')
    check = [line.strip() for line in cmd_list]
    for cmd in check:
        if(text.lower()==cmd):
            cmd_detail = open('data/{}.json'.format(cmd))
    data = json.load(cmd_detail)
    return data

ls = command_list('ls')
print(ls['nama'])