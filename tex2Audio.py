#/!/Users/antonio/opt/anaconda3/bin/python
#python == 3.10.7
#by Visi@n 20221008 h.13.41

from datetime import datetime
import os, sys
import argparse
import time
from googletrans import Translator
import googletrans
import pygame
pygame.init()
import time
from gtts import gTTS 

translator = Translator() 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-s", "--source", required=True,
#	help="id microphone source")
ap.add_argument("-i", "--input", default="txt_en",# required=True,
	help="input directory TXT ")
ap.add_argument("-l", "--language", default="en",#required=True,
	help="input language, default Italian en")
ap.add_argument("-o", "--output", default="it",#required=True,
	help="output language, default Italian it")
#ap.add_argument("-t", "--type", default="wav",  type=str,#required=True,
#	help="type format file ogg mp3 flv wav opus")


args = vars(ap.parse_args())


global datastamp
datastamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

dirs = os.listdir(str(args["input"]))

outputdirectory = (datastamp)

if not os.path.exists(outputdirectory):
	os.makedirs(outputdirectory)

documentoHTML = open(outputdirectory+"\\"+datastamp+".html", "a", encoding='utf-8')
documentoHTML.write("<html>")
documentoHTML.write("<head>")

documentoHTML.write("<style>")
documentoHTML.write("table, th, td {")
documentoHTML.write("	  border: 1px solid black;")
documentoHTML.write("}")
documentoHTML.write("</style>")
documentoHTML.write("<title>")
documentoHTML.write(str(args["input"]))
documentoHTML.write("</title>")
documentoHTML.write("</head>")
documentoHTML.write("<h3><font color='darkblue'> Text2Audio2Translate by Visi@n </font></h3>")
documentoHTML.write("<br><br>")

documentoHTML.write("<body  text='darkblue'>")#background='http://www.broi.it/xxx/terra.jpg'
documentoHTML.write("<table>")

	
	
for file in dirs:
	filestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") 

	print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
	fileditesto = (str(args["input"])+'\\'+str(file))
	print(fileditesto)
	f = open(str(fileditesto),"r")
	contenutofile = (f.read())  
	print(contenutofile) 
	f.close()
	#################################à translate #######################################
	rigatransA = translator.translate(contenutofile,dest=str(args["output"])).text
	print("¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶")
	print(rigatransA)
	print('                                                                    ')
	
	########################################################## save audio translated in mp3##########################
	# Language of original text 
	#global language
	language = (args["language"])
	# have a high speed 
	myobj = gTTS(text=contenutofile, lang=language, slow=False) 
	# welcome  
	myobj.save(datastamp+'\\'+str(file)+'.mp3') 
	# Playing the converted file 
	pygame.mixer.music.load(datastamp+'\\'+str(file)+'.mp3') 

	##########################################################			
	
	# Language in which you want to convert 
	#global language
	language = (args["output"])
	# have a high speed 
	myobj = gTTS(text=rigatransA, lang=language, slow=False) 
	# welcome  
	myobj.save(datastamp+'\\'+str(file)+'_'+str(args['output'])+'.mp3') 
	# Playing the converted file 
	pygame.mixer.music.load(datastamp+'\\'+str(file)+'.mp3') 

	##########################################################				
	
	documentotradotto = open(datastamp+'\\'+str(file)+'_'+str(args['output'])+'.csv', "a", encoding='utf-8')
	documentotradotto.write(str(rigatransA))
	documentotradotto.close()
	
	documentoHTML.write("<tr><td><h4><font color='darkblue'><a target=\'_blank\' href=\'"+"..\\"+datastamp+'\\'+str(file)+'.mp3'+"\'>"+datastamp+'\\'+str(file)+'.mp3'+"</font></a></h2><br>")
	documentoHTML.write("<h4><font color='darkblue'><a target=\'_blank\' href=\'"+"..\\"+datastamp+'\\'+str(file)+'_'+str(args['output'])+'.mp3'+"\'>"+datastamp+'\\'+str(file)+'_'+str(args['output'])+'.mp3'+"</font></a></h2></td>")

		
	documentoHTML.write("<td><h4><font color='darkblue'>"+contenutofile+"<br><p align='center'>"+"= = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = </p>"+rigatransA+"<br></font></h2></td></tr>")

	
documentoHTML.write("</table>")
documentoHTML.write("</body>")
documentoHTML.write("</html>")
documentoHTML.close()
print(documentoHTML)
os.startfile(outputdirectory+"\\"+datastamp+".html")	
	
	
