#!/usr/bin/env python3
 
#   Name: Supersploit 
#   Feature: A improved sulotion of using Searchsploit and Metasploit
#   Version: 0.0.1 (2019-09-16)
#   Written by: Thaddeus Pearson, RedsHort
#   Homepage: https://github.com/thaddeuspearson/Super_Sploit
 
import subprocess
import datetime
import os
 
 
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
    elif message == "end":
        return """
    ██╗  ██╗ █████╗ ██████╗ ██████╗ ██╗   ██╗    ██╗  ██╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗ ██████╗ ██╗
    ██║  ██║██╔══██╗██╔══██╗██╔══██╗╚██╗ ██╔╝    ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██║████╗  ██║██╔════╝ ██║
    ███████║███████║██████╔╝██████╔╝ ╚████╔╝     ███████║███████║██║     █████╔╝ ██║██╔██╗ ██║██║  ███╗██║
    ██╔══██║██╔══██║██╔═══╝ ██╔═══╝   ╚██╔╝      ██╔══██║██╔══██║██║     ██╔═██╗ ██║██║╚██╗██║██║   ██║╚═╝
    ██║  ██║██║  ██║██║     ██║        ██║       ██║  ██║██║  ██║╚██████╗██║  ██╗██║██║ ╚████║╚██████╔╝██╗
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝        ╚═╝       ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝
    """
 
    
 
 
# This is a function for running bash script
def runcommand(cmd):
    output = subprocess.run(cmd, shell = True, capture_output = True)
    list_string = output.stdout.decode("utf-8")
    return list_string
 
# Removes the format of the searchsploit result
def format_stripper(output1):
    # output_simple = output1.replace("\x1b[01;31m\x1b[K", "").replace('\x1b[m\x1b[K', '').split('\n')
    output_simple = output1.split('\n')
    if '(Metasploit)' in output_simple[0]:  
        
        output_simpler = output_simple[0:-1]
    else:
        output_simpler = output_simple[4:-3]
    # The simplest format of the results
    return [" ".join(i.split()) for i in output_simpler]
 
# Build the selection list.
def list_builder(new_list1):
    result_list = []
    
    for entry in new_list1:
        
        exploit_instance = entry.split(" | ")
        
        result_list.append(exploit_instance)
    
    return result_list
 
 
# Format the selection list.
def pretty(origin_list):
    print_string = ""
    for i in origin_list:
        print_string += str(origin_list.index(i) + 1) + ": " + i[0]
        if origin_list.index(i) != len(origin_list):
            print_string += "\n"
    return print_string
 
 
# User selection of local or Metasploit exploits.
def local_or_metasploit(is_metasploit, target_os, target):
    flag = "" if is_metasploit else "-v"
    searchsploit_command = "searchsploit --colour --overflow %s %s | grep  %s  '(Metasploit)' " % (target_os, target, flag)
    
    return list_builder(format_stripper(runcommand(searchsploit_command)))
 
 
def copy_exploit(list_of_lists, copy_pathway):
    exploit = list_of_lists[int(copy) - 1][1]
    all_exploit_path = "/usr/share/exploitdb/" + exploit
    runcommand("cp " + all_exploit_path + " " + copy_pathway)
    
 
# Generate the current time for .rc file name
def file_name_date(date_format):
    x = datetime.datetime.now()
    return x.strftime(date_format)
 
# Generate the .rc file to open msfconsole
def metasploit_open(list_of_lists_two, user_selection):
 
    exploit_disc = list_of_lists_two[int(user_selection) - 1][0]
    search_term_msfconsole = exploit_disc[exploit_disc.index(" - ") + 3 : exploit_disc.index(" (Metasploit)")]
    tmp_file = file_name_date("%I%M%S%m%d%y")
    log_builder(exploit_disc)
    open_msfconsole = '/tmp/' + tmp_file + ".rc"
    runcommand("echo search name:" + search_term_msfconsole + " > " + open_msfconsole )
    subprocess.run(["msfconsole", "-r", open_msfconsole])
        
    
def log_builder(log):
    file_name = "/var/log/supersploit.log"
    mode = "a" if os.path.exists(file_name) else "w"
    log_file = open(file_name, mode)
    log_file.write(file_name_date("%a %b %d %Y %I:%M:%S %p    ") + log + "\n")
    
    
def input_check(usr_prompt, error, is_valid, valid_list):
    user_input = input(usr_prompt)
    while not is_valid(user_input, valid_list):
        print(error)
        user_input = input(usr_prompt)
    return user_input
 
 
def validate_list(item, lst):
    if item not in lst:
        return False
    return True
 
 
def validate_number(item, lst):
    if item.isdigit() and int(item) <= len(lst):
        return True
    return False
 
def main():
    print(banner_message("start"))
 
    input_os = input("Plz type the target OS.   ")
    input_target = input("plz type the target service or application.    ")
 
 
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
 
    
    copy = input_check("Which exploit do you want?    ", "Invalid input. Expected digits from provided list.", validate_number, range(0, len(reference_list)))
 
    
    if metasploitable == True:
        metasploit_open(reference_list, copy)
    else:
        file_cp_dest = input_check("Type C copy to corrent directory OR T copy to /tmp    ", "Invalid input. Expected C or T", validate_list, ["C", "c", "T", "t"])
        if file_cp_dest in ["c", "C"]:
            final_file_path = "."
        elif file_cp_dest in ["t", "T"]:
            final_file_path = "/tmp"
        copy_exploit(reference_list, final_file_path)
 
 
    print(banner_message("end"))
 
if __name__ == '__main__':
    main()
 
   
 
 

