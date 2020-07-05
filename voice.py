import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
	print("speak anything: ")
	audio= r.listen(source)
	
	try:
		text=r.recognize_google(audio)
		print("you said :",format(text))
		with open('file.txt',mode ='w') as file: 
			file.write("Recognized text:") 
			file.write("\n") 
			file.write(text) 
			print("complete")


	except:
		print("sorry")
		
