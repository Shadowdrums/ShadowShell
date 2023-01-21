Set objSHL = CreateObject("Wscript.Shell")

MsgBox "Starting Client",vbOKOnly,"Please Wait"
objSHL.Popup "Thank you",5,"please Wait",vbokonly


Set WshShell = CreateObject("WScript.Shell")
WshShell.Run chr(34) & "C:\Intel\Client.py" & chr(34), 0
Set WshShell = Nothing