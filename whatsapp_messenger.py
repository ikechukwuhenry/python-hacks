# pip install pywhatkit
import pywhatkit as pwk


# using Exception Handling to avoid 
# unprecedented errors
   
try:

    # Define the recepient's phone number (with country code)
    # and the message

    phone_number = "+1234567890"
    message = "Hello, this is an automated message using python!"

    # send the message
    # takes phone number, message and hour in 24 hour format and minutes
    # as parameter
    pwk.sendwhatmsg(phone_number, message, 15, 15)

except:
   
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")
