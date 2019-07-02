#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jun 28, 2019

@author: nurrencd
'''
import sys
from App import Application

def main(args):
    #args = ['C:/Users/nurrencd/Documents/Personal Workspace/MinitabApplication/sample1.csv','alpha', 'ascending']
    app = Application(args)
    
    
    # specifications indicate implicitly adding CSV compatibility and printing
    # so App is being configured in main    
    app.addProcessorToPipeline("csvreader")
    app.setup() # process command-line arguments --> Processors
    app.addProcessorToPipeline("printer")
    
    app.setInitialData(args[0])
    app.run()

if __name__ == '__main__':
    args = sys.argv
    main(args[1:])