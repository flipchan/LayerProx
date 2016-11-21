#!/usr/bin/python
# -*- coding: utf-8 -*-

import wx
import wx.wizard
import os, sys #for lib test
#from textconf import appen # lets import the configuration file editor

class TitledPage(wx.wizard.WizardPageSimple):
    def __init__(self, parent, title):
        wx.wizard.WizardPageSimple.__init__(self, parent)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.sizer)
        titleText = wx.StaticText(self, -1, title)
        titleText.SetFont(
                wx.Font(18, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.sizer.Add(titleText, 0,
                wx.ALIGN_CENTRE | wx.ALL, 5)
        self.sizer.Add(wx.StaticLine(self, -1), 0,
                wx.EXPAND | wx.ALL, 5)

try:
    import gnupg
    pg = 'yes'
except ImportError:
    pg = 'nope'

try:
    import regex2dfa
    rf = 'yes'
except ImportError:
    rf = 'nope'

    
try:
    import fte
    ft = 'yes'
except ImportError:
    ft = 'nope'

        
try:
    import Crypto
    pc = 'yes'
except ImportError:
    pc = 'nope'

#install script
def install():
    os.system('./../debianinstaller')
    return 'ok'

if __name__ == "__main__":
    app = wx.PySimpleApp()
    wizard = wx.wizard.Wizard(None, -1, "LayerProx Wizard")
    page1 = TitledPage(wizard, "Welcome!")
    page2 = TitledPage(wizard, "Library install")
    #button = wx.Button(page2, -1, "Install it", pos=(200, 110))
    #self.bind(wx.EVT_BUTTON, OnClick, button)
    #button.SetDefault()    
    page3 = TitledPage(wizard, "Library check")
    page4 = TitledPage(wizard, "Launch")
    page1.sizer.Add(wx.StaticText(page1, -1,
            "This wizard will guide you throw installing LayerProx"))#welcome msg
    page2.sizer.Add(wx.StaticText(page2, -1,
     "for layerprox you need the following python libraries:\n\n gnupg\n\n pycrypto \n\n fte and regex2dfa"
     "installed: " + install()
     )) #lib install

    page3.sizer.Add(wx.StaticText(page3, -1,
                                  "python-gnupg: " + pg + '\n\n'
                                  "regex2dfa: " + rf + '\n\n'
                                  "fte: " +  ft + '\n\n'
                                  "pycrypto: " + pc + '\n\n'))
    
    page4.sizer.Add(wx.StaticText(page4, -1,
	"Finished installing, other cool projects:"
	"\n\n"
	"My github https://github.com/flipchan \n\n" 
	"Marionette https://github.com/marionette/marionette \n\n" 
	"Bitmask https://bitmask.net/ \n\n"
	"Tor https://www.torproject.org/ \n\n"
        "Demonsaw demonsaw.com\n\n"
        "Press finish to configure LayerProx\n\n"))
    wx.wizard.WizardPageSimple_Chain(page1, page2)
    wx.wizard.WizardPageSimple_Chain(page2, page3)
    wx.wizard.WizardPageSimple_Chain(page3, page4)
    
    wizard.FitToPage(page1)
    
    if wizard.RunWizard(page1):        
        print "Press open to edit the conf file"  
    
    
    
    if IOError:
        print 'something went wrong'
        
    
    if wx.wizard.EVT_WIZARD_FINISHED:
        from textconf import appen

        

    wizard.Destroy()
    
