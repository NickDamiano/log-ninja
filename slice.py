#!/usr/bin/env python
import os
from datetime import datetime, timedelta
from datetime import time as timelib
from math import floor
import re
import gzip
import pdb

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
		folder_path = raw_input("Drag the folder containing the modem messages logs: ")
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
		times = raw_input("Enter all of the GMT times of incidents separated by spaces (1345 1532 1930 1345 : ")
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
				times = raw_input("Enter all of the GMT times of incidents separated by spaces (1345 1532 1930 1345 : ")
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
			if sliced_minutes < 721:
				break
			elif sliced_minutes > 720:
				sliced_minutes = input("Max number of sliced minutes is 720. Enter the number of minutes around each incident you want to slice: ")

		return sliced_minutes / 2.0

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

		minutes = minutes_in % 60
		hours = minutes_in / 60
		print(hours)
		print("hours above")
		converted_time =  timelib(hours, minutes, seconds)
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

			temp_start = converted_time - sliced_minutes
			temp_stop = converted_time + sliced_minutes
			if(temp_start < 0):
				temp_start = 0
			elif(temp_start > 2359):
				temp_stop = 2359

			temp_start_string = self.convert_minutes_to_time(temp_start)
			temp_stop_string = self.convert_minutes_to_time(temp_stop)
			start_stop = temp_start_string + " " + temp_stop_string
			start_stop_combined.append(start_stop)

		return start_stop_combined

	def modify_date(self, date):
		date_object = datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]))
		now = datetime.now()
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
		now = datetime.now()
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
				extension = "text"
		# if found logs is false, meaning we didn't match our date with any filenames, then we inform the user and the most outer loop
		#	starts again
		else:
			print("There were no matching log files with date " + date)
			file_type = False
		return file_type

	def parse_file(self, file_path, file_type, date, times, sliced_minutes):
		print("I am in the parse_file method")
		# For each time in times
		# calculate time start based off times[i] - sliced_minutes plus convert it to "00:04:00" format (but if the start time is a negative, meaning we subtracted 5 from 0001, then we start it at 0000)
		# calculate time stop based off times[i] + sliced_minutes plus convert it to "00:04:00" format (if the start time is over 2359, then cap it at 2359)
		# create a start flag and set to false
		# create a stop flag and set to false

		# Open the file and read in each line
			# split the line into a separate split_line variable
			# if start_flag is flipped OR line[2] == start_time or if line[2] > start_time and start_flag not flipped
					# flip the start flag
					# grab that line and write it to the outfile
			# if line[2] == stop_time or if line[2] > stop_time and stop_flag not flipped
				# flip stop_flag to true and start flag to false
				# Write a bunch of line breaks and formatting for next time
				# Skip the for loop to get to the next time in the times array
		# if(extension == ".gz")
		# 	with gzip.open(file_path) as f:
		# 		line = f.read()
		# # If we matched a file but it doesn't have .gz, then it must be an already unzipped file
		# else:
		# 	opened_input_file = open(file_path, "r")
		# 	line = opened_input_file.readlines()
		# 	# if startime is in line or greater, then open file
		# 	# if stoptime or greater is in line, close the output file and change starttime

	# # Takes a line 
	# def line_parser(line):
	# 	print

Ninja = LogNinja()
Ninja.print_ninja()

# Probably start a loop here until the user types exit or something so it keeps getting dates
folder_path = Ninja.get_folder_path()
print(folder_path)
date = Ninja.get_date()
times = Ninja.get_times()
sliced_minutes = Ninja.get_sliced_minutes()
date = Ninja.modify_date(date)
print(date)
file_path = Ninja.find_log_by_date(date, folder_path)
print(file_path)
file_type = Ninja.check_extension(file_path)
print(file_type)
modified_times = Ninja.modify_times(times)
print(modified_times)








	#TODO handle just plain messages file

	#TODO once the file is being extracted accurately, create a second class or method that is just for applying filters and rules
	# so I can be like if you see, within 2 minutes span, 10 attenuator railed issues, then flag it for cable inspection and pending no issues, antenna replacement

	# or if you see arinc missing o rsomething like that and this and that, diagnose as possible w




	


	# Close infile and outfile


	# Maybe trace this ? It should only look through the file once and during that look, grab the appropriate sections for all times
	# what you should probably do is create some methods and call them instead of so many inner loops.
	# What we want to do is then ask the user if they have more dates yes/no. If they say yes, then we loop through the entire thing. If they say no
	# 	then we exit with another ascii art thing. But at a mimimum we get this working for one iteration. 
	#	Then a user can go look at SMS and write down 20190501 1353 

	# what would be cool and totally worthless would be to have an animation of a sword slicing and then it loops ascii string file, clear screen, through an array of ascii string files
	# then it has like 60 frames/elements in the array





