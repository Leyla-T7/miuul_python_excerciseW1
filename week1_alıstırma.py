#2.SORU # string ifadenin tum harflerini buyuk harfe cevırın space yerıne vırgul koyup kelımelerı ayırın
text = "The goal is to turn data into information, and information into insight"
text= text.upper()
list[text.replace("."," ").replace(","," ").upper().split()]


#3.SORU
list=["D","A","T","A","S","C","I","E","N","C","E"]
len(list)
print(list[0],list[10],sep=",")
list[0:4]
del list[8]
list
list.append("w")
list.insert(8,"N")


#4.SORU
dict= {"cristian":["america",18],
       "daisy":["england",12],
       "antonio":["spain",22],
       "dante":["italy",25]}
dict.keys()
dict.values()
dict["daisy"]=["england",13] #12 olan yasi 13 olarak degistirdik
dict["ahmet"]=["turkey",24]  # eleman ekledik
dict.pop("antonio") #antonioyu sildik

#5.SORU
l=[2,13,18,93,22]
def func(l) :
    groups = [[], []]
    for i in l:
        if i%2==0:
            groups[0].append(i)
        else:
            groups[1].append(i)
    print(groups)
    return groups

func(l)
#2.yol comprahensions
l=[2,13,18,93,22]
def func(l):
     groups = [[], []]
     [groups[0].append(i) if i%2==0 else groups[1].append(i) for i in l]
     return groups



#6.SORU  (list comprahensıons kulanarak column adları numreıc degıskenlerın ısmını buyutup baslarına NUM ekledık)
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
["NUM_" + col.upper()  if df[col].dtype!="object" else col.upper() for col in df.columns]

# 7.SORU
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
[col.upper() + "_FLAG" if "no"not in col  else col.upper() for col in df.columns]

#8.SORU
import seaborn as sns
df=sns.load_dataset("car_crashes")
df.columns
og_list= ["abbrev","no_previous"]
new_list=[]
[new_list.append(i) for i in df.columns if i not in og_list]
new_df=df[new_list]