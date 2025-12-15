from django.shortcuts import render
import pymysql

# Create your views here.
def index(request):
    return render(request,'index.html')
def student(request):
    return render(request,'student.html')
def register(request):
    return render(request,'register.html')
def Signup_Action(request):
    full_name=request.POST["full_name"]
    email=request.POST["email"]
    contact_no=request.POST["contact_no"]
    gender=request.POST["gender"]
    username=request.POST["username"]
    password=request.POST["password"]

    con=pymysql.connect(host='localhost',user='root',password='root', database='shopping', charset='utf8')
    cur=con.cursor()
    i=cur.execute("insert into shopyz values('"+full_name+"','"+email+"','"+contact_no+"','"+gender+"','"+username+"','"+password+"')")
    con.commit()
    if i>0:
        context={'data':'Registration successful'}
        return render(request, 'student.html',context)
    else:
        context={'data':'registration failed'}
        return render(request, 'register.html',context)

def LoginAction(request):
    username=request.POST["username"]
    password=request.POST["password"]

    con=pymysql.connect(host='localhost',user='root',password='root',database='shopping',charset='utf8')
    cur=con.cursor()
    i=cur.execute("select * from shopyz where username='"+username+"' and password='"+password+"' ")
    con.commit()
    if i>0:
        context={'data':'login successful'}
        return render(request, 'studenthome.html',context)
    else:
        context={'data':'login failed'}
        return render(request, 'student.html',context)
