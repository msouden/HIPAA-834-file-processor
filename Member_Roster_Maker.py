from __future__ import print_function
import csv, re

filename = input('Please enter the client-supplied file to convert with the 834 extension:> ')
outputFile = 'Output for ' + filename + '.csv'
linebreakfix = 'Linebreak_fixed_' + filename + '.txt'

#Define correct line endings
beginLine1 = 'INS*Y'
beginLine2 = 'INS*N'
beginReplace1 = '\nINS*Y'
beginReplace2 = '\nINS*N'

#Define first column data (done differently to accomodate *INS* occurring in data)
col1offset = 0
col1length = 12

# All the black magic RegEx to find our columns
col1 = re.compile(r'^INS\*(.*?)(?=\~)') # Y & Relation
col2 = re.compile(r'(?<=REF\*0F\*)(.*?)(?=\~)') # Some Num
col3 = re.compile(r'(?<=REF\*1L\*)(.*?)(?=\~)') # A/M - some code
col4 = re.compile(r'(?<=REF\*23\*)(.*?)(?=\~)') # Member ID
col5 = re.compile(r'(?<=REF\*ZZ\*)(.*?)(?=\~)') # - 2 digit code
col6 = re.compile(r'(?<=DTP\*336\*D8\*)(.*?)(?=\~)') # Date (DOH?)
col7 = re.compile(r'(?<=DTP\*356\*D8\*)(.*?)(?=\~)') # Date
col8 = re.compile(r'(?<=NM1\*IL\*1\*)(.*?)(?=\~)') # Name
col9 = re.compile(r'(?<=PER\*IP\*\*HP\*)(.*?)(?=\~)') # Phone
col10 = re.compile(r'(?<=\~N3\*)(.*?)(?=\~)') # Street
col11 = re.compile(r'(?<=\~N4\*)(.*?)(?=\~)') # City, ST, Zip
col12 = re.compile(r'(?<=DMG\*D8\*)(.*?)(?=\~)') # DOB & Gender
col13 = re.compile(r'(?<=HD\*030\*\*HLT\*)(.*?)(?=\~)') # Relation
col14 = re.compile(r'(?<=DTP\*348\*D8\*)(.*?)(?=\~)') # Date (updated?)

# strip linebreaks
with open(filename, 'r') as fh:
    with open('tempfile.txt','w') as fw:
        for line in fh:
            line = line.rstrip('\n')+('~') #adds "~" as delimiter. Change to comma later & test
            fw.write(line)

# write tempfile with correct linebreaks    
    with open('tempfile.txt','r') as fw:
        with open('lineBreakFix.txt', 'w') as fl:
            for line in fw:
                fl.write( line.replace( beginLine1, beginReplace1 ).replace( beginLine2, beginReplace2 ) )
        
        print("A copy of the complete file has been created with more readable line breaks as lineBreakFix.txt")
        
        with open( 'lineBreakFix.txt', 'r' ) as fr:
            with open( outputFile, 'w' ) as fo:   
                line_count = 0 # Counting Members
                for line in fr:
                    if line_count == 0: # Put in Header Row
                        fo.write('Subscriber Status,Member Prefix,Member ID,UNK,DOH(?),Date,Name,Telephone,Street,City,State,Zip,DOB,Gender,Relation,Date\n')
                    else: # Write Out Cols Line by line
                        if col1.search(line):
                            fo.write(re.search(col1, line).group(0)+',')
                        else: fo.write( ',' )
                        # if col2.search(line):    <<<<----- A number we do not need.
                        #     fo.write(re.search(col2, line).group(0)+',')
                        # else: fo.write( ',' )
                        if col3.search(line):
                            fo.write(re.search(col3, line).group(0)+',')
                        else: fo.write( ',' )
                        if col4.search(line):
                            fo.write(re.search(col4, line).group(0)+',')
                        else: fo.write( ',' )
                        if col5.search(line):
                            fo.write(re.search(col5, line).group(0)+',')
                        else: fo.write( ',' )
                        if col6.search(line):
                            fo.write(re.search(col6, line).group(0)+',')
                        else: fo.write( ',' )
                        if col7.search(line):
                            fo.write(re.search(col7, line).group(0)+',')
                        else: fo.write( ',' )
                        if col8.search(line):
                            fo.write(re.search(col8, line).group(0)+',')
                        else: fo.write( ',' )
                        if col9.search(line):
                            fo.write(re.search(col9, line).group(0)+',')
                        else: fo.write( ',' )
                        if col10.search(line):
                            fo.write(re.search(col10, line).group(0)+',')
                        else: fo.write( ',' )
                        if col11.search(line):
                            fo.write(re.search(col11, line).group(0).replace("*", ",")+',')
                        else: fo.write( ',,,' )
                        if col12.search(line):
                            fo.write(re.search(col12, line).group(0).replace("*", ",")+',')
                        else: fo.write( ',,' )
                        if col13.search(line):
                            fo.write(re.search(col13, line).group(0)+',')
                        else: fo.write( ',' )
                        if col14.search(line):
                            fo.write(re.search(col14, line).group(0)+',')
                        else: fo.write( ',' )
                        fo.write('\n')
                    line_count += 1
                fo.write('Member Count is: ' + str(line_count))
                print('Member Count is: ' + str(line_count))
                print('Done. Press any key to close this window.')
                input()
                