import usrLib
import eventRec

students = usrLib.Students()

print("id          Code")
print("------------------------")
for sId in students.get_sId_list():
    print(str(sId) + "          " + students.get_pwd_by_id(sId))
print("------------------------")
print("del [id]: 删除学生\n"
      "add [id] [pwd]: 增加学生\n"
      "cp [id] [pwd]: 修改密码\n"
      "exit: 结束")

whitelist = ['del', 'add', 'cp', 'exit']
while True:
    ip = str(input("\n<<<")).split(" ")
    if ip[0] in whitelist:
        if ip[0] == "del":
            if ip[1] not in students.get_sId_list():
                print("-->未能找到匹配的学生")
                continue
            else:
                students.remove_student(ip[1])
                eventRec.ok_msg(msg="remove user: " + ip[1])
        elif ip[0] == "add" and len(ip) == 3:
            students.add_student(ip[1], ip[2])
            eventRec.ok_msg(msg="add user: " + ip[1])
        elif ip[0] == "cp" and len(ip) == 3:
            if ip[1] not in students.get_sId_list():
                print("-->未能找到匹配的学生")
                continue
            students.change_pwd(ip[1], ip[2])
            eventRec.ok_msg(ip[1], "change pwd")
        elif ip[0] == "exit":
            break
        else:
            print("-->请输入正确的指令")
            continue
        print("\nid          Code")
        print("------------------------")
        for sId in students.get_sId_list():
            print(str(sId) + "          " + students.get_pwd_by_id(sId))
        print("------------------------")
    else:
        print("-->请输入正确的指令")
