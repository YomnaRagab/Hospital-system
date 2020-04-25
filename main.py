import lib


while 1:

    choice=int(input('''**********Welcome to Yomna's hospital*********

1)Admin mode.
2)User mode.

Your choice:'''))
    if choice==1:
        psw=str(input("Enter the password: "))
        i=1
        while (i<3):
            if psw!='1234':
                psw=str(input("Please enter the correct password: "))
                i+=1
            else:
                break
        if(i==3):
            print("\n****Blocked for now*****\nPlease try again later")
            break
        else:
            while(1):
                choice=int(input(
'''
**Hello admin**
1)Manage patients.
2)Manage doctors.
3)Book an appointment.
4)Exit.
Your choice: '''))
                if   (choice==1):
                    lib.manage_patients()
                elif (choice==2):
                    lib.manage_doctors()
                elif (choice==3):
                    lib.book_app()
                elif (choice==4):
                    break
                else:
                    print("Wrong choice")
    elif (choice==2):
        print(
'''1- View all departments.
2- View all doctors.
3- View all patients Residents in a hospital.
4- Enter the patient's ID to view the patient details
5- Enter the doctor's ID to view an appointments'''
            )
        viewer_option=int(input("\nYour choice: "))
        if     (viewer_option==1) or (viewer_option==2):
            lib.user_display(viewer_option)
        elif   (viewer_option==3)or(viewer_option==4):
            lib.patient_display_user(viewer_option)
        elif   (viewer_option==5):
            lib.dr_appointments()
        else :
            print("Error choice!")
