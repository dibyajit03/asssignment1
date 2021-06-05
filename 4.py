 
def freq(str1):

	
	str1 = str1.split()		
	str2 = []

	
	for i in str1:			
         if i not in str2:
            str2.append(i)
			
	for i in range(0, len(str2)):
         print( str2[i], ' ', str1.count(str2[i]),len(str2[i]))	

def main():
        n = int(input("Enter number of words : ")) 
        a = list(input("\nEnter the words by space: ").strip().split())[:n] 
        listToStr = ' '.join([str(elem) for elem in a])
        print( listToStr)
        #str1 ='New Old Existing New New '
        freq(listToStr )					

if __name__=="__main__":
	main()	