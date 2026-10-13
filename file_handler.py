
def file_writer(data:list)->str:
    with open("data.txt","a") as f:
        f.writelines(data)
        f.writelines('\n')
    return "done"

    




