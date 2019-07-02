'''
Created on Jun 28, 2019

@author: nurrencd
'''

import Processors as p
from functools import cmp_to_key

class Application(object):
    '''
    classdocs
    '''

    def __init__(self, args):
        '''
        Constructor
        '''
        self.args = args
        self.processors = {}
        self.pipeline = []
        self.data = None
        
        #set up defined processors
        self.processors["numeric"] = p.NumericFilter()
        self.processors["alpha"] = p.AlphaFilter()
        self.processors["both"] = p.BothFilter()
        
        self.processors["ascending"] = p.Sorter(cmp_to_key(p.AscendingComparator))
        self.processors["descending"] = p.Sorter(cmp_to_key(p.DescendingComparator))
        
        self.processors["csvreader"] = p.CSVReader()
        self.processors["printer"] = p.Printer()
        
    def setup(self):
        '''
        Appends each command-line argument processor to the pipeline. Assumes each argument is an already-
        provided processor.
        '''
        for arg in self.args[1:]:
            try:
                print(arg)
                p = self.processors[arg]
                self.pipeline.append(p)
            except KeyError:
                print("Processor for",arg,"not found.")
                continue
    
    def run(self):
        '''
        Runs the application with the specified configuration parameters.
        '''        
        # read csv, save original data
        # setup pipeline from arguments
        
        # run pipeline
        data = self.data # initialization
        for proc in self.pipeline:
            data = proc.process(data)
    
    def addProcessorToPipeline(self, name):
        try:
            processor = self.processors[name]
            self.pipeline.append(processor)
        except KeyError:
            print("No processor of name",name,"found")
        
    def addProcessor(self, name, processor):
        self.processors[name] = processor
        
    def setInitialData(self, data):
        self.data = data
        