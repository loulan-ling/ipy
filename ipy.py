import os 
import sys
from IPy import IP

ip = sys.argv[1]
ip2 = sys.argv[2]
ip3 = sys.argv[3]
rate = sys.argv[4]
name = ip+ip2+"-"+ip3
filename = ip+ip2+"-"+ip3+".txt"
os.mknod("./"+filename)
file_handle=open(filename,mode='w')

 # file = open()
 # file.write(msg)
 # text_create(filename, 'Hello world!')
for i in range(int(ip2),int(ip3)+1):
        ipsum = str(ip)+str(i)
        file_handle.write(ipsum+'\n')
file_handle.close()
#val = os.system("masscan -h")
val = os.system("masscan -iL "+filename+" -p0-65535 -oX "+name+".xml --max-rate "+rate)
print val
vapython = os.system("python ./masscan-report-converter.py -i ./"+name+".xml -o ./"+name+".xls")
print vapython
print '----------------------------'
print 'ok'
# ip = IP('10.182.127.130-190/24')
         # print (ip.len())
         # for i in ip:
         #     print (i)
