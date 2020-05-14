import pandas as pd
path = '/Users/farhanali/Desktop/'
outFile = open(path+'SeedBooks1.cs', 'w')
outFile.close() #use this at the end to close your file

# there are functions for reading both csv and excel files
# df = pd.read_csv() will read a .csv file

path = "/Users/farhanali/Desktop/Spring Semester/MIS 333K/Final Project/Longhorn Data.xlsx"

df = pd.read_excel(io = path, sheet_name = 'Customers')
    # sheetname is used to specify the tab in excel you want to draw the data from

AdvantageNumber = df['Advantage #'].iloc[0]
LastName = df['LastName'].iloc[0]
FirstName = df['FirstName'].iloc[0]
MI = df['MI'].iloc[0]
DOB = df['DOB'].iloc[0]
Street = df['Address'].iloc[0]
City = df['City'].iloc[0]
State = df['State'].iloc[0]
Zip = df['Zip'].iloc[0]
Phone = df['Phone'].iloc[0]
Email = df['E-Mail'].iloc[0]
RewardMiles = df['Miles'].iloc[0]

for i in range(len(df)): #this will iterate through each row with i set as the row #
    AdvantageNumber = df['Advantage #'].iloc[i]
    LastName = df['LastName'].iloc[i]
    FirstName = df['FirstName'].iloc[i]
    MI = df['MI'].iloc[i]
    DOB = df['DOB'].iloc[i]
    Street = df['Address'].iloc[i]
    City = df['City'].iloc[i]
    State = df['State'].iloc[i]
    Zip = df['Zip'].iloc[i]
    Phone = df['Phone'].iloc[i]
    Email = df['E-Mail'].iloc[i]
    RewardMiles = df['Miles'].iloc[i]

    outFile.write("\t\t\t\tCustomer c" + str(i + 1) + " = new Customer()\n")

    outFile.write("\t\t\t\t{\n")

    outFile.write("\t\t\t\t\tAdvantageNumber  = \"" + str(AdvantageNumber) + "\",\n")
    outFile.write("\t\t\t\t\tLastName = \"" + str(Last) + "\",\n")
    outFile.write("\t\t\t\t\tDescription = \"" + str(description) + "\",\n")
    outFile.write("\t\t\t\t\tReleaseDate = new DateTime(" + str(year) + ", " + str(month) + ", " + str(day) + "),\n")
    outFile.write("\t\t\t\t\tPrice = " + str(price) + "m\n")

    outFile.write("\t\t\t\t};\n")

    outFile.write(
        "\t\t\t\tb" + str(i + 1) + ".Genre = db.Genres.FirstOrDefault(g => g.GenreName == \"" + str(genre) + "\");\n")

    outFile.write("\t\t\t\tBooks.Add(b" + str(i + 1) + ");\n\n")
