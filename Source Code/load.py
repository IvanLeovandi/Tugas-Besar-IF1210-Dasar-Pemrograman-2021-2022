import os 
import argparse
import sys 
def load ():
    print('loading...')
    if len(sys.argv)!=1:
        parser=argparse.ArgumentParser(usage="")
        parser.add_argument("x")
        args=parser.parse_args()
        namafolder=args.x
        if (os.path.exists(args.x)): 
            with open(f"{namafolder}/game.csv",'r') as file:
                game=file.readlines()
            with open(f"{namafolder}/user.csv",'r') as file:
                user=file.readlines()
            with open(f"{namafolder}/riwayat.csv",'r') as file:
                riwayat=file.readlines()
            with open(f"{namafolder}/kepemilikan.csv",'r') as file:
                kepemilikan=file.readlines()
            return (gantikoma(game),gantikoma(user),gantikoma(riwayat),gantikoma(kepemilikan)) 
    else:
        print ("Tidak ada nama folder yang diberikan!")

def gantikoma (x): 
    arraybaru=[]
    for i in x: 
        array=[]
        char=''
        for c in i: 
            if c==";" or c=='' or c=='\n':
                array+=[char]
                char=''
            else : 
                char+=c
        if array!=[''] and char!='':
            arraybaru+=[array+[char]]
        else : 
            arraybaru+=[array]
    return arraybaru 

    
print(load())
 

