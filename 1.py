import datetime
def timeconvert(str1):
      #str1=input("Enter times : ")
      if str1[-2:] == "AM" and str1[:2] == "12":
         return "00" + str1[2:8]
      elif str1[-2:] == "AM":
         return str1[:-2]
      elif str1[-2:] == "PM" and str1[:2] == "12":
         return str1[:8]
      else:
         return str(int(str1[:2]) + 12) + str1[2:8]

def main():
      str1=input("Enter time : ")
      #str1 ='08:55:48 PM'
      print(timeconvert(str1))					

if __name__=="__main__":
	main()