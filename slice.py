#!/usr/bin/env python
import os
from datetime import datetime, timedelta
from datetime import time as timelib
from math import floor
import re
import gzip
# import pdb

class LogNinja:

	def print_ninja(self):                                     
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
		print(" / /  / _ \\ / _  |  /  \\/ / | '_ \\ | |/ _` |            ")
		print("/ /__| (_) | (_| | / /\\  /| | | | || | (_| |              ")
		print("\\____/\\___/ \\__, | \\_\\ \\/ |_|_| |_|/ |\\__,_|        ")
		print("            |___/                |__/                      ")
		print("Welcome to Log Ninja! Let's slice some logs.")

	def get_folder_path(self):
		# Get the path holding the modem messages
		folder_path = input("Drag the folder containing the modem messages logs: ")
		folder_path = str(folder_path).strip()
		# Switch to that directory
		os.chdir(r'%s' % folder_path)
		# List directory to verify we switched to the right one
		current_dir_path = os.path.dirname(os.path.realpath(__file__))

		print("Switched to " + current_dir_path)
		print("Files in this directory: ")

		# List files in that directory
		for file_name in os.listdir(folder_path):
			print(file_name)
		return folder_path

	def get_date(self):
		print('\n'*2)
		# Start the outer loop up here. If the user flag is set to true, then we do everything here. It is set to false at the end
		#	if the user selects no to the question if they want to continue putting in more dates
		print("Note if you enter today's date (GMT) the default messages with no timestamp log will be retrieved. If you are slicing these logs on a later date than when the logs were pulled, that may be an older file")
		print('\n')
		date = input("Enter the GMT date yyyymmdd: ")

		date = str(date).strip()
		# Check for 8 digit date stamp else we continue to ask user for good input
		while True:
			if(len(date) == 8):
				break
			else:
				date = str(input("Invalid input: Please enter the date <yyyymmdd>: "))
		return date

	def get_times(self):
		times = input("Enter all of the GMT times of incidents separated by spaces such as 1345 1532 1930 1345 : ")
		times = times.split()
		times_are_valid = True

		# Input Validation for Times We set times valid to true. Then we have an endless loop where we loop through the times values to 
		#   evaluate the times entered to see if they are outside of the values for a 24 hour day. If they are we change times are valid to false
		#   if it is never changed to false then when we check it after the for loop we break out of the endless loop. If we do find an invalid time,
		#	the user is prompted again to enter the times and reevaluate it all. It also handles times like 1068
		while True:
			for index, time in enumerate(times):
				time_int = int(time)
				time_str = time
				# If the time is outside of the 24 hours in the day
				if time_int < 0 or time_int > 2400:
					print(time_str + " is outside of valid range 0000...2359")
					times_are_valid = False
				# If the last time digits of the 4 digit time are greater than 59 it is declared invalid also
				elif(int(time_str[2:4]) > 59):
					print(time_str + " has more than 59 minutes")
					times_are_valid = False
				# If the times validate, then the times_are_valid flag is flipped to true for this for loop iteration. 
				#	This is needed in case the input fails validation, but then the user is asked for times again, the 
				#   flag has been flipped to false for the first time but it needs to be flipped back to true to prepare
				# 	for all inputs good
				else:
					times_are_valid = True
			# If the times are declared valid, or rather, they are not declared false, we break out of the endless validation
			#	loop
			if times_are_valid:
				break
			# Otherwise we ask the user for the times again
			else:
				times = input("Enter all of the GMT times of incidents separated by spaces (1345 1532 1930 1345 : ")
				times = times.split()	
		print("You entered: ")
		print(times)
		return times		

	# Gets number of minutes to be added plus or minus. Max number is set to 360 though it can be higher. 12 hours total around a timestamp 
	def get_sliced_minutes(self):
		print("")
		print("Sliced Minutes is the +/- around the timestamp. If timestamp is 1300 and sliced minutes is 6, it will slice 1257 - 1303 with the timestamp centered")
		print("")
		sliced_minutes = input("Enter the number of minutes around each incident you want to slice: ")
		while True:
			if int(sliced_minutes) < 721:
				break
			elif int(sliced_minutes) > 720:
				sliced_minutes = input("Max number of sliced minutes is 720. Enter the number of minutes around each incident you want to slice: ")

		return int(sliced_minutes) / 2.0

	# Takes in a string like 0345 and returns it like 
	def convert_time_to_minutes(self, time):
		time = (int(time[0:2]) * 60) + int(time[2:4])
		return time

	# After we calculate start and stop based off total minutes plus minus sliced_minutes, we convert the value back into a string time like
	#	03:45:30
	def convert_minutes_to_time(self, minutes_in):
		# Convert half minutes first
		if ".5" in str(minutes_in):
			seconds = 30
			# round down for the minutes
			minutes_in = int(floor(minutes_in))
		else:
			seconds = 0
		minutes_in = int(minutes_in)
		minutes = minutes_in % 60
		hours = minutes_in / 60
		converted_time =  timelib(int(hours), int(minutes), int(seconds))
		converted_time = converted_time.strftime("%H:%M:%S")
		return converted_time

	# Modifies the times array from ["1345", "1550"] to ["1344 1346", "1549 1551"] if the user inputs 2 minutes for sliced_minutes. Returns that new array
	#	this will be split by space when setting start and stop times in the log parse
	def modify_times(self, times):
		# Create the array we will return with start and stop times
		start_stop_combined = []
		# Holds the string we push into the array we return that has start stop time for one time
		start_stop = ""
		# Iterate through times array, convert the time to number of minutes to do easy math since date time stamps for this become cumbersome.
		#	calculate the start and stop times but subtracting and adding sliced_minutes to them, checking for overflow on the day. Then convert the 
		#	minutes back into strings of time stamps like "03:45:30" and create string holding both with a space in the middle and push that into our array
		# 	after we run through all times we return that array. 
		for time in times:
			converted_time = self.convert_time_to_minutes(time)

			temp_start = int(converted_time - sliced_minutes)
			temp_stop = int(converted_time + sliced_minutes)
			if(temp_start < 0):
				temp_start = 0
			elif(temp_stop > 1439):
				temp_stop = 1439
			temp_start_string = self.convert_minutes_to_time(int(temp_start))
			temp_stop_string = self.convert_minutes_to_time(temp_stop)
			start_stop = temp_start_string + " " + temp_stop_string
			start_stop_combined.append(start_stop)

		return start_stop_combined

	def modify_date(self, date):
		date_object = datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]))
		now = datetime.utcnow()
		if(now.strftime("%Y%m%d") == date):
			return date
		else:
			date_plus_one = date_object + timedelta(days=1)
			date = date_plus_one.strftime("%Y%m%d")
			return date

	# Takes date string and file_path string and returns the filepath containing the file that has a matching date 
	def find_log_by_date(self, date, folder_path):
		# Create and set found logs variable. If user enters a date and no log files match that date, this flag helps communicate that to them
		found_logs = False

		# If the input date equals now in zulu time, then set file_path to end in /messages
		now = datetime.utcnow()
		if(now.strftime("%Y%m%d") == date):
			file_path = folder_path + "/" + "messages"
			found_logs = True
		else:
			# Iterate through the list of files in object os.listdir(file_path). If we find a file with both messages and the date
			#	in the filename, that's our target file and we store it concatenated with the file_path into file_path. We also flip the 
			#	found logs flag to true so we can process it below.
			for filename in os.listdir(folder_path):
				if date in filename and "messages" in filename:
					found_logs = True
					file_path = folder_path + "/" + filename
					break	
		# If no matching file for that date is found, we set file_path to blank
		if not (found_logs):
			file_path = False
		return file_path

	def check_extension(self, file_path):
		file_type = ""
		# If we found the logs, we get the file extension or last 3 of the file. If it ends in .gz then we use the gzip library, otherwise
		#	 we use regular file IO to read it.
		if(file_path):
			extension = file_path[-3:]
			if(extension == ".gz"):
				file_type = "gzip"
			else:
				file_type = "text"
		# if found logs is false, meaning we didn't match our date with any filenames, then we inform the user and the most outer loop
		#	starts again
		else:
			print("There were no matching log files with your date")
			file_type = False
		return file_type

	# The time stamp is in the third position but there are a few lines throughout the log that is a message like 
	#	"Please review provided documentation". The program will falsely read that as reading the end of the stop time. 
	#	To prevent this, the below line looks for the colon in a time stamp and returns early if none is found meaning
	#	it is not a valid time to evaluate against. There must be a better way and there's a small chance you could have
	#	a word or message with no time stamp and a colon in the third item on the line but I haven't seen it. 
	def parse_line(self, start_time, stop_time, line, actual_date):	
		line = line.decode()
		split_line = line.split()
		# If the log file line has more than 3 elements then we grab the third element which is the time stamp. Sometimes
		# it has something like "Content-length: 907" which is not a valid line with a time stamp in which case we return
		# and don't copy that line
		if(len(split_line) > 2):
			time_stamp = split_line[2]
		else:
			return

		if(":" not in time_stamp):
			return 
		if(time_stamp > stop_time):
			return "end"
		elif(time_stamp >= start_time):
			outfile = open("sliced_logs_" + actual_date, "a")
			outfile.write(line)
			outfile.close()

	# Parse file takes all string variables of path to file, file type (gzip or text), actual date meaning the date the user put in
	#	date meaning the date of the log file since it lists the following day , and a time range to slice. 
	#	The method checks the file type and does the appropriate file opening based on that. It calls parse_line to check each
	#	line against start and stop times, and once the stop time is reached, it returns a success message
	def parse_file(self, file_path, file_type, actual_date, date, time):
		split_times = time.split(" ")
		start_time = split_times[0]
		end_time = split_times[1]
		line_status = ""

		self.create_section_header(time, actual_date, file_path)
		# pdb.set_trace()
		if(file_type == "gzip"):
			with gzip.open(file_path) as log_file:
				for line in log_file:
					line_status = self.parse_line(start_time, end_time, line, actual_date)
					if(line_status == "end"):
						log_file.close()
						return "File Parsed"

		# If we matched a file but it doesn't have .gz, then it must be an already unzipped file
		elif(file_type == "text"):
			log_file = open(file_path, "r")
			for line in log_file:
				line_status = self.parse_line(start_time, end_time, line, actual_date)
				if(line_status == "end"):
					log_file.close()
					return "File Parsed"

	def create_file_header(self, actual_date, file_path):
		outfile = open("sliced_logs_" + actual_date, "w")
		outfile.write("\n")
		outfile.write("Sliced logs for " + actual_date + " retrieved from " + file_path + "\n")
		outfile.write(("*" * 80) + "\n")
		outfile.close()

	# Creates the section header for the timestamp section in the outfile
	def create_section_header(self, time, actual_date, log_date):
		outfile = open("sliced_logs_" + actual_date, "a")
		outfile.write("\n\n\n\n\n\n\n\n")
		outfile.write("        __                    _ _        _                      \n")
		outfile.write("       / /  ___   __ _    /\\ \\ (_)_ __  (_) __ _              \n")
		outfile.write("      / /  / _ \\ / _  |  /  \\/ / | '_ \\ | |/ _` |            \n")
		outfile.write("     / /__| (_) | (_| | / /\\  /| | | | || | (_| |              \n")
		outfile.write("     \\____/\\___/ \\__, | \\_\\ \\/ |_|_| |_|/ |\\__,_|        \n")
		outfile.write("                 |___/                |__/                      \n")
		outfile.write("\n\n\n\n\n\n\n\n")
		outfile.write(("*" * 80) + "\n")
		outfile.write("Sliced logs for " + actual_date + " " + time +  "\n")
		outfile.write(("*" * 80) + "\n")




# Create the LogNinja instance and run main
Ninja = LogNinja()
Ninja.print_ninja()
keep_going = True 
# Get folder Path
folder_path = Ninja.get_folder_path()

while keep_going:	
	# Get date
	actual_date = Ninja.get_date()
	# Get times to be sliced
	times = Ninja.get_times()
	# Get num of minutes to slice out
	sliced_minutes = Ninja.get_sliced_minutes()
	# Modify the date since the logs for the 25th will actually be listed under the 26th
	log_date = Ninja.modify_date(actual_date)
	# Locate the matching file and return file path
	file_path = Ninja.find_log_by_date(log_date, folder_path)
	if(file_path == False):
		print("No matching log found for " + actual_date)
		continue
	# TODO add a thing where if the file_path is not located we loop through and ask for it all again 
	file_type = Ninja.check_extension(file_path)
	# Convert invidivual center times to start stop times in an array to be looped
	modified_times = Ninja.modify_times(times)
	# Create the outfile for the sliced logs where date is the date we are trying to locate
	Ninja.create_file_header(actual_date, file_path)
	# Call file parser method to find and output lines that match the timestamp
	for index, time in enumerate(modified_times):
		result = Ninja.parse_file(file_path, file_type, actual_date, log_date, modified_times[index])
		if(result == "File Parsed"):
			print("Sliced " + modified_times[index] + " from " + file_path)
	keep_going = input("Would you like to slice another day? y/n: ")
	if(keep_going == 'n' or keep_going == 'no' or keep_going == 'N' or keep_going == 'NO'):
		break
	else:
		keep_going = True


# Tests
# test, for 0000 time, 2359 time, 2359 + 5 minutes, 0000 + 5 minutes, test the maximum and minimum acceptable values for each method
#	test for current date, test for unzipped regular file

# Future Plans
# Create a parse alert method or alternate class. Looks through logs and creates a diagnosis based off of known errors - railing attenuator, arinc, etc
