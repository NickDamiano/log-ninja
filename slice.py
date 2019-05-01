#!/usr/bin/env python
import os
                                                       
print("               ***,*   ")
print("                     /*,,,                                 ")
print("                          /***                             ")
print("                              .***                         ")
print("                      %&&@&&&     ***                      ")
print("                     #&&&&&&&@        ***                  ")
print("                     & -  - /&%          .(&@##            ")
print("                     %&&&&&@@@&            @&&@            ")
print("                      @&&&&&@@             ./,#            ")
print("                      &@@@@@@@&@&&&%        % ((           ")
print("                %&&@&&@@@@@@@@@&%&%*&&&&&&&&& ,@           ")
print("            &@&&&&,,,&@/@&&&&&&&/&&&&&&@&&&@&@&&           ")
print("               &&@@%&&&&&&*&&&&%&&&&&                      ")
print("              &&&@@(&&&&&&&&@&& &&&                        ")
print("             %&@&@@ @&&&&&&.&&&&&&&&                       ")
print("            &&&&&@  @@@@@@&&&&/&&&&                        ")
print("           %&&&&&   &&@&&&&&.,@@&&                         ")
print("           &&&&&    @@  &%&&&&&&&%                         ")
print("          &&&&&    /%.    &&     @                         ")
print("         ,. &&     &*@@&&&&&&&@&@%/                        ")
print("         .*%&     @@@@&@@@&@&&&&@@@&                       ")
print("        (. &/    &&@@@@@&@@@@&&@@&&&&                      ")
print("      &&&&&    &&&&&&&@@&@@@@@@&&&&&&&                     ")
print("     / ||||    &&&&&&&&&@&&@@&&&&&&&&&                     ")
print("              *&&&&&&&@@   @&&&&&&&&&&                     ")
print("              &&&&&&&@&     @@&&&&&&&&&                    ")
print("            &&&&&&&&&        @&@@&&&&&&                    ")
print("           &&&&&&&&&          /&&&@&&&&                    ")
print("           &&&&&&&&            &&@&@&&                     ")
print("           &&&@&&&             &&@@&&                      ")
print("           &&@&&&              &&@@&                       ")
print("           /@&&                 .&@&&                      ")
print("          ,.(..                 . .&.                      ")
print("          ..,..                  ..&&                      ")
print("   __   &&&.%&                   &&#%&.&                   ")
print("  / /  ___   __ _    /\\ \\ (_)_ __  (_) __ _              ")
print(" / /  / _ \\ / _` |  /  \\/ / | '_ \\ | |/ _` |            ")
print("/ /__| (_) | (_| | / /\\  /| | | | || | (_| |              ")
print("\\____/\\___/ \\__, | \\_\\ \\/ |_|_| |_|/ |\\__,_|        ")
print("            |___/                |__/                      ")
print("Welcome to Log Ninja! Let's slice some logs.")

file_path = raw_input("Drag the folder containing the modem messages logs: ")
# file_path = os.path.normpath(file_path)
file_path = str(file_path).strip()
print(file_path)

# os.path.isdir(file_path)
# print(file_path)
# print(current_dir_path)
os.chdir(r'%s' % file_path)
current_dir_path = os.path.dirname(os.path.realpath(__file__))
print(current_dir_path)

# date = str(input("Enter the date <yyyymmdd>: "))
# date.strip
# print(date)
# # Check for 8 digit date stamp else we continue to ask user for good input
# while True:
# 	if(len(date) == 8):
# 		break
# 	else:
# 		date = str(input("Invalid input: Please enter the date <ddmmyyyy>: "))
# time = str(input("Enter the time in GMT <hhmm>: "))
# # If the time is other than 4 digits we continue to ask for a 4 digit time stamp
# while True:
# 	if(len(time)==4):
# 		break
# 	else:
# 		time = str(input("Invalid input: Please enter the time in GMT <hhmm>: "))
# diff = str(input("Enter number of minutes plus minus: "))

# TODO use os path function to get the file path . maybe ask cody
# print(date)