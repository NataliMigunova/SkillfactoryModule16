class PartyAttender:

    def __init__(self, name, city_from, type):
        self.name = name
        self.city_from = city_from
        self.type = type

    def get_attender_info(self):
        return


class AttenderMentor(PartyAttender):

    def __init__(self, name, city_from):
        PartyAttender.__init__(self, name, city_from, "Mentor")


class AttenderStudent(PartyAttender):

    def __init__(self, name, city_from):
        PartyAttender.__init__(self, name, city_from, "Student")


class SuperBoss(PartyAttender):

    def __init__(self, name, city_from):
        PartyAttender.__init__(self, name, city_from, "Super Boss")

