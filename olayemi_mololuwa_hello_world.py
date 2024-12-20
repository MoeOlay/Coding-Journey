from datetime import datetime
Day_Of_Week = datetime.now().strftime("%A")
Time_Now = datetime.now().strftime("%I:%M.%S%p")
print("Hello!\nWelcome to CSC 1301 Principles of Computer Science I Course!\nOur Class is help every Monday and Wednesday at 11:00am.\nOur Lab session is held every " + Day_Of_Week + " at " + Time_Now)