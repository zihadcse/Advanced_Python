village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {"name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}

managing_committee_caniddates = [{"name": "Sultan Ahmed", "age": 43, "occupation": "Service Holder", "designation": "General Member"}, {"name": "Jamsed Khan", "age": 45, "occupation": "Doctor", "designation": "Vice Chairman"}, {"name": "Jahangir Talukder", "age": 47, "occupation": "Doctor", "designation": "Chairman"}, {"name": "Josim Uddin", "age": 38, "occupation": "Farmar", "designation": "Vice Chairman"}]


#output the data type of village_school
village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
print(type(village_school)) 


#output the name of the above school
data =	{
  "name": "Boalia High School",
  "established": 1965,
  "total_teachers": 45,
  "total_students": 658
}
x = data["name"]
print(x)


#try to access "number_of_rooms" key of that school without getting any error
new = data.keys()
data["number_of_rooms"] = "65"
print(new) 
if "number_of_rooms" in data:
  print("For 'number_of_rooms' access are granted")


#change that schools establishment year and make it 1962
data["established"] = 1962
print(data)


#add school_details to village_school
village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
school_details = {"address": "Boalia Bazar", "principal": "Sohidullah Kaisar", "founder": "Johir Raihan", "managing_committee": [{"name": "Sohrab Hossain", "age": 55, "occupation": "Retired person", "designation": "Chairman"}, {"name": "Raisul Islam", "age": 49, "occupation": "Businessman", "designation": "General Member"}, {"name": "Altaf Khan", "age": 33, "occupation": "Founder of Toto Company", "designation": "Vice Chairman"}, {"name": "Sohidul Islam", "age": 45, "occupation": "Businessman", "designation": "General Member"}]}
new_info=dict(village_school,**school_details)
print (new_info)


#check the length of village_school after adding school_details to it
print(len(new_info))


#add number_of_classrooms key with value 25 in village_school dictionary
if "number_of_classrooms" not in village_school:
    village_school["number_of_classrooms"] = "25"
print(village_school)


#check the data type of village_school
print(type(village_school)) 


####loop through all the values of village_school and check if any list type data found there if found print the key name
village_school = {"name": "Boalia High School", "established": 1965, "total_teachers": 45, "total_students": 658}
my_list = []
for i in village_school.values():
    my_list.append(i)
print(my_list)
print(type(my_list))


####output how many members are there in the managing committee
print(len(managing_committee_caniddates))


####check if 'Founder of Toto Company' exist in the managing committee if found then remove that person from the managing committee




###output all the members occupation of the managing committee to check "Founder of Toto Company" is not there



###remove the last added item from the village_school (remember we've a built in function for that)
village_school.popitem()
print(village_school)


#remove the founder of that school
del school_details["founder"]
print(school_details)


###set default value for founder key to "Robiul Islam"
school_details["founder"] = "Robiul Islam"
print(school_details)


#check for a doctor in the 'managing_committee_candidates' list and make sure he wants to be the 'Vice Chairman' of that school if so then add that person to the managing_committe of that school



#output the member of managing_committee after update



#wipe out all the prperties of village_school and make it empty
village_school.clear()
print(village_school)









students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}

a = {8, 4, 3, 3, 2, 7, 5}
b = {1, 4, 9, 20, 34}



#check the data type of students
print(type(students1)) 
print(type(students2)) 


#check the length of students
print(len(students1)) 
print(len(students2)) 


#add "sweety" to students
students1.add("sweety")
students2.add("sweety")
print(students1)
print(students2)


#remove "risat" from students
students1.remove("risat")
print(students1)


#try to safely remove "raihan" from students without facing any error
students1.add("raihan")
print(students1)
students1.remove("raihan")
print(students1)



#add students2 to students1
students2.update(students1)
print(students2)


#check is students2 is the subset of student1
subset = students2.issubset(students1)
print(subset)


#check is students1 is the superset of student2
superset = students1.issuperset(students2)
print(superset)


#clear student1
students1.clear()
students2.clear()
print(students1)
print(students2)


#print all the combined items of student1 and student2, without any duplication (without making any permanent change)
students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}
students=students1.symmetric_difference(students2)
print(students)


#print all the combined items of student1 and student2, with all common values of them (without making any permanent change)
z = students1.intersection(students2) 
print(z)


#print all the combined items of student1 and student2, with all uncommon values of them (without making any permanent change)
students1 = {"shaon", "sufian", "sohrab", "risat", "sohrab", "shaon", "sohan", "romiz"}
students2 = {"kobir", "shaon", "rakib"}
students1.symmetric_difference_update(students2) 
print(students1)


