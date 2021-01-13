!pip install hdf5storage
import numpy as np
import hdf5storage as io


def to_fixed(f,e):
    a = f* (2**e)
    b = int(round(a))
    if a < 0:
        # next three lines turns b into it's 2's complement.       
        b = abs(b)        
        b = ~b        
        b = b + 1
    return b

def to_float(x,e):
    c = abs(x)
    sign = 1 
    if x < 0:
        # convert back from two's complement
        c = x - 1 
        c = ~c
        sign = -1
    f = (1.0 * c) / (2 ** e)
    f = f * sign
    return f



b2=1
b4=1.75
b8= 1.984375
b16=1.99993896484375
bits=4
bm=b4


f=open('kernel_1.h','w')
if flag ==1:
   m=np.maximum(-np.percentile(arrc1,p),np.percentile(arrc1,100-p))
else:
   m=np.maximum(np.max(arrc1),-np.min(arrc1))
sc=bm/m
print(m,sc,"kernel_1")
print('float kernel_1[',arrc1.shape[0],'][',arrc1.shape[1],'][',arrc1.shape[2],'][',arrc1.shape[3],'] = {',file=f)
for i in range(arrc1.shape[0]):
    print('{',file=f)
    for j in range(arrc1.shape[1]):
        print('{', end=' ', file=f)
        for k in range(arrc1.shape[2]):
            print('{',end=' ',file=f)
            for l in range(arrc1.shape[3]):
                a= arrc1[i][j][k][l]*sc
                if a>bm:
                  a=bm
                elif a<-bm:
                  a=-bm
                b = to_fixed(a,bits-2)
                c = to_float(b,bits-2)
                # c=a
                if (l!=arrc1.shape[3]-1 ):
                    print(c,end=',', file=f)
                elif (l==arrc1.shape[3]-1 ):
                    print(c,end=' ', file=f)                                      
                
            
            if k!=arrc1.shape[2]-1:
                print( '},' ,end=' \n', file=f)
            else:
                print('}' ,end=' \n', file=f)
        
        if j!=arrc1.shape[1]-1:
            print('},', file=f)
        else:
           print('}', file=f)
    
    if i!=arrc1.shape[0]-1:
        print('},', file=f)
    else:
       print('}', file=f)

print('};',file=f) 

f.close()

datac2=io.loadmat('/content/weightsc2.mat')
arrc2=datac2['wc2']


f=open('kernel_2.h','w')
if flag ==1:
   m=np.maximum(-np.percentile(arrc2,p),np.percentile(arrc2,100-p))
else:
   m=np.maximum(np.max(arrc2),-np.min(arrc2))
sc=bm/m
print(m,sc,"kernel_2")
print('float kernel_2[',arrc2.shape[0],'][',arrc2.shape[1],'][',arrc2.shape[2],'][',arrc2.shape[3],'] = {',file=f)
for i in range(arrc2.shape[0]):
    print('{',file=f)
    for j in range(arrc2.shape[1]):
        print('{', end=' ', file=f)
        for k in range(arrc2.shape[2]):
            print('{',end=' ',file=f)
            for l in range(arrc2.shape[3]):
                a= arrc2[i][j][k][l]*sc
                if a>bm:
                  a=bm
                elif a<-bm:
                  a=-bm
                b = to_fixed(a,bits-2)
                c = to_float(b,bits-2)
                # c=a
                if (l!=arrc2.shape[3]-1 ):
                    print(c,end=',', file=f)
                elif (l==arrc2.shape[3]-1 ):
                    print(c,end=' ', file=f) 
                
            
            if k!=arrc2.shape[2]-1:
                print( '},' ,end=' \n', file=f)
            else:
                print('}' ,end=' \n', file=f)
        
        if j!=arrc2.shape[1]-1:
            print('},', file=f)
        else:
           print('}', file=f)
    
    if i!=arrc2.shape[0]-1:
        print('},', file=f)
    else:
       print('}', file=f)

print('};',file=f) 

f.close()


datad1=io.loadmat('/content/weightsd1.mat')
arrd1=datad1['wd1']

f=open('weights.h','w')

if flag ==1:
   m=np.maximum(-np.percentile(arrd1,p),np.percentile(arrd1,100-p))
else:
   m=np.maximum(np.max(arrd1),-np.min(arrd1))
sc=bm/m
print(m,sc,"weights")
print('float weights[',arrd1.shape[0],'][',arrd1.shape[1],']= {',file=f)
for i in range(arrd1.shape[0]):    
    print('{',end=' ',file=f)
    for j in range(arrd1.shape[1]): 
        a = arrd1[i][j]*sc
        if a>bm:
          a=bm
        elif a<-bm:
          a=-bm
        b = to_fixed(a,bits-2)
        c = to_float(b,bits-2)  
        # c=a      
        if j!=arrd1.shape[1]-1:
            print(c,end=',', file=f)
        else:
           print(c,end=' ', file=f)        
    
    if i!=arrd1.shape[0]-1:
        print('},', file=f)
    else:
       print('}', file=f)

print('};',file=f) 

f.close()



datad1=io.loadmat('/content/weightsd2.mat')
arrd1=datad1['wd2']


f=open('weights1.h','w')

if flag ==1:
   m=np.maximum(-np.percentile(arrd1,p),np.percentile(arrd1,100-p))
else:
   m=np.maximum(np.max(arrd1),-np.min(arrd1))
sc=bm/m
print(m,sc,"weights1")
print('float weights1[',arrd1.shape[0],'][',arrd1.shape[1],']= {',file=f)
for i in range(arrd1.shape[0]):    
    print('{',end=' ',file=f)
    for j in range(arrd1.shape[1]): 
        a = arrd1[i][j]*sc
        if a>bm:
          a=bm
        elif a<-bm:
          a=-bm
        b = to_fixed(a,bits-2)
        c = to_float(b,bits-2)  
        # c=a      
        if j!=arrd1.shape[1]-1:
            print(c,end=',', file=f)
        else:
           print(c,end=' ', file=f)        
    
    if i!=arrd1.shape[0]-1:
        print('},', file=f)
    else:
       print('}', file=f)

print('};',file=f) 

f.close()