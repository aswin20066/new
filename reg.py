from fun import*

def registration(name,age,address,course):
    data=read_json()
    temp_dict={
        "sno":len(data["students"])+1,
        "name":name,
        "age":age,
        "address":address,
        "course":course
    }
    data["students"].append(temp_dict)
    write_json(data)
    
    
def delete_stud(id):
    data=read_json()
    for stud in data["students"]:
        if str(stud["sno"])==id:
            data["students"].remove(stud)
            break
        
    i=1
    for stud in data["students"]:
        stud["sno"]=i
        i+=1
    write_json(data)
    
def update_stud(id,name,age,address,course):
    data=read_json()
    for stud in data["students"]:
         if str(stud["sno"])==id:
             stud["name"]=name
             stud["age"]=age
             stud["address"]=address
             stud["course"]=course
             break
    
    write_json(data)
            