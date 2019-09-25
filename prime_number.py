#Prime factors

#Starting main function
def main():

    #Collecting user input 
    number = int ( input ( "Enter the number : " ) )

    #Calculating and displaying prime factors 
    for i in range ( 2, number ):
        while ( number%i == 0 ):
            print ( i  )
            number = number / i

    if ( number > 2 ):
            print ( number )
        

#Calling main function
main()
