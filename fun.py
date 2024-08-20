from json import*

FILE="data/stud.json"


def read_json():
    try:
        with open(FILE) as f:
            data=load(f)
        return data
    except:
        with open(FILE,"w") as f:
            data={"students":[]}
            dump(data,f,indent=3)
        return data
             
def write_json(data):
    with open(FILE,"w") as f:
        dump(data,f,indent=3)