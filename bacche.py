class bacche:

    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major

    def on_honor_role(self):
        if self.gpa >= 4:
            return True
        else:
            return False

