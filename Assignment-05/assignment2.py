# import csv
# class PatientManagement:

#   """ 
#   CONSTRUCTOR WILL REQUEST FOR THE FILE NAME AND INITIALISES ALL THE VARIABLES
#   """
#   def __init__(self):
#     print("Welcome to UB patient management system")
#     self.patient_dict = {}
#     self.file_name = input("Enter the file Name: ")
#     self.read_patients_file(self.file_name)
#     global d
#     d = {}
  


#   """ 
#   THIS METHOD SHOULD READ DATA FROM FILE AND INTIALISE THE MAIN METHOD
#   """
#   def read_patients_file(self, file_name):
#     fulldata = []
#     with open(file_name, newline = "") as infile: #open the file to read
#       data = csv.reader(infile)
#       for row in data :
#         fulldata.append(row)
#       for i in range(len(fulldata)):  
#         d[i] = fulldata[i]
      
#       print("Loaded {} records from file.".format(len(fulldata)))
#       infile.close()
#     self.main_menu()
  


#   """ 
#   THIS METHOD SHOULD DISPLAY MAIN MENU AND SHOULD HANDLE ALL THE MENU OPERATIONS
#   """
#   def main_menu(self):
#     print("##################################################")
#     print("#######             MAIN MENU              #######")
#     print("##################################################")
#     print("#######  1.Add Patient                     #######")
#     print("#######  2.View Patient at specific Index  #######")
#     print("#######  3.View all Patients               #######")
#     print("#######  4.Search for Patient              #######")
#     print("#######  5.Exit                            #######")
#     print("##################################################\n")
    
#     option = input("Select an Option : ")
    
#     if(option == '1'):
#       self.add_patient()
#     elif(option == '2'):
#       print("No. of patients in Patient Directory are : {} ,select any index from 0 till {}".format(len(d),len(d)-1))
#       ind_to_returned=int(input("Enter the index number : "))
#       self.find_patient_at_index(ind_to_returned)
#     elif(option == '3'):
#       self.show_all()
#     elif(option == '4'):
#       self.find_patient_with_name()
#     elif(option == '5'):
#       self.call_exit()
#     else:
#       print ("Invalid Choice.. Try Again with valid choices..")
#       self.main_menu()
 


#   """ 
#   THIS METHOD SHOULD ADD DATA INTO PATIENT DICTONARY
#   """
#   def add_patient(self):
#     data = []
#     name = input("Enter Name to be added: ")
#     data.append(name)
#     SSN  = input("Enter SSN  to be added: ")
#     data.append(SSN)
#     age  = input("Enter Age  to be added: ")
#     data.append(age)
#     diagnosis = input("Enter Diagnosis to be added: ")
#     data.append(diagnosis)
#     d[len(d)] = data
    
#     print (d)
#     print("\nNew Record Added\n")
#     self.main_menu()



#   """ 
#   THIS METHOD SHOULD RETRIEVE THE DATA AT SPECIFIED INDEX
#   """
#   def find_patient_at_index(self,ind_to_returned):
#     if(ind_to_returned<=len(d)-1):
#       print("--------------------------------------------------------------------------------")
#       print("{:15} {:15} {:15} {:15}".format("NAME", "SSN", "AGE", "DIAGNOSIS"))
#       print("--------------------------------------------------------------------------------")
#       info = d[ind_to_returned]
#       print(''.join(['{:16}'.format(item) for item in info]))
#     else:
#       print("Invalid Patient Index..")
#       print("No. of patients in Patient Directory are : {} ,select any index from 0 till {}".format(len(d),len(d)-1))
#       ind_to_returned=int(input("Enter the index number : "))
#       self.find_patient_at_index(ind_to_returned)
    
#     self.main_menu()



#   """ 
#   THIS3 METHOD SHOULD SHOW ALL RECORDS IN DICTIONARY
#   """
#   def show_all(self):
#     print("--------------------------------------------------------------------------------")
#     print("{:15} {:15} {:15} {:15}".format("NAME", "SSN", "AGE", "DIAGNOSIS"))
#     print("--------------------------------------------------------------------------------")
#     #print('\n'.join([''.join(['{:16}'.format(item) for item in row]) for row in fulldata]))
#     for data in d.values():
#       #print(data)
#       print(''.join(['{:16}'.format(item) for item in data]))
#     print()
#     self.main_menu()



#   """ 
#   THIS METHOD SHOULD RETRIEVE THE RECORD WITH USER NAME
#   """
#   def find_patient_with_name(self):
#     name = input("Enter the Patient to be searched with Name: ")
#     temp = 0
#     for i in range(0,len(d)):
#       for j in range(0,4):
#         if name in d[i][j]:
#           print("--------------------------------------------------------------------------------")
#           print("{:15} {:15} {:15} {:15}".format("NAME", "SSN", "AGE", "DIAGNOSIS"))
#           print("--------------------------------------------------------------------------------")
#           print(''.join(['{:16}'.format(item) for item in d[i]]))
#           temp = 1
#     if(temp==0):
#       print("No results found")
#     self.main_menu()



#   """ 
#   THIS METHOD WRITES NEWLY ADDED DATA INTO TEXT FILE AND EXIT FROM LOOP
#   """
#   def call_exit(self):
#     with open(self.file_name, "w") as outfile:  #open the file to read
#       writer = csv.writer(outfile)
#       for data in d.values():
#         writer.writerow(data)
#     outfile.close()
#     return 0


# pm = PatientManagement()


# TODO: complete this class

import csv

class PatientManagement:
    """
    CONSTRUCTOR WILL REQUEST FOR THE FILE NAME AND INITIALISES ALL THE VARIABLES
    """

    def __init__(self):
        print("Welcome to UB patient management system")
        self.patient_dict = {}
        self.file_name = input("Enter the file Name: ")
        self.read_patients_file(self.file_name.replace(" ",""))

    """ 
    THIS METHOD SHOULD READ DATA FROM FILE AND INTIALISE THE MAIN METHOD
    """

    def read_patients_file(self, file_name):
        fulldata = []
        global dictionary  # global declaration of dictionary
        dictionary = {}
        try:
            with open(file_name, newline="") as infile:  # open the file from which you want to read
                data = csv.reader(infile)
                for row in data:
                    fulldata.append(row)
                for i in range(len(fulldata)):
                    dictionary[i] = fulldata[i]
            print("Loaded {} records from file.".format(len(fulldata)))
            infile.close()
            self.main_menu()
        except FileNotFoundError:  # exception handling if file is not found on the disk.
            print("Couldn't find the file")
            return 0
        except OSError:  # exception handling if file is not readable.
            print("File Found - Problem reading the file")
            return 0
        except SyntaxError:  # eception handling if program has any syntax error.
            print("SyntaxError")
            return 0

    """ 
    THIS METHOD SHOULD DISPLAY MAIN MENU AND SHOULD HANDLE ALL THE MENU OPERATIONS
    """

    def main_menu(self):  # menu to display
        print("##################################################")
        print("#######             MAIN MENU              #######")
        print("##################################################")
        print("#######  1.Add Patient                     #######")
        print("#######  2.View Patient at specific Index  #######")
        print("#######  3.View all Patients               #######")
        print("#######  4.Search for Patient              #######")
        print("#######  5.Exit                            #######")
        print("##################################################\n")

        option = input("Select an Option : ")

        if (option == '1'):  # options handling using if else ladder
            self.add_patient()
        elif (option == '2'):
            print(
                "No. of patients in Patient Directory are : {} ,select any index from 0 till {}".format(len(dictionary),
                                                                                                        len(
                                                                                                            dictionary) - 1))
            ind_to_returned = int(input("Enter the index number : "))
            self.find_patient_at_index(ind_to_returned)
        elif (option == '3'):
            self.show_all()
        elif (option == '4'):
            self.find_patient_with_name()
        elif (option == '5'):
            self.call_exit()
        else:
            print("Invalid Choice.. Try Again with valid choices..")
            self.main_menu()

    """ 
    THIS METHOD SHOULD ADD DATA INTO PATIENT DICTONARY
    """

    def add_patient(self):
        data = []
        name = input("Enter Name to be added: ")
        data.append(name)
        SSN = input("Enter SSN  to be added: ")
        data.append(SSN)
        age = input("Enter Age  to be added: ")
        data.append(age)
        diagnosis = input("Enter Diagnosis to be added: ")
        data.append(diagnosis)
        dictionary[len(dictionary)] = data

        print("\nNew Record Added\n")
        self.main_menu()

    """ 
    THIS METHOD SHOULD RETRIEVE THE DATA AT SPECIFIED INDEX
    """

    def find_patient_at_index(self, ind_to_returned):
        if (ind_to_returned <= len(dictionary) - 1):
            print("--------------------------------------------------------------------------------")
            print("{:15} {:15} {:15} {:15}".format("NAME", "SSN", "AGE", "DIAGNOSIS"))
            print("--------------------------------------------------------------------------------")
            info = dictionary[ind_to_returned]
            print(''.join(['{:16}'.format(item) for item in info]))  # forammting the list in dictionary to print
        else:
            print("Invalid Patient Index..")  # Error Handling
            print(
                "No. of patients in Patient Directory are : {} ,select any index from 0 till {}".format(len(dictionary),
                                                                                                        len(
                                                                                                            dictionary) - 1))
            ind_to_returned = int(input("Enter the index number : "))
            self.find_patient_at_index(ind_to_returned)

        self.main_menu()

    """ 
    THIS3 METHOD SHOULD SHOW ALL RECORDS IN DICTIONARY
    """

    def show_all(self):  # show all the data
        print("--------------------------------------------------------------------------------")
        print("{:15} {:15} {:15} {:15}".format("NAME", "SSN", "AGE", "DIAGNOSIS"))
        print("--------------------------------------------------------------------------------")
        # print('\n'.join([''.join(['{:16}'.format(item) for item in row]) for row in fulldata]))
        for data in dictionary.values():
            # print(data)
            print(''.join(['{:16}'.format(item) for item in data]))
        print()
        self.main_menu()

    """ 
    THIS METHOD SHOULD RETRIEVE THE RECORD WITH USER NAME
    """

    def find_patient_with_name(self):
        name = input("Enter the Patient to be searched with Name: ")
        temp = 0
        print("--------------------------------------------------------------------------------")
        print("{:15} {:15} {:15} {:15}".format("NAME", "SSN", "AGE", "DIAGNOSIS"))
        print("--------------------------------------------------------------------------------")
        for i in range(0, len(dictionary)):
            for j in range(0, 4):
                if name in dictionary[i][j]:
                    print(''.join(['{:16}'.format(item) for item in dictionary[i]]))
                    temp = 1
        if (temp == 0):
            print("No results found")
        self.main_menu()

    """ 
    THIS METHOD WRITES NEWLY ADDED DATA INTO TEXT FILE AND EXIT FROM LOOP
    """

    def call_exit(self):  # before exit writing new data to the file and save and exit.
        try:
            with open(self.file_name, "w", newline="") as outfile:  # open the file from which you want to read
                writer = csv.writer(outfile)
                for data in dictionary.values():
                    writer.writerow(data)
            outfile.close()
        except FileNotFoundError:  # exception handling if file is not found on the disk.
            print("Couldn't find the file")
        except OSError:  # exception handling if file is not readable.
            print("File Found - Problem reading the file")
        except SyntaxError:  # eception handling if program has any syntax error.
            print("SyntaxError")
        return 0


pm = PatientManagement()  # make the object of the class which will call the constructor