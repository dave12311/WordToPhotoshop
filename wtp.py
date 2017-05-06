import win32clipboard
import win32com.client
import string

#--------------------------------------------
size = 12
#--------------------------------------------

win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

datalist = string.split(data,"\r\n")

#print datalist

psApp = win32com.client.Dispatch("Photoshop.Application")
doc = psApp.Application.ActiveDocument

for i in datalist:
    if i != "":
        layer = psApp.ActiveDocument.ArtLayers.Add()
        layer.Kind = 2
        layer.Name = i
        text = doc.ArtLayers(i).TextItem
        text.Contents = i
        text.Font = "ArialMT"
        text.Size = size