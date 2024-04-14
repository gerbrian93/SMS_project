import uuid


class Student:
    def __init__(
        self,
        f_name,
        l_name,
        date_of_birth,
        gender,
        address,
        phone_number,
        email,
        student_uuid=None,
    ):
        self.f_name = f_name
        self.l_name = l_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.address = address
        self.phone_number = phone_number
        self.email = email
        if student_uuid:
            self.id = student_uuid
        else:
            self.id = str(uuid.uuid4())

    def __str__(self):
        return (
            "First Name: "
            + str(self.f_name)
            + "\nLast Name: "
            + str(self.l_name)
            + "\nDate of Birth: "
            + str(self.date_of_birth)
            + "\nGender: "
            + str(self.gender)
            + "\nAddress: "
            + str(self.address)
            + "\nPhone Number: "
            + str(self.phone_number)
            + "\nE-mail: "
            + str(self.email)
            + "\nID: "
            + str(self.id)
        )

    def setfname(self, newfname):
        self.fname = newfname
    
    def setlname(self, newlname):
        self.lname = newlname

    def setDob(self, newdob):
        self.date_of_birth = newdob

    def setgender(self, newgender):
        self.gender = newgender

    def setaddress(self, newaddress):
        self.address = newaddress

    def setphonenum(self, newphonenumber):
        self.phone_number = newphonenumber
