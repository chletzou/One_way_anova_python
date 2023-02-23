
class test:
    #constructor
    def __init__(self, type, imm, rea, enj, com):
        self.type = type
        self.imm = imm
        self.rea = rea 
        self.enj = enj
        self.com = com

class game:
    #constructor
    def __init__(self, name, A1, B, A2, C):
        self.name = name
        self.A1 = A1
        self.B = B 
        self.A2 = A2
        self.C = C

class user:
    #constructor
    def __init__(self, G1, G2, G3, G4):
        self.G1 = G1
        self.G2 = G2
        self.G3 = G3
        self.G4 = G4


#if __name__ == '__main__':

#    test_opject = test('audiobased', imm=3,rea=4,com=5,type=8787)
#    test_opject2 = test('audiobased', 3,4,5,6)
#    game_object = game('HLA', test_opject,test_opject2,test_opject, test_opject)
#    print(game_object.B.com)

