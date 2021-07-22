import json


def get_cookies_address(sId):
    return "UsrLib/" + sId + '.pkl'


class Students:
    with open("UsrLib/Usr.json", 'r') as usr:
        studentDict = json.loads(usr.read())
    usr.close()

    def __update_database(self):
        with open("UsrLib/Usr.json", 'w') as usr:
            usr.write(json.dumps(self.studentDict))
        usr.close()

    def get_pwd_by_id(self, sId):
        return self.studentDict[sId]['pwd']

    def add_student(self, sId, sPwd):
        self.studentDict[sId] = {
            "pwd": sPwd,
        }
        self.__update_database()

    def remove_student(self, sId):
        self.studentDict.pop(sId)
        self.__update_database()

    def change_pwd(self, sId, pwd):
        self.studentDict[sId] = {
            "pwd": pwd
        }
        self.__update_database()

    def get_sId_list(self):
        return self.studentDict.keys()
