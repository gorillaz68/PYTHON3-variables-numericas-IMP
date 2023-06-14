from limite import *
from menu import *
from control import *
from entrada import *
num=leeNum()
num2=leeNum() #sustituye por zero
opt=menu()
print ("la opcion es :"+opt)
res=control(opt,num,num2)
escribir(res,opt)
