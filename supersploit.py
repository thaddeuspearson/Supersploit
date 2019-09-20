#!/usr/bin/env python3
 
#   Name: Supersploit 
#   Feature: A improved sulotion of using Searchsploit and Metasploit
#   Version: 0.0.1 (2019-09-16)
#   Written by: Thaddeus Pearson, RedsHort
#   Homepage: https://github.com/thaddeuspearson/Supersploit
 
import subprocess
import datetime
import os
import re

 
# banner printing function
def banner_message(message):
    if message == "start":
        return """
    ███████╗██╗   ██╗██████╗ ███████╗██████╗ ███████╗██████╗ ██╗      ██████╗ ██╗████████╗
    ██╔════╝██║   ██║██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██║     ██╔═══██╗██║╚══██╔══╝
    ███████╗██║   ██║██████╔╝█████╗  ██████╔╝███████╗██████╔╝██║     ██║   ██║██║   ██║
    ╚════██║██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗╚════██║██╔═══╝ ██║     ██║   ██║██║   ██║
    ███████║╚██████╔╝██║     ███████╗██║  ██║███████║██║     ███████╗╚██████╔╝██║   ██║
    ╚══════╝ ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝ ╚═════╝ ╚═╝   ╚═╝
    """
    if message == "end":
        return """
    ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ██╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ ██║
    ███████║███████║██████╔╝██████╔╝ ╚████╔╝     ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗██║
    ██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝      ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║╚═╝
    ██║  ██║██║  ██║██║     ██║        ██║       ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
    """
    if message == "again":
        return """
    ████████╗██████╗ ██╗   ██╗     █████╗  ██████╗  █████╗ ██╗███╗   ██╗    ██████╗ ██████╗  ██████╗ 
    ╚══██╔══╝██╔══██╗╚██╗ ██╔╝    ██╔══██╗██╔════╝ ██╔══██╗██║████╗  ██║    ██╔══██╗██╔══██╗██╔═══██╗
       ██║   ██████╔╝ ╚████╔╝     ███████║██║  ███╗███████║██║██╔██╗ ██║    ██████╔╝██████╔╝██║   ██║
       ██║   ██╔══██╗  ╚██╔╝      ██╔══██║██║   ██║██╔══██║██║██║╚██╗██║    ██╔══██╗██╔══██╗██║   ██║
       ██║   ██║  ██║   ██║       ██║  ██║╚██████╔╝██║  ██║██║██║ ╚████║    ██████╔╝██║  ██║╚██████╔╝
       ╚═╝   ╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
    """
    if message == "wait":
        return """
     ██████╗ ██╗██╗   ██╗███████╗    ██╗████████╗     █████╗     ███████╗███████╗ ██████╗         
    ██╔════╝ ██║██║   ██║██╔════╝    ██║╚══██╔══╝    ██╔══██╗    ██╔════╝██╔════╝██╔════╝         
    ██║  ███╗██║██║   ██║█████╗      ██║   ██║       ███████║    ███████╗█████╗  ██║              
    ██║   ██║██║╚██╗ ██╔╝██╔══╝      ██║   ██║       ██╔══██║    ╚════██║██╔══╝  ██║              
    ╚██████╔╝██║ ╚████╔╝ ███████╗    ██║   ██║       ██║  ██║    ███████║███████╗╚██████╗██╗██╗██╗
     ╚═════╝ ╚═╝  ╚═══╝  ╚══════╝    ╚═╝   ╚═╝       ╚═╝  ╚═╝    ╚══════╝╚══════╝ ╚═════╝╚═╝╚═╝╚═╝
    """
 
    
# this is a function for running bash script
def runcommand(cmd):
    output = subprocess.run(cmd, shell = True, capture_output = True)
    list_string = output.stdout.decode("utf-8")
    return list_string

 
# removes the format of the searchsploit result
def format_stripper(searchsploit_output):
    output_simple = searchsploit_output.split('\n')
    if '(Metasploit)' in output_simple[0]:  
        output_simpler = output_simple[0:-1]
    else:
        output_simpler = output_simple[4:-3]
    # The simplest format of the results
    return [" ".join(i.split()) for i in output_simpler]

 
# build the selection list.
def list_builder(new_list1):
    result_list = []
    for entry in new_list1:
        exploit_instance = entry.split(" | ")
        result_list.append(exploit_instance)
    return result_list

 
# format the selection list.
def pretty(origin_list):
    print_string = ""
    for i in origin_list:
        print_string += str(origin_list.index(i) + 1) + ": " + i[0]
        if origin_list.index(i) != len(origin_list):
            print_string += "\n"
    return print_string
 

# user selection of local or Metasploit exploits.
def local_or_metasploit(is_metasploit, target_os, target):
    flag = "" if is_metasploit else "-v"
    searchsploit_command = "searchsploit --colour --overflow %s %s | grep  %s  '(Metasploit)' " % (target_os, target, flag)
    return list_builder(format_stripper(runcommand(searchsploit_command)))
 

# copy the user selected exploit.
def copy_exploit(list_of_lists, copy_pathway, exploit_num):
    exploit = list_of_lists[int(exploit_num) - 1][1]
    all_exploit_path = "/usr/share/exploitdb/" + exploit
    runcommand("cp " + all_exploit_path + " " + copy_pathway)
    
 
# generate the current time for .rc file name.
def file_name_date(date_format):
    x = datetime.datetime.now()
    return x.strftime(date_format)
 

# open Metasploit with the user selected search parameters
def metasploit_open(list_of_lists_two, user_selection):
    exploit_path = list_of_lists_two[int(user_selection) - 1][1]
    name = exploit_path_to_name(exploit_path)
    tmp_file = file_name_date("%I%M%S%m%d%y")
    log_builder(exploit_path)
    open_msfconsole = '/tmp/' + tmp_file + ".rc"
    runcommand(("echo search -u -S \\'%s\\' description:\\'%s\\'" % (name,name)) + " > " + open_msfconsole)
    subprocess.run(["msfconsole", "-r", open_msfconsole])
    return open_msfconsole


# search the local exploit for the Metasploit exploit name
def exploit_path_to_name(path):
    absolute_path ="/usr/share/exploitdb/" + path
    f = open(absolute_path)
    for line in f:
        match = re.findall(r"'Name'\s*=>\s*('.*')", line)
        #print(match)
        if len(match) > 0:
            return match[0]


# build or append user activity to the supersploit log.
def log_builder(log):
    file_name = "/var/log/supersploit.log"
    mode = "a" if os.path.exists(file_name) else "w"
    log_file = open(file_name, mode)
    log_file.write(file_name_date("%a %b %d %Y %I:%M:%S %p    ") + log + "\n")
    

# user input validation function.
def input_check(usr_prompt, error, is_valid, valid_list):
    user_input = input(usr_prompt)
    while not is_valid(user_input, valid_list):
        print(error)
        user_input = input(usr_prompt)
    return user_input
 

# input_check helper function.
def validate_list(item, lst):
    if item not in lst:
        return False
    return True
 

# input_check helper function.
def validate_number(item, lst):
    if item.isdigit() and int(item) <= len(lst):
        return True
    return False
 

def main():
    # Welcome banner.
    print(banner_message("start"))

    # User input search paramenters.
    input_os = input("Please type the target OS.   ")
    input_target = input("Please type the target service or application.    ")
    choice = input_check("Type L for local exploits OR M for Metaspolits    ", "Invalid input. Expected L or M.", validate_list, ["M", "m", "L", "l"])
    metasploitable = False
 
    # Differentiate the user input.
    if choice in ["L", "l"]:
        reference_list = local_or_metasploit(False, input_os, input_target) 
        print(pretty(reference_list))
    elif choice in ["M", "m"]:
        metasploitable = True
        reference_list = local_or_metasploit(True, input_os, input_target) 
        print(pretty(reference_list))

    if len(reference_list) == 0:
        print("Your OS input: " + input_os + " and/or your target service input: " + input_target + " yeilded absolutely no results. You should check your input and")
        return print(banner_message("again"))

    # user selects which exploit they want
    copy = input_check("Which exploit do you want?    ", "Invalid input. Expected digits from provided list.", validate_number, range(0, len(reference_list)))
 
    # differentiate local or metasploit exploits
    if metasploitable == True:
        print(banner_message("wait"))
        tmp_file = metasploit_open(reference_list, copy)
        runcommand("rm -r %s" % (tmp_file))
    else:
        file_cp_dest = input_check("Type C copy to current directory OR T copy to /tmp    ", "Invalid input. Expected C or T", validate_list, ["C", "c", "T", "t"])
        if file_cp_dest in ["c", "C"]:
            final_file_path = "."
        elif file_cp_dest in ["t", "T"]:
            final_file_path = "/tmp"
        exploit_name = input("What do you want to call your exploit?    ")
        copy_exploit(reference_list, final_file_path + "/" + exploit_name, copy)
    
    
    # farewell message
    print(banner_message("end"))
 
if __name__ == '__main__':
    main()
    
    