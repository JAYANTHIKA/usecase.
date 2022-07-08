import time
import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(host="localhost", user="root", password="ammappa123*#", database="house_tenant")
mycursor = mydb.cursor()


class checking_process:
    def _init_(self, name, password):
        self.name = name
        self.password = password

    def check(self):
        mycursor.execute("select * from user_details where name like %s", (self.name,))
        details = mycursor.fetchall()
        for i in details:
            if i[1] == self.name and i[2] == self.password:
                return i[0]


class selecting_process:
    def _init_(self, existing_user):
        self.user_id = existing_user

    def sel_pro(self):
        user_requ = input("ender the address of the house: ")
        mycursor.execute("select house_id from house1_detail where house_address like %s", (user_requ,))
        details = mycursor.fetchall()
        for i in details:
            return i[0]


class ten_owner:
    def _init_(self, existing_user, final_selection):
        self.user_id = existing_user
        self.house_id = final_selection

    def request_process(self):
        data = datetime.now()
        formattedDate = data.strftime('%Y-%m-%d %H:%M:%S')
        a = "approved"
        mycursor.execute("insert into request_table2(is_approved,house_id,user_id,date) values(%s,%s,%s,%s)",
                         (a, self.house_id, self.user_id, formattedDate,))
        mydb.commit()
        mycursor.execute("select * from request_table2 where user_id like %s and house_id like %s",
                         (self.user_id, self.house_id,))
        details = mycursor.fetchall()
        for i in details:
            return i[0]


class approval_tab:
    def _init_(self, existing_user):
        self.houseid = existing_user

    def app(self):
        mycursor.execute("select * from house1_detail where user_id like %s", (self.houseid,))
        details = mycursor.fetchall()
        for i in details:
            return i[0]  # house owner's house_id


class approver_approval:
    def _init_(self, wo_app):
        self.house_id = ow_app

    def app_notapproved(self):
        mycursor.execute("select * from approver_detail")
        details = mycursor.fetchall()
        approver_person_id = details[0][0]
        a = "Approved"
        mycursor.execute("insert into approval_tabl(house_id,approver_id,is_approved) values(%s,%s,%s)",
                         (self.house_id, approver_person_id, a))
        mydb.commit()
        mycursor.execute("select approval_id from approval_tabl")
        details = mycursor.fetchall()
        for i in details:
            return i[0]


class addver_requied:
    def _init_(self, approval_table):
        self.approval_id = approval_table

    def advertise(self):
        mycursor.execute("select * from administration")
        details = mycursor.fetchall()
        administration_id = details[0][0]
        a = 10
        mycursor.execute("insert into advertise_table1(admin_id,approval_id,time) values(%s,%s,%s)",
                         (administration_id, self.approval_id, a,))
        mydb.commit()


class payment_method:
    def _init_(self, request_id):
        self.request_id = request_id

    def payment_process(self):
        k = int(input("IF U REALLY WANT TO BUY THEN MAKE THE PAYMENT AS SOON AS POSSIBLE :TRUE-->1 OR -->2 "))
        if k == 1:
            payment_method = input("which method do you want to pay either online or case?: ")
            if payment_method == 'online':
                ccv = int(input("enter your ccv no of your account: "))
                accountHolderName = str(input('Enter your account holder name: '))
                accountNumber = int(input('Enter your account number: '))
                month = int(input('Enter your account valid month: '))
                year = int(input('Enter your account valid year: '))
                mycursor.execute(
                    "insert into payment1(payment_method,account_holdername,account_no,month,year,ccv,request_id) values(%s,%s,%s,%s,%s,%s,%s)",
                    (payment_method, accountHolderName, accountNumber, month, year, ccv, self.request_id,))
                mydb.commit()
            else:
                mycursor.execute("insert into payment1(payment_method,request_id) values(%s,%s)",
                                 (payment_method, self.request_id,))
                mydb.commit()
                print("Then make the payment as soon as possible with a case amount: ")
            mycursor.execute("select * from payment")
            details = mycursor.fetchall()
            for i in details:
                return i[0]


class history_user:
    def _init_(self, existing_user):
        self.user_id = existing_user

    def find_history(self):
        mycursor.execute(
            "select distinct request_table2.user_id,house1_detail.locality,house1_detail.city,house1_detail.square_feet,house1_detail.type,house1_detail.rent_type,house1_detail.house_address from request_table2 inner join payment1 on request_table2.request_id=payment1.request_id inner join user_details on request_table2.user_id=user_details.user_id inner join house1_detail on house1_detail.house_id=request_table2.house_id where request_table2.user_id like %s",
            (self.user_id,))
        details = mycursor.fetchall()
        print("HISTORY OF USER:")
        for i in details:
            print("locality:", i[1], "city:", i[2], "square_feet:", i[3], "type:", i[4], "rent_type:", i[5],
                  "house_address:", i[6])


class ad_specific:
    def _init_(self, existing_user):
        self.user_id = existing_user

    def process(self):
        k = "yes"
        mycursor.execute(
            "select distinct user_details.user_id,house1_detail.house_id from request_table2 inner join  house1_detail on request_table2.house_id=house1_detail.house_id inner join user_details on user_details.user_id=request_table2.user_id where house1_detail.is_addvertisement like %s and request_table2.user_id like %s",
            (k, self.user_id,))
        details = mycursor.fetchall()
        for i in details:
            return 1


class admin_checking_process:
    def _init_(self, name, password):
        self.name = name
        self.password = password

    def admin_proces(self):
        mycursor.execute("select * from administration where admin_name like %s", (self.name,))
        details = mycursor.fetchall()
        for i in details:
            if i[1] == self.name and i[2] == self.password:
                return i[0]


class check_approver:
    def _init_(self, name, password):
        self.name = name
        self.password = password

    def process_chk(self):
        mycursor.execute("select * from approver_detail where approver_name like %s", (self.name,))
        details = mycursor.fetchall()
        for i in details:
            if i[1] == self.name and i[2] == self.password:
                return i[0]


if _name == "main_":
    getting_user = input(
        "if you are a user then you can put -->u or if you are an admin then put-->admin or if you are an approver then put-->approver: ")
    name = input("Enter u r name: ")
    password = input("enter u r password: ")
    if getting_user == 'u':
        checking = checking_process(name, password)
        existing_user = checking.check()
        if existing_user:
            question_ask = input(
                "DO TOU WANT TO KNOW ABOUT THE HOUSE SOLD DETAILS?--->sold or HOW ARE ALL BROUGHT THE HOUSE?--->brought ")
            if question_ask == "sold":
                mycursor.execute(
                    "select distinct user_details.name,house1_detail.locality,house1_detail.city,house1_detail.house_address from user_details inner join house1_detail on user_details.user_id=house1_detail.user_id inner join request_table2 on request_table2.house_id=house1_detail.house_id inner join payment1 on payment1.request_id=request_table2.request_id")
                details = mycursor.fetchall()
                for i in details:
                    print("name:", i[0], "locality:", i[1], "city:", i[2], "house_address:", i[3])
            elif question_ask == "brought":
                mycursor.execute(
                    "select distinct user_details.name from user_details inner join request_table2 on user_details.user_id=request_table2.user_id inner join payment1 on payment1.request_id=request_table2.request_id")
                details = mycursor.fetchall()
                for i in details:
                    print("NAME:", i[0])
            tenant_or_owner = int(input("tenant-->1 or owner-->2:"))
            if tenant_or_owner == 2:
                locality = input("enter u r location: ")
                city = input("enter u city: ")
                sq_feet = input("enter the square feet of u r property: ")
                type = input("type of house:")
                rent_type = input("rent_type: ")
                is_advertisement = input("do u want adverdisement: ")
                house_address = input("enter the addrees of the house: ")
                mycursor.execute(
                    "insert into house1_detail(locality,city,square_feet,type,rent_type,is_addvertisement,user_id,house_address) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                    (locality, city, sq_feet, type, rent_type, is_advertisement, existing_user, house_address,))
                mydb.commit()
                owner_appoval_tab = approval_tab(existing_user)
                ow_app = owner_appoval_tab.app()
                # house_id will be return here

                # approver table
                app_approval = approver_approval(ow_app)
                approval_table = app_approval.app_notapproved()
                print(approval_table)

                # advertisment
                add_require = addver_requied(approval_table)
                advertisement = add_require.advertise()

            else:
                mycursor.execute(
                    "select distinct house1_detail.house_id,house1_detail.locality,house1_detail.city,house1_detail.square_feet,house1_detail.type,house1_detail.rent_type,house1_detail.house_address from house1_detail inner join approval_tabl on house1_detail.house_id=approval_tabl.house_id")
                details = mycursor.fetchall()
                for i in details:
                    print('locality: ', i[1], 'city :', i[2], 'square_feet: ', i[3], 'type: ', i[4], 'rent_type: ',
                          i[5], 'house_address: ', i[6])
                house_sel = selecting_process(existing_user)
                final_selection = house_sel.sel_pro()
                print(final_selection)
                request = ten_owner(existing_user, final_selection)
                request_id = request.request_process()
                # payment process
                pay = payment_method(request_id)
                payment = pay.payment_process()
                want_history = int(input("if you want your histrory of rentals then print 1 or else print 0 "))
                if want_history == 1:
                    history = history_user(existing_user)
                    history.find_history()
                addd = ad_specific(existing_user)
                value = addd.process()
                if value == 1:
                    n = 2
                    while (n):
                        time.sleep(2)
                        print("HELLO EVERYONE!!!........THIS IS IS FOR YOUR ENTERTAINMENT GUYS BE COOOOLLLLLL........")
                        time.sleep(2)
                        print("WAKE UP!!!!......BRO!!!")
                        n = n - 1

        else:
            phone_no = int(input("enter u r phone no: "))
            email = input("enter u r emil_id: ")
            address = input("enter u r address: ")
            aadhaar_no = int(input("enter u r aadhaar no: "))
            mycursor.execute(
                "insert into user_details(name,password,phone_no,email,address,aadhaar_no) values(%s,%s,%s,%s,%s,%s)",
                (name, password, phone_no, email, address, aadhaar_no,))
            mydb.commit()
    elif getting_user == "admin":
        admin_check = admin_checking_process(name, password)
        admin_id = admin_check.admin_proces()
        if admin_id:
            # THE ADMIN CAN SEE WHAT ARE PROCESS AS OF NOW GOING ON IN THE APPLICATION
            mycursor.execute(
                "select distinct user_details.name,user_details.password,user_details.phone_no,user_details.email,user_details.address,user_details.aadhaar_no,house1_detail.user_id,house1_detail.locality,house1_detail.city,house1_detail.square_feet,house1_detail.type,house1_detail.rent_type,house1_detail.house_address,house1_detail.is_addvertisement from request_table2 inner join payment1 on request_table2.request_id=payment1.request_id inner join user_details on request_table2.user_id=user_details.user_id inner join house1_detail on house1_detail.house_id=request_table2.house_id")
            details = mycursor.fetchall()
            for i in details:
                print("USER NAME:", i[0], 'PASSWORD:', i[1], 'PHONE NO:', i[2], 'EMAIL', i[3], 'ADDRESS:', i[4],
                      'AADHAAR NO:', i[5], 'LOCALITY:', i[7], 'CITY:', i[8], 'SQUARE_FEET:', i[9], 'TYPE:', i[10],
                      'RENT TYPE:', i[11], 'ADVERTISEMENT:', i[12])
    elif getting_user == "approver":
        approver_check = check_approver(name, password)
        approve = approver_check.process_chk()
        if approve:
            # approver can see the process which are in the approval table
            mycursor.execute(
                "select distinct house1_detail.locality,house1_detail.city,house1_detail.square_feet,house1_detail.type,house1_detail.rent_type,house1_detail.house_address,house1_detail.is_addvertisement,user_details.email,user_details.address from approval_tabl inner join house1_detail on approval_tabl.house_id=house1_detail.house_id inner join user_details on house1_detail.user_id=user_details.user_id")
            details = mycursor.fetchall()
            for i in details:
                print('locality:', i[0], 'city:', i[1], 'square_feet:', i[2], 'type:', i[3], 'rent_type:', i[4],
                      'house_address:', i[5], 'is_addvertisement:', i[6], 'email:', i[7], 'address:', i[8])