# data structures - why,how ?
# lists

environments = ["dev","production","staging","test"]
print(len(environments)) # lenght of the list is 4 which is 0,1,2,3

environments.append("basiton")

# dictionary

system_info = {
    "name" : "asus notebook",
    "ram" : "16 GB",
    "cpu" : 8,
    "isnew" : True
}

system_info.update({"environment" : environments})
print(system_info.get("name"))

# sets

device_ids = {1,2,3,4,4,4,5,6,6,7,8,9,10} #sets
new_device_ids = {1,2,3,11,12,13,14}
print(device_ids.union(new_device_ids))

# tuples

days_of_week = ("sunday","monday") # the values wont change

# array - not core for python

 


