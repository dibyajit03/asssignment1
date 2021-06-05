def main():
    v = int(input("Enter number of chocolate : ")) 
    m = int(input("tot amount : ")) 

    numbers= list(map(int,input("\nEnter the n chocolate price : ").strip().split()))

    target_number = m

    for i, number in enumerate(numbers[:-1]): 
        complementary = target_number - number
        if complementary in numbers[i+1:]:  
            print("Solution Found: {} {}".format(number, complementary))
            break
    else: 
        print("No solutions exist")
					

if __name__=="__main__":
	main()