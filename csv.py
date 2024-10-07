#  Paula Farebrother
#  Created on 2nd August 2024
#  Last updated Oct 2024

# ________________________________________________________________
#              Module: Retrieve csv file data
# ________________________________________________________________

class CSV:
    def __init__(self, filename):
        self.filename = filename

    def getlist_from_csv(self):
        """ Returns the contents of a csv file as a list of data. """
        with open(self.filename) as file:
            lines = file.readlines()
            str_data = (lines[0].strip().split(","))
            data = [int(num) for num in str_data]
            return data

