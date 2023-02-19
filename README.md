# LOG NINJA
Slices out logs x number of minutes around an incident time in a log file and exports them to an external file. 
Use case: 
- You have a folder of .gzip log files that are tens or hundreds of thousands of lines each. 
- You have incident times for failures that ocurred and want to quickly see the before and after logs around that time stamp
- You want all the incidents exported to a single file for further analysis 

Instructions
1. Run python slice.py
2. Drag the folder containing the .gzip log files from the file explorer into the CLI window and hit enter
3. Enter the date you want to slice
4. Enter time stamps separated by a space for each incident you want to slice
5. Enter the number of minutes around the incident you want to slice
6. Log Ninja will slice and dice the logs for you and export them into a plain text file named something like "sliced_logs_20221102" in the same directory
as the file location
7. All of your wildest dreams will come true


```              ***,*
                     /*,,,
                          /***
                              .***
                      %&&@&&&     ***
                     #&&&&&&&@        ***
                     & -  - /&%          .(&@##
                     %&&&&&@@@&            @&&@
                      @&&&&&@@             ./,#
                      &@@@@@@@&@&&&%        % ((
                %&&@&&@@@@@@@@@&%&%*&&&&&&&&& ,@
            &@&&&&,,,&@/@&&&&&&&/&&&&&&@&&&@&@&&
               &&@@%&&&&&&*&&&&%&&&&&
              &&&@@(&&&&&&&&@&& &&&
             %&@&@@ @&&&&&&.&&&&&&&&
            &&&&&@  @@@@@@&&&&/&&&&
           %&&&&&   &&@&&&&&.,@@&&
           &&&&&    @@  &%&&&&&&&%
          &&&&&    /%.    &&     @
         ,. &&     &*@@&&&&&&&@&@%/
         .*%&     @@@@&@@@&@&&&&@@@&
        (. &/    &&@@@@@&@@@@&&@@&&&&
      &&&&&    &&&&&&&@@&@@@@@@&&&&&&&
     / ||||    &&&&&&&&&@&&@@&&&&&&&&&
              *&&&&&&&@@   @&&&&&&&&&&
              &&&&&&&@&     @@&&&&&&&&&
            &&&&&&&&&        @&@@&&&&&&
           &&&&&&&&&          /&&&@&&&&
           &&&&&&&&            &&@&@&&
           &&&@&&&             &&@@&&
           &&@&&&              &&@@&
           /@&&                 .&@&&
          ,.(..                 . .&.
          ..,..                  ..&&
   __   &&&.%&                   &&#%&.&
  / /  ___   __ _    /\ \ (_)_ __  (_) __ _
 / /  / _ \ / _  |  /  \/ / | '_ \ | |/ _` |
/ /__| (_) | (_| | / /\  /| | | | || | (_| |
\____/\___/ \__, | \_\ \/ |_|_| |_|/ |\__,_|
            |___/                |__/
Welcome to Log Ninja! Let's slice some logs.
Drag the folder containing the modem messages logs:

```

After entering date, times, minutes to slice it will export to a file like this

```

Sliced logs for 20221102 retrieved from /Users/ndamiano/Desktop/var/tmp/dump/messages-2022110300.gz
********************************************************************************

        __                    _ _        _                      
       / /  ___   __ _    /\ \ (_)_ __  (_) __ _              
      / /  / _ \ / _  |  /  \/ / | '_ \ | |/ _` |            
     / /__| (_) | (_| | / /\  /| | | | || | (_| |              
     \____/\___/ \__, | \_\ \/ |_|_| |_|/ |\__,_|        
                 |___/                |__/                      


********************************************************************************
Sliced logs for 20221102 13:42:00 13:47:00
********************************************************************************
Nov  2 13:42:07 Oh no something bad happened!
Nov  2 13:42:10 MORE BAD STUFF!
```
