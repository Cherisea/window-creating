import wx
# define the load function
def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

 # define the save function
def save(event):
    file = open(filename.GetValue(), 'w')
    file.write(str(contents))
    file.close()

app = wx.App() # create an app object
win = wx.Frame(None, title = 'Joey window', size = (410, 335)) # creat a window supplied with title and size

bkg = wx.Panel(win) # a backgronund component subclassing window

loadButton = wx.Button(bkg, label = 'Open') # create a button named 'load'
loadButton.Bind(wx.EVT_BUTTON, load) # bind the button with a function

saveButton = wx.Button(bkg, label = 'Save') # create a button named 'save'
saveButton.Bind(wx.EVT_BUTTON, save)

filename = wx.TextCtrl(bkg) # a default text control object
contents = wx.TextCtrl(bkg, style = wx.TE_MULTILINE | wx.HSCROLL) # a customised text control object with a two bars and a text field

hbox = wx.BoxSizer()
hbox.Add(filename, proportion=1, flag= wx.EXPAND) # define the size of "filename" horizontal bar
hbox.Add(loadButton, proportion =0, flag= wx.LEFT, border= 5) # specify the size and position of 'load' button
hbox.Add(saveButton, proportion= 0, flag= wx.LEFT, border = 5) # specify the size and position of 'save' button

# specify vertical botton
vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox, proportion= 0, flag= wx.EXPAND | wx.ALL, border = 5)
vbox.Add(contents, proportion =1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

bkg.SetSizer(vbox)
win.Show()

app.MainLoop()


