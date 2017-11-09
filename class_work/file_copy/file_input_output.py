#This program writes three lines of data to a file.

def main():
    outfile = open('philosophers.txt','w')

    outfile.write("John Locke\n")
    outfile.write("Aristotle\n")
    outfile.write("Plato\n")

#close the file.
    outfile.close()

#call the main function.
main()
