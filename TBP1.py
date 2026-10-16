import csv
import os
n = 20
filename = "seats.csv"
if os.path.exists(filename) == 1 :
    pass
else:
    f=open("seats.csv","w",newline="")
    wo = csv.writer(f)
    for i in range(n):
        senu=i+1
        status='empty'
        name=''
        age=''
        ticketid=''
        if senu in [1,5,9,13,17,4,8,12,16,20]:
             typ='window'
        else :
             typ='Aisle'
        wo.writerow([senu,status,name,age,ticketid,typ])
    f.close()

def showtickets():
     f=open("Seats.csv",'r')
     obj=list(csv.reader(f))
     for a in obj :
          print("seat number "+str(a[0])+" = "+str(a[1])+" ("+str(a[5])+")")


def bookticket():
    print("\n\n------------------------------------------------Ticket Booking----------------------------------------\n\n")
    f=open("seats.csv", "r")
    obj= list(csv.reader(f))
    f.close()
    for a in obj :
         print("seat number "+str(a[0])+" = "+str(a[1])+" ("+str(a[5])+")")
    m=int(input("Enter number of seats you want to book  :  "))
    print("\n\n")
    for i in range(m):
            sn=int(input("Enter your desired seat number for person "+str(i+1)+" :  \n\n"))
            if obj[sn-1][1]=='occupied' :
                 print("That seat is already occupied... choose another from the chart please .\n")
            else:
                 obj[sn-1][1]='occupied'
                 obj[sn-1][2]=input("Enter name of person "+str(i+1)+" :  ")
                 obj[sn-1][3]=int(input("Enter age of person "+str(i+1)+"  :  "))
                 obj[sn-1][4]="725744"+str(obj[sn-1][0])+str(str(obj[sn-1][2][0:3]).upper())+str(obj[sn-1][3])
                 print("Congratulations. You have booked seat number "+str(obj[sn-1][0])+"for "+str(obj[sn-1][2]+"\n\n"))
                 print("Ticket id for the above is : "+str(obj[sn-1][4])+"\n\n")
    fh=open("seats.csv",'w',newline='')
    wo=csv.writer(fh)
    wo.writerows(obj)
    fh.close()
    print("\nThanks for choosing us  :-) ...")
    print("\n\n----------------------------------------------------------------------------------------------------\n\n")



def printticket():
     print("\n\n--------------------------------------------- Print a ticket ---------------------------------------\n\n")
     fh = open("seats.csv",'r')
     obj=list(csv.reader(fh))
     ti=input("Enter your ticket id please :       \n")
     k=0
     for i in range(0,len(obj)):
          if obj[i][4]==ti:
               print("\n\n-------------- Happy Journey ---------------\n\n")
               print("Ticketid    :     "+str(obj[i][4]))
               print("Seat Number :     "+str(obj[i][0]))
               print("Name        :     "+str(obj[i][2]))
               print("Age         :     "+str(obj[i][3]))
               print("Seat type   :     "+str(obj[i][5]))
               break
          else:
               k+=1
               pass
     if k == len(obj):
        print("Provided ticketid does not exist !!...")
     else:
        pass
     fh.close()
     print('\n\n------------------------------------------------------------------------------------------------------------\n\n')


def cancelticket():
     print("\n\n----------------------------------------Ticket Cancellations-------------------------------------------------\n\n")
     fc=open("seats.csv",'r')
     p=0
     obj=list(csv.reader(fc))
     ti=input("Enter your ticket id of the ticket you want to cancel :   ")
     fc.close()
     for a in range(len(obj)):
          if ti == obj[a][4]:
               print("Ticket cancellation is process ...  \n\n")
               print("Your ticket with ticketid "+ti+" and seat number "+obj[a][0]+" has been cancelled.")
               obj[a][1]='Empty'
               obj[a][2]=""
               obj[a][3]=""
               obj[a][4]=""
               break
          else:
               pass
          p+=1
     if a==len(obj):
          print("Ticketid not found... ")
     else:
          pass
     fh=open("seats.csv",'w',newline='')
     wo=csv.writer(fh)
     wo.writerows(obj)
     print("\n\n----------------------------------------------------------------------------------------------------------------\n\n")


'''Main function '''
ans="yes"
while ans == "yes":
     print("\n\n                                           -:              TICKETING MENU              :-                         \n\n")
     print("1. Book a ticket \n2. Print a ticket \n3. Cancel a ticket\n4. Show tickets\n\n")
     h=int(input("Enter your choice from the menu  :   "))
     if h == 1:
          bookticket()
     elif h==2:
          printticket()
     elif h==3:
          cancelticket()
     elif h==4:
          showtickets()
     else:
          print("Invalid choice !!!!!!!!\n")
     ans = input("Do you want to perform any other operation (yes or no )  :   ")

               
