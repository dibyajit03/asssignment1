def markcom(zip):
    n = int(input("Enter number of tests : ")) 
    Alice_mark = list(map(int,input("\nEnter the scores for alice separated by space : ").strip().split(" ")))
    bob_mark = list(map(int,input("\nEnter the scores for bob separated by space : ").strip().split(" ")))
    print("\nalice marks are - ",Alice_mark) 
    print("\nbob marks are - ",bob_mark) 
    i=0
    j=0
    for l1,l2 in zip(Alice_mark,bob_mark):
        if l1 < l2:
            #print("l1 < l2")
            j+=1
        elif l1 > l2:
            #print("l2 > l1")
            i+=1
        elif l1 == l2:
            pass
    print("Alice",i)
    print("Bob",j)
    #if l1 < l2:
        #print("bob",j)
    #else:
        #print("alic",i)
        #print(i,j)
    if i>j:
        print("Alice won the competition")   
    elif i<j:
        print("Bob won the competition")
    else:
    	print("It's a tie")
        
def main():	
	markcom(zip)					

if __name__=="__main__":
	main()