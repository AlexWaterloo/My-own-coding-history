def userid(fname, midname,lastname):
    temp_id = fname[0]+midname[0:1]+lastname
    temp_id = temp_id.lower()
    return temp_id[0:8]
print(userid("Harry","","Potter"))

