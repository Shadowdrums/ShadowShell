# Shadow Shell Terminal
# This will be the terminal to activate and run the programs on the shadow Shell
# have a picture
# have a help terminal 
# be able to activate 2 programs
# password(key) activated
#Contributers:
# Shadowdrums
# DJ Stomp
# toroidist

print("You must use Key to use ShadowShell\n")

def get_key():
  key = -1
  correct = 7331
  while key != correct:
    key = input("please enter key: \n")
    try:
      if int(key) != correct:
        raise
      else:
        key = int(key)
    except:
      print("Access Dendied Inavlid Key")
      
get_key()
print("Access Granted")

#      ...                                    ..                                                ...                                      ..       .. 
#   .x888888hx    :   .uef^"                 dF                       x=~                    .x888888hx    :   .uef^"               x .d88"  x .d88" 
#  d88888888888hxx  :d88E                   '88bu.             u.    88x.   .e.   .e.       d88888888888hxx  :d88E                   5888R    5888R 
# 8" ... `"*8888%`  `888E             u     '*88888bu    ...ue888b  '8888X.x888:.x888      8" ... `"*8888%`  `888E            .u     '888R    '888R 
#!  "   ` .xnxx.     888E .z8k     us888u.    ^"*8888N   888R Y888r  `8888  888X '888k    !  "   ` .xnxx.     888E .z8k    ud8888.    888R     888R 
#X X   .H8888888%:   888E~?888L .@88 "8888"  beWE "888L  888R I888>   X888  888X  888X    X X   .H8888888%:   888E~?888L :888'8888.   888R     888R 
#X 'hn8888888*"   >  888E  888E 9888  9888   888E  888E  888R I888>   X888  888X  888X    X 'hn8888888*"   >  888E  888E d888 '88%"   888R     888R 
#X: `*88888%`     !  888E  888E 9888  9888   888E  888E  888R I888>   X888  888X  888X    X: `*88888%`     !  888E  888E 8888.+"      888R     888R 
#'8h.. ``     ..x8>  888E  888E 9888  9888   888E  888F u8888cJ888   .X888  888X. 888~    '8h.. ``     ..x8>  888E  888E 8888L        888R     888R 
# `88888888888888f   888E  888E 9888  9888  .888N..888   "*888*P"    `%88%``"*888Y"        `88888888888888f   888E  888E '8888c. .+  .888B .  .888B .
#  '%8888888888*"   m888N= 888> "888*""888"  `"888*""      'Y"         `~     `"            '%8888888888*"   m888N= 888>  "88888%    ^*888%   ^*888% 
#     ^"****""`      `Y"   888   ^Y"   ^Y'      ""                                             ^"****""`      `Y"   888     "YP"       "%       "% 
#                         J88"                                                                                     J88"
#                         @%                                                                                       @%
#                       :"                                                                                        :"

print("Welcome to ShadowShell\n") 
 
menu = "/S" , "/C"
print("please choose from one of our option\n" + "1. /S : will start the Server\n" + "2. /C : will start and run Client,\n")

import os # imports always go at the top
routines = {
  "/S": "Server",
  "/C": "Client"
}
def exec_routine(inpt):
  if inpt in routines.keys():
    os.system("C:\\%HOMEPATH%\\Desktop\\projects\\"+f"{routines[inpt]}.py")
    print(f"{routines[inpt]} has finished")

def get_input():
  command = ""
  while command not in routines.keys():
    command = input("Please enter command:\n> ")
    try:
      if command not in routines.keys():
        raise
      else:
        return command
    except:
      print("Invalid Command")

exec_routine(get_input())
print("Thank you for using ShadowShell")


wait = input()





















