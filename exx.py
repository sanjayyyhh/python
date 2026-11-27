# n=int(input("enter the number:"))
# sum=0
# for i in range(n,1):
#     if n%i==0:
#      sum=sum+1

#     if sum==n:
#         print("its perfect number")
#     else:
#         print("not perfect number")

# n=int(input("enter the number of products:"))
# total=0
# for i in range(n):
#     name=input("enter the name:")
#     quantity=int(input("enter the quantity:"))
#     price=float(input("enter the price:"))

#     product_total=quantity*price
#     total=total+product_total

#     if total > 5000:
#         discount=total*0.10
#     else:
#         discount=0

#         final_bill=total-discount


#         print("total:",total)
#         print("discount:",discount)
#         print("final_bill:",final_bill)
        

def book_room(bookings):
    print("\n room book")

    room=int(input("enter your room number:"))
    if room in bookings:
        print("already booked")

    else:
        print("booking not found")

    name=input("enter guest name:")
    room_type=input("enter your room type:",("deluxe,standard,suit")).strip()
    days=int(input("enter the number of days:"))
    while days > 0:
        print("days should be greater than 0:")
        days=int(input("enter the number of days"))

    price=float(input("enter the price"))
    while price > 0:
        print("prices should be greater than 0:")
        price=float(input("enter the price"))

        bookings[room]={
            "guest name":name,
            "room_type":room_type,
            "days":days,
            "price":price

        }
        print("successfully booked!")

def view_booking(bookings):
    print("view booking")

    if len(bookings)==0:
        print("booking not found")

    else:
        for room , details in bookings.items():
         print("\n room number:",room)
         print("guest name:",details["name"])
         print("room_type:",details["room_type"])
         print("number of days:",details["days"])
         print("total price:",details["price"])
         print("================================")

def search_booking(bookings):
    print("search booking")
    room=int(input("enter room number:"))
    if room in bookings:
        print("already booked")
        print("room number:",room)

    for key,values in bookings[room].items():
        print(key,":",values)
    else:
        print("booking not found")


def update_booking(bookings):
    print("update booking")

    room=int(input("enter room number:"))
    if room in bookings:
        days=int(input("enter the updated days: "))

    while days > 0:
        print("days should be greater than 0:")
        days=int(input("enter the updated days:"))
 
        bookings[room]["number of days"]=days
        print("successfully updated")
    else:
        print("booking not found!")

def cancel_booking(bookings):
    print("cancel booking")

    room=int(input("enter room number:"))
    if room in booking:
        del booking[room]
        print("successfully cancelled")

    else:
        print("booking not found")

booking={}

while True:
    print("\n===========================")
    print("hotel booking system")
    print("=============================")
    print("1.book room")
    print("2.view booking")
    print("3.search booking")
    print("4.update booking")
    print("5.cancel booking")
    print("6.exit")
    print("===============================")

    choice=input("enter your choice:").strip()

    if choice=="1":
        book_room(booking)

    elif choice=="2":
        view_booking(booking)

    elif choice=="3":
        search_booking(booking)

    elif choice=="4":
        update_booking(booking)

    elif choice=="5":
        cancel_booking(booking)

    elif choice=="6":
        print("thankyou..")

    else:
        print("invalid choice")
        














        

     