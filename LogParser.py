import os
import fnmatch

def main():     
    # Use a Dictionary of list to store Bug numbers and corresponding Log Signatures
    errorDict = { 
                1234: ["error1", "error2"],
                5678: ["error3", "error4"],
                9999: ["error6", "error5"]
                }

    for file in os.listdir('.'):
      if fnmatch.fnmatch(file, 'Log*.txt'):
        FindMatchingErrorsInFile(file, errorDict)   
      
# Function takes filename and Error Dictonary and finds the matching lines 
def FindMatchingErrorsInFile(fileName, errorDict):
    _lineNumber = 0
    _matchingCount = 0 

    print("For " + fileName + ":")
    
    with open(fileName, 'r') as file:
      for line in file:
        _lineNumber += 1
        
        for bugid in errorDict:
          for error in errorDict[bugid]:
            if error in line:
              _matchingCount += 1
              print("At line %s signature match with bug %s" % (_lineNumber, bugid))    
    file.close

    if _matchingCount == 0:
      print ("No signatures matches!")

if __name__ == "__main__": main()