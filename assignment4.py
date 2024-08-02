list=[]
rating=[]

def get_ratings(f):

    for line in f:
        list.append(line.strip())

try:
    f1=open("feedback1.txt",'r') 
    f2=open("feedback2.txt",'r') 
    f3=open("feedback3.txt",'r') 
    get_ratings(f1)
    get_ratings(f2)
    get_ratings(f3)
    for i in range(len(list)):
        rating.append(list[i].split()[1])
    sum=0
    for i in rating:
        sum+=int(i)
    sum=sum/len(list)
    f1.close()
    f2.close()
    f3.close()
except(FileNotFoundError ):
    print("File not found",FileNotFoundError)


try:
    fs=open("feedback_summary.txt",'w')
    fs.writelines(f"Total Feedback Entries:{len(list)}\n")
    fs.writelines(f"Average Rating: {round(sum,2)}\n")
    fs.writelines("\nFeedbacks:\n")
    for feedbacks in list:
        fs.writelines(f"{feedbacks}\n")
except(Exception):
    print("error",Exception)
