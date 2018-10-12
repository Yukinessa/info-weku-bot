import json

class Analisa:
    def __init__(self, text):
        self.text = text

    def command_list(self):
        text = self.text
        cmd_list = open('data/command.txt')
        check = [line.strip() for line in cmd_list]
        for cmd in check:
            if(text.lower()==cmd):
                cmd_detail = open('data/{}.json'.format(cmd))
                data = json.load(cmd_detail)
                break
            else:
                data = None

        if data == None:
            return "Perintah tidak ditemukan"
        return "Perintah ditemukan"

ls = Analisa('mkdir')
cmd = ls.command_list()
print(cmd)