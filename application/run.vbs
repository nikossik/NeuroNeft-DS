Dim WShell
Set WShell = CreateObject("WScript.Shell")
WShell.Run "python main.py", 0
Set WShell = Nothing