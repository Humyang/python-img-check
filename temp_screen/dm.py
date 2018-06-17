import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')

#current version
print(dm.Ver()) 
dm.MoveTo(100,200)
d=dm.LeftDoubleClick()
print(d)