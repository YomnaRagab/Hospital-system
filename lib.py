def file_handling(file_name):
    file=open(file_name,'r')
    data=file.read()
    file.close()
    data=data.splitlines()
    return data
def manage_patients():
    patients=dict()
    data=file_handling("data/patients_data.txt")
    for i in data:
        list=i.split(',')
        patients[list[0]]=dict(department=list[1],dr_name=list[2],patinet_name=list[3],
                               patient_age=list[4],patient_gender=list[5],patient_address=list[6],
                               patient_phone_num=list[7],room_num=list[8],describtion=list[9])

    choice=int(input('''1)Add.\n2)Delete.\n3)Edit.\n4)Display\nYour choice: '''))
    if   (choice==1):
        add_new(patients,1)
    elif (choice==2):
        delete (patients,1)
    elif (choice==3):
        edit   (patients,1)
    elif (choice==4):
        display(patients)
    else:
        print("Wrong choice")

def manage_doctors():
    doctors=dict()
    data=file_handling("data/doctors_data.txt")
    for i in data:
        list=i.split(',')
        doctors[list[0]]=dict(dr_department=list[1],dr_name=list[2],dr_address=list[3],
                              dr_phone_num =list[4] )

    choice=int(input('''1)Add.\n2)Delete.\n3)Edit.\n4)Display\nYour choice: '''))
    if   (choice==1):
        add_new (doctors,2)
    elif (choice==2):
        delete  (doctors,2)
    elif (choice==3):
        edit    (doctors,2)
    elif (choice==4):
        display (doctors)
    else:
        print("Wrong choice")

def book_app():
     choice=int(input("1)Book\n2)Edit\n3)Cancel\n\nYour choice: "))
     if   (choice==1) :
         book()
     elif (choice==2) :
         edit_app()
     elif (choice==3) :
         cancel_app()
     else :
         print("Wrong choice")
#####################################################################################################################
def user_display(option):
    data=file_handling("data/doctors_data.txt")
    doctors=dict()
    for i in data:
        list=i.split(',')
        doctors[list[0]]=dict(dr_department=list[1],dr_name=list[2],dr_address=list[3],
                              dr_phone_num =list[4] )
    counter=0
    if(option==1):
        dep_list=[]
        for key in doctors:
            if doctors[key]['dr_department'] not in dep_list:
                dep_list.append(doctors[key]['dr_department'])
                print(doctors[key]['dr_department'])
    elif(option==2):
        for key in doctors:
                if(counter!=0):
                    print('Doctor ID:',key)
                    print('Doctor name:',doctors[key]['dr_name'])
                    print('Doctor department:',doctors[key]['dr_department'])
                    print('Doctor address:',doctors[key]['dr_address'])
                    print('Doctor phone number:',doctors[key]['dr_phone_num'])
                    print("/-------------------------------------------------------------/")
                counter=1


####################################################################################################################
def patient_display_user(option):
    patients=dict()
    data=file_handling("data/patients_data.txt")
    for i in data:
        list=i.split(',')
        patients[list[0]]=dict(department=list[1],dr_name=list[2],patinet_name=list[3],
                               patient_age=list[4],patient_gender=list[5],patient_address=list[6],
                               patient_phone_num=list[7],room_num=list[8],describtion=list[9])
    counter=0
    if option==3:
        for key in patients :
            if(counter!=0):
                print('Patient ID:',key)
                print('Patient name:',patients[key]['patinet_name'])
                print('Department:',patients[key]['department'])
                print('Doctor name:',patients[key]['dr_name'])
                print('Patient age:',patients[key]['patient_age'])
                print('Patient gender:',patients[key]['patient_gender'])
                print('Patient phone number:',patients[key]['patient_phone_num'])
                print('Patient room number:',patients[key]['room_num'])
                print('Describtion:',patients[key]['describtion'])
                print("/-------------------------------------------------------------/")
            counter=1
    elif option==4:
        key=str(input("Enter the ID:"))
        ids      =patients.keys()
        if key in ids:
            print('Patient ID:',key)
            print('Patient name:',patients[key]['patinet_name'])
            print('Department:',patients[key]['department'])
            print('Doctor name:',patients[key]['dr_name'])
            print('Patient age:',patients[key]['patient_age'])
            print('Patient gender:',patients[key]['patient_gender'])
            print('Patient phone number:',patients[key]['patient_phone_num'])
            print('Patient room number:',patients[key]['room_num'])
            print('Describtion:',patients[key]['describtion'])
        else :
            print("ID doesn't exist")

############################################################################################
def dr_appointments():
    data=file_handling("data/available_app.txt")
    available=dict()
    available=availableTimeFileHandling(data)

    data=file_handling("data/appointments_data.txt")
    appointments=dict()
    for i in data:
        list=i.split(',')
        appointments[list[0]]=dict(department =list[1],dr_name       =list[2],patinet_name   =list[3],
                                   patient_age=list[4],patient_gender=list[5],appointment_day=list[6],
                                   appointment_time=list[7])

    key=str(input("Enter the ID:"))
    ids      =available.keys()
    app_list=[]
    if key in ids:
        app_list,length=available_times_display(available,key)
        for i in appointments:
            if ((available[key]['dr_name'] in appointments[i].values()) and (available[key]['department'] in appointments[i].values())):
                print("in",appointments[i]['appointment_day'],"at",appointments[i]['appointment_time'],"is reserved")


############################################################################################


def add_new(myDic,target):

    depart   =str(input("Enter the deprtment: "))
    dr_n     =str(input("Enter the dr name: "  ))
    if target ==1 : #patients
        print("Enter the basic information for the patient")
        name     =str(input("Name: "              ))
        age      =str(input("Age: "               ))
        gender   =str(input("Gender: "            ))
        room_no  =str(input("Room number: "       ))
        describ  =str(input("Describtion: "       ))
    address  =str(input("Address: "           ))
    phone_num=str(input("Phone number: "      ))
    id       =str(input("ID: "                ))
    ids=myDic.keys()
    while id in ids:
        print("ID must be unique , please try again")
        id=str(input("ID: "))
    if target==1: #patient
        myDic[id]=dict(department=depart,dr_name=dr_n,patinet_name=name,
                       patient_age=age,patient_gender=gender,patient_address=address,
                       patient_phone_num=phone_num,room_num=room_no,describtion=describ)
        Update_data("data/patients_data.txt",myDic)
    if target==2: #doctors
        myDic[id]=dict(dr_department=depart,dr_name=dr_n,dr_address=address,
                       dr_phone_num =phone_num )
        Update_data("data/doctors_data.txt",myDic)


def delete(myDic,target):
    id=str(input("Enter the ID: "))
    ids=myDic.keys()
    if id in ids:
        myDic.pop(id)
        if target==1:
            print("The patient was deleted")
            Update_data("data/patients_data.txt",myDic)
        else:
            print("The doctor was deleted")
            Update_data("data/doctors_data.txt",myDic)
    else:
        print("The ID is not exist")

def edit(myDic,target):
    id=str(input("Enter the ID: "))
    ids=myDic.keys()
    if id in ids:
        print(myDic[id])
        depart   =str(input("Enter the deprtment:"))
        dr_n     =str(input("Enter the dr name:"  ))
        if(target==1):
            print("Enter the basic information for the patient")
            name     =str(input("Name: "              ))
            age      =str(input("Age: "               ))
            gender   =str(input("Gender: "            ))
            room_no  =str(input("Room number: "       ))
            describ  =str(input("Describtion: "       ))
        address  =str(input("Address: "           ))
        phone_num=str(input("Phone number: "      ))
        if target==1:
            myDic[id]=dict(department=depart,dr_name=dr_n,patinet_name=name,
                              patient_age=age,patient_gender=gender,patient_address=address,
                              patient_phone_num=phone_num,room_num=room_no,describtion=describ)
            Update_data("data/patients_data.txt",myDic)
        else:
            myDic[id]=dict(dr_department=depart,dr_name=dr_n,dr_address=address,
                           dr_phone_num =phone_num )
            Update_data("data/doctors_data.txt",myDic)

    else :
        print("ID is not exist")

def display(myDic):
    choice=int(input("1)Display all.\n2)Display with an ID\nYour choice: "))
    data=str()
    if choice==1:
        for i in myDic :
            diplay_id(myDic,i)
    elif choice==2:
        id=str(input("Enter the ID: "))
        ids=myDic.keys()
        if id in ids:
            diplay_id(myDic,id)


def Update_data(file_name,myDic):
    file=open(file_name,'w')
    for i in myDic:
        file.write(str(i)) #write key
        for i in myDic[str(i)].values():
            file.write(','+str(i))
        file.write('\n')

def diplay_id(myDic,id):
    data=str()
    for j in myDic[str(id)].values():
        data=data+' '+str(j)
    print(id+data)
########################################################################################33
def book():
    data=file_handling("data/appointments_data.txt")
    appointments=dict()
    for i in data:
        list=i.split(',')
        appointments[list[0]]=dict(department =list[1],dr_name       =list[2],patinet_name   =list[3],
                                   patient_age=list[4],patient_gender=list[5],appointment_day=list[6],
                                   appointment_time=list[7])
    dep      =str(input("Enter the deprtment:")).lower()
    dr_n     =str(input("Enter the dr name:"  )).lower()
    print("Enter the basic information of the patient")
    name     =str(input("Name: "              ))
    age      =str(input("Age: "               ))
    gender   =str(input("Gender: "            ))
    id       =str(input("ID: "                ))
    ids      =appointments.keys()
    while id in ids:
        print("ID must be unique , please try again")
        id=str(input("ID: "))

    data=file_handling("data/available_app.txt")
    available=dict()
    available=availableTimeFileHandling(data)

    flag_dr_exist=0
    app_list=[]
    for key in available :
        if (dr_n in available[key].values()) and (dep in available[key].values()):
            flag_dr_exist=1
            app_list,length=available_times_display(available,key)
            choice=int(input("Your choice: "))
            if(choice>length-1):
                print("Error choice!")
            else:
                available[app_list[choice][2]][app_list[choice][0]].remove(app_list[choice][1]) #remove the time from available
                update_available_appointment(available)
                appointments[id]=dict(department =dep,dr_name       =dr_n  ,patinet_name   =name,
                                      patient_age=age,patient_gender=gender,appointment_day=app_list[choice][3],
                                      appointment_time=app_list[choice][1])
                Update_data("data/appointments_data.txt",appointments)
                #app_list[choice][0]#day
                #app_list[choice][1]#time

    if (flag_dr_exist==0):
            print("The doctor data is wrong")
###############################################################################################################
def edit_app():
     data=file_handling("data/appointments_data.txt")
     appointments=dict()
     for i in data:
        list=i.split(',')
        appointments[list[0]]=dict(department =list[1],dr_name       =list[2],patinet_name   =list[3],
                                   patient_age=list[4],patient_gender=list[5],appointment_day=list[6],
                                   appointment_time=list[7])
     id=str(input("Enter the ID:"))
     ids      =appointments.keys()
     if id in ids:
         diplay_id(appointments,id)
         data=file_handling("data/available_app.txt")
         available=dict()
         available=availableTimeFileHandling(data)

         app_list=[]
         for key in available :
             if (appointments[id]['dr_name'] in available[key].values()):
                 app_list,length=available_times_display(available,key)
                 choice=int(input("Your choice: "))
                 if(choice>length-1):
                     print("Error choice!")
                 else:
                     available[app_list[choice][2]][app_list[choice][0]].remove(app_list[choice][1]) #remove the time from available
                     available[app_list[choice][2]][app_list[choice][0]].append(appointments[id]['appointment_time'])
                     update_available_appointment(available)
                     appointments[id] =dict(department      =appointments[id]['department']    ,dr_name        =appointments[id]['dr_name']     ,
                                            patinet_name    =appointments[id]['patinet_name']  ,patient_age    =appointments[id]['patient_age'] ,
                                            patient_gender  =appointments[id]['patient_gender'],appointment_day=app_list[choice][3],
                                            appointment_time=app_list[choice][1])
                     Update_data("data/appointments_data.txt",appointments)
     else:
         print("ID doesn't exist")
##############################################################################################################
def cancel_app():
     data=file_handling("data/appointments_data.txt")
     appointments=dict()
     for i in data:
        list=i.split(',')
        appointments[list[0]]=dict(department =list[1],dr_name       =list[2],patinet_name   =list[3],
                                   patient_age=list[4],patient_gender=list[5],appointment_day=list[6],
                                   appointment_time=list[7])
     id=str(input("Enter the ID:"))
     ids      =appointments.keys()
     if id in ids:
         diplay_id(appointments,id)
         data=file_handling("data/available_app.txt")
         available=dict()
         available=availableTimeFileHandling(data)
         app_list=[]
         for key in available :
             if (appointments[id]['dr_name'] in available[key].values()):
                if appointments[id]['appointment_day']==available[key]['available_day1']:
                     available[key]['available_times1'].append(appointments[id]['appointment_time'])
                elif appointments[id]['appointment_day']==available[key]['available_day2']:
                    available[key]['available_times2'].append(appointments[id]['appointment_time'])
                break
         appointments.pop(id)
         Update_data("data/appointments_data.txt",appointments)
         update_available_appointment(available)

     else :
         print("ID doens't exist")


##############################################################################################################
def availableTimeFileHandling(data):
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
    available=dict()
    counter=0
    start1=start2=end1=end2=day1=day2=0
    for i in data:
        list=i.split(',')
        counter=0
        for day in days:
            if day in list:
                counter=counter+1
                start=list.index(day)
                end=list.index('#')
                if(end<start):
                    end=list.index('##')
                if counter==1:
                    start1=start
                    end1=end
                    day1=day
                elif counter==2:
                    start2=start
                    end2=end
                    day2=day
        if(counter==2):
            available[list[0]]=dict(dr_name=list[1],department=list[2],available_day1=day1,
                                    available_times1=list[start1+1:end1],available_day2=day2,
                                    available_times2=list[start2+1:end2])

        elif(counter==1):
            available[list[0]]=dict(dr_name=list[1],department=list[2],available_day1=day1,
                                    available_times1=list[start1+1:end1])
    return(available)
##################################################################################################
def available_times_display(myDic,key):
    app_list=[]
    length=length1=len(myDic[key]['available_times1'])
    if 'available_day2' in myDic[key].keys():
        length2=len(myDic[key]['available_times2'])
        length=length1+length2
    print ("Availables appointment:")
    i=0
    for choice in myDic[key]['available_times1'] :
        print (i,')',"In",myDic[key]['available_day1'],"at",choice)
        app_list.append(['available_times1',choice,key,myDic[key]['available_day1']])
        i=i+1
    if 'available_day2' in myDic[key].keys():
        for choice in myDic[key]['available_times2'] :
            print (i,')',"In",myDic[key]['available_day2'],"at",choice)
            app_list.append(['available_times2',choice,key,myDic[key]['available_day2']])
            i=i+1
    return app_list,length

###################################################################################################

def update_available_appointment(myDic):
    file=open("data/available_app.txt",'w')
    for i in myDic:
        file.write(str(i))
        counter=0
        count=0
        flag=0
        days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday']
        for i in myDic[str(i)].values():
            #to handle the list of the avaialable times
            if flag ==1:
                str1=str()
                for word in i:
                    str1=word+','+str1 #time , time ,time
                i=str1[:len(str1)-1]
                flag=0
            #to handle the # after the first day with its avaialble times
            for day in days:
                if day == str(i):
                    counter=counter+1
                    count=counter
                    flag=1
            if counter ==2:
                file.write(',#')
                count=counter
                counter=0
            file.write(','+str(i))

        #at the end of the line , put # if it was only one day , and ## if they were
        if count ==2:
            file.write(',##')
        elif count==1:
            file.write(',#')
        file.write('\n')
