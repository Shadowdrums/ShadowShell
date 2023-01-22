# ShadowShell

<img style="max-width: 500px" width="500px" max-width="500px" title="Get it? Shell!" src="https://i.imgur.com/gmsJJbZ.jpg">

## Overview
A reverse shell for Windows to Windows application written in python

## Requirements
- Both devices will need python 3 installed.
- This reverse shell is for windows to windows application.

## Getting Started

1. In both client.py and server.py you will need to change FF.FF.FF.FF for the ip address of your computer(host).

2. Be sure to change the port's and that they match in both server and client. also to be safe make sure to make a firewall rule
   that only allows connection on the port youre going to use between your computer and the target computer and only those devices.

3. This application comes with a VBScript that you place in the target device startup folder and the Client.py in the Intel folder this will
   run client.py in the background on target device everytime the device is turned on.

4. ShadowShell1.3A.py is optional for using this application and its preferable sue is on the host device. the key to use the terminal is "7331"
   and can be changed to what ever you prefer though note it only excepts numbers and no special characters or letters. Also not that the file path the ShadowShell 
   uses is set for dsktop and a folder named projects and the server and client must be placed in that folder for the terminal to activate them if you
   chose to use it.

5. This will give you a reverse shell into a windows computer and allow the user to use the targets command prompt. if you would like to use powershell
   you must use "powerhsell -command yourCommand" other wise the program will freeze and crash and you will have to reconnect.

## Special thanks
##### Author
- Shadowdrums
##### Contributors
- DJ Stomp
- toroidist

## Disclaimer
__THIS APPLICATION IS INTENDED FOR EDUCATIONAL PURPOSES *ONLY*__

THE DEVELOPER WILL NOT BE HELD LIABLE FOR ANY DAMAGES
CAUSED BY MISUSE OF THE SOURCE CODE IN THIS REPOSITORY.

NEVER USE ON ANY DEVICE YOU DO NOT OWN UNLESS YOU HAVE
DOCUMENTED PRE-APPROVAL FROM THE OWNER OF THE DEVICE(S)

<hr>
<details>
<summary style="color:#0d1117">Secret Section</summary>

<pre><code>+--------------+
|  SHADOWDRUMS |
|          TM  |
|              |
|              |
+--------------+ </code></pre>
<p align="center"><img width="250" src="https://i.imgur.com/gZ0Dp0L.png"></p>
<hr>
</details>
