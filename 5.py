from operator import itemgetter
def markcom():	

    n = int(input("Enter number of books : ")) 
    L1 = list(map(int,input("\n books and their details (no.of pages, price and no.of chapters). : ").strip().split()))
    L2 = list(map(int,input("\n books and their details (no.of pages, price and no.of chapters). : ").strip().split()))
    L3 = list(map(int,input("\n books and their details (no.of pages, price and no.of chapters). : ").strip().split()))
    test_list = [L1,L2,L3]



    print ("The original list is : " + str(test_list))


    m = int(input(" please select the attribute  : ")) 
    if m ==1:
        res = sorted(test_list, key = itemgetter(1))

    
        print ("List after sorting by 2nd element of lists : " + str(res))
    elif m==0:
        res = sorted(test_list, key = itemgetter(0))

    
        print ("List after sorting by 1st element of lists : " + str(res))

    elif m==2:
        res = sorted(test_list, key = itemgetter(2))

    
        print ("List after sorting by 3rd element of lists : " + str(res))
def main():
	markcom()					

if __name__=="__main__":
	main()
