import numpy as np
#create dictionary for the titles of channels corresponding to the number in csv
Top1 = ['A2', 'C2', 'A4', 'C4', 'A6', 'C6', 'A8', 'C8', 'A13', 'C13', 'A15', 'C15', 'A17', 'C17', 
       'A19', 'C19', 'A24', 'C24', 'A26', 'C26', 'A28', 'C28']
Top2 = ['A30', 'C30', 'A35', 'C35', 'A37', 'C37', 'A39', 'C39', 'A41', 'C41', 'A44', 'B44', 'C47', 
        'A47', 'C49', 'A49', 'C51', 'A51', 'C53', 'A53', 'C58', 'A58']
Top3 = ['C60', 'A60', 'C62', 'A62', 'C64', 'A64', 'C69', 'A69', 'C71',
        'A71', 'C73', 'A73', 'C75', 'A75', 'C80', 'A80', 'C82', 'A82', 'C84', 'A84', 'C86', 'A86']
Bottom1= ['G2', 'E2', 'G4', 'E4', 'G6', 'E6', 'G8', 'E8', 'G13', 'E13', 'G15', 'E15',
          'G17', 'E17', 'G19', 'E19', 'G24', 'E24', 'G26', 'E26', 'G28', 'E28']
Bottom2 = ['G30','E30','G35','E35','G37','E37','G39','E39','G41','E41',
            'F44','G44','E47','G47','E49','G49','E51','G51','E53','G53','E58','G58']
Bottom3 = ['E60','G60','E62','G62','E64','G64','E69','G69','E71','G71',
           'E73','G73','E75','G75','E80','G80','E82','G82','E84','G84','E86','G86']
class Cable:
    def __init__(self, serial_number, matrix):
        self.serial_number = serial_number
        self.matrix = matrix  
    def set_serial_number(self, sn):
        self.serial_number = sn
        def set_matrix(self, matrix):
            self.matrix = matrix

    def __str__(self):
        return f"Cable SN: {self.serial_number}\n"
