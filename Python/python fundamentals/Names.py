students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def Names_1(list):
    for element in list:
        str = element.values()
        print " , ".join(str)


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }




def  Names_2(dict):
    key_1 = dict.keys()
    value_1 = dict.values()
    for count in range(len(dict)):
        print key_1[count]
        for n in range(len(value_1)):
            for j in range(len(value_1[n])):
                value_2 = value_1[n]
                value_3 = value_2[j].values()
                string = str(n+1)
                sum = 0
                for m in range(len(value_3)):
                    string += " - " +value_3[m]
                    sum += len(value_3[m])
                string += " - " + str(sum)
                print string



Names_2(users)
