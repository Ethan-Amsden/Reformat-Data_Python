import codecs

"""
Date: 01/20/23
Author: Ethan Amsden
Name: Reformat_Data
Description:
Program reformat_data is used for reformating
data so that it is easier to read.
"""

if __name__ == "__main__":

    # Variables fot the program
    emptyLines = 0
    varDesc = ""
    varGt = ""
    varReformat = ""
    empty = ['\n','\r\n']
    SplitLines = []
    fileLines = []
    reformattedLines = []

    # First Try, Except Block for opening/Closing input file.
    try:
        with codecs.open('Data.txt', 'r', 'utf-8') as inFile:
            # Place file lines in list for access.
            fileLines = inFile.readlines()

            # loop through list of lines to reformat them.
            for line in fileLines:

                # Try, Except block inside loop for reformatting purposes.
                # Reformat the line to have less spaces and a "|" in
                # place of the first "~".
                try:

                    splitLine = line.split("~", 1)
                    varDesc = splitLine[0].rstrip()
                    varGt = splitLine[1].lstrip()
                    varReformat = varDesc + "|" + varGt.rstrip()
                    reformattedLines.append(varReformat)

                    #print to console
                    print(varReformat)

                # If the line is empty count it.
                # If nothing follows a "~", reformat line
                # to have less spaces and a "|"
                except:
                    if line in empty:
                        emptyLines += 1
                                               
                    else:
                        varReformat = line.rstrip() + "|"
                        reformattedLines.append(varReformat)

                        #print to console
                        print(varReformat)

            #print to console
            print("----------------------------------")
            print("Number of empty lines:", emptyLines)
            print("----------------------------------")

    except Exception as error:
        print(error)

    # Second Try, Except block for opening/closing output file.
    try:
        with codecs.open('Data_Output.txt', 'a', 'utf-8') as outFile:

            # Append each newly formtted line into output file
            # in order.
            for newLine in reformattedLines:
                outFile.write(newLine + "\n")

            # Append number of empty lines note to the end of the file.
            outFile.write("Number of empty lines in input file: " + str(emptyLines))
            
    except Exception as error2:
        print(error2)

