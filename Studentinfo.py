import csv

def write_info_csv(info_list):
    with open('student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        if csv_file.tell()== 0:
            writer.writerow(["Name", "Age", "Contact number", "E-mail ID"])
        
        writer.writerow(info_list)
        
        
if __name__ == '__main__':        
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter student info for student #{} in the following format (Name Age Contact_Nymber E-mail_ID): ")
        
        #split 

        student_info_list = student_info.split(' ')
        
        print ("\nThe enterened information is- \nName: {}\nRoll_number: {}\nContact_number : {}\nE_mail_id: {}"
               .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
        
        
        choice_check = input("Is the entered information correct? (yes/no)")
        
        if choice_check == "yes":
            write_info_csv(student_info_list)
            condi_check = input ("Enter (yes/no) if you want to enter information for another student: ")
            if condi_check == "yes":
                condition = True
                student_num =student_num +1
            else:
                condition = False
        
        else:
            print ('\nPlease re enter the values!')
