import urllib
web = raw_input("http location: ")
filename = raw_input("Enter the filename: ")



def urlOpen(http, name):
     pfile = open(name + '.log', 'w')
     filehandle = urllib.urlopen(http)
     for lines in filehandle.readlines():
                    str(lines)    
                    pfile.write(lines)
                    
urlOpen(web,filename)
