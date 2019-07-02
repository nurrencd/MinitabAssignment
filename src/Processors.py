'''
Created on Jun 30, 2019

@author: nurrencd
'''
import csv

class Processor(object):
    def __init__(self):
        pass
        
    def process(self, data):
        '''
        Function for processing data, implemented by children
        '''
        raise NotImplementedError()
    
class Filter(Processor):
    def __init__(self):
        super().__init__()
        
    def process(self, data):        
        newData = []
        for row in data:
            newRow = []
            for datum in row:
                value = self.getFilteredValue(datum)
                if value is not None:
                    newRow.append(value)
            newData.append(newRow)
            
    # return filtered data
        return newData
    
    def getFilteredValue(self, datum):
        '''
        Method for child classes to obtain the end result of a filter
        '''
        raise NotImplementedError()
        
class NumericFilter(Filter):
    '''
    Returns copy of the original data after filtering
    '''
    
    def __init__(self):
        super().__init__()
    
    
    def getFilteredValue(self, datum):
        try:
            return float(datum)
        except ValueError:
            return None
        
class AlphaFilter(Filter):
    '''
    Returns copy of the original data after filtering.
    Needs better heuristic...
    '''
    
    def __init__(self):
        super().__init__()
    
    
    def getFilteredValue(self, datum):
        try:
            float(datum) # clearly a number, therefore abort!
            return None
        except ValueError:
            return datum

class BothFilter(Filter):
    def __init__(self):
        super().__init__()
        
    def getFilteredValue(self, datum):
        try:
            return float(datum)
        except ValueError:
            return datum
        
class CSVReader(Processor):
    def __init__(self):
        super().__init__()
        
    def process(self, data):
        with open(data) as csv_file:
            csv_reader = csv.reader(csv_file)
            newData = []
            for row in csv_reader:
                newData.append(row)
            
    # return filtered data
            return newData

class Printer(Processor):
    def __init__(self):
        super().__init__()
        
    def process(self, data):
        for row in data:
            print(", ".join(map(str, row)))
            
class Sorter(Processor):
    def __init__(self, comparator):
        super().__init__()
        self.comparator = comparator
        
    def process(self, data):
        return self.sort(data)
        
    def sort(self, data):
        for row in data:
            row.sort(key=self.comparator)
        return data
    
def AlphaNumericComparator(a, b):
    case = 0
    try:
        numA = float(a)
    except ValueError:
        case += 1
    try:
        numB = float(b)
    except ValueError:
        case += 1 * 2
    finally:
        if case == 0:
            return numA - numB
        elif case == 1:
            # number before strings
            return 1
        elif case == 2:
            # number before strings
            return -1
        elif case == 3:
            # both are strings
            if a < b:
                return -1
            elif a == b:
                return 0
            else:
                return 1

def AscendingComparator(a, b):
    return AlphaNumericComparator(a, b)

def DescendingComparator(a, b):
    return -1 * AlphaNumericComparator(a, b)
