import os

#os.system('ls -l')
os.system("dir")
# But using above cmd you don;t get handle to the output it gave.
#So, use the following
stream = os.popen("echo 'Amit Jain'")
output = stream.read()
print(output)