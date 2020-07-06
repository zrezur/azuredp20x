# Endpoint=sb://iotbus-ns.servicebus.windows.net/;SharedAccessKeyName=Policy1;SharedAccessKey=H8CUEFbi96yd8GVv/EmsR5m1QR/SWg+IdFhjxh27XsQ=;EntityPath=iotinput
# V6A6/xA0JDZsn+B776Gy0oTK2t9vSl9JPHff/wCkHPY=
#!/usr/bin/python3
import sys
from azure.servicebus import ServiceBusService
import datetime
from random import randint
from time import sleep
import demjson

if len(sys.argv) !=5:
	print("Usage: ./simulator <servicebus> <inputEventHubPolicyName> <inputEventHubPolicyKey> <inputEventHubName>")
else:
	servicebus, inputEventHubPolicyName, inputEventHubPolicyKey, inputEventHubName = sys.argv[1:]
	service_name = servicebus
	key_name = inputEventHubPolicyName # SharedAccessKeyName from Azure portal
	key_value = inputEventHubPolicyKey # SharedAccessKey from Azure portal
	sbs = ServiceBusService(service_name,shared_access_key_name=key_name,shared_access_key_value=key_value)
	
	m1 = "E001"
	m2 = "E002"
	m3 = "E003"
	
	
	t1 = 315+8
	f1 = 20+4
	v1 = 110+30
	
	t2 = 10+ 315+5
	f2 = 20+2+8
	v2 = 75+ 110+70
	
	
	t3 = 5 + 315+9
	f3 = 2 +20+4
	v3 = 50 + 130+25
	loop = 1
	counter =0
	counter1 = 1
	counter2 = 1
	counter3 = 1
	while True: 
		
		# # t = In
		timeIn=str(datetime.datetime.now()) #In.Format("2006-01-02T150405.999-0700") ##.String()
		
		if(loop==1):
			if(counter1==1):
				t1=t1+1
				f1=f1+1
				v1=v1+11
				counter1=2
			elif(counter1==2):
				t1=t1+3
				f1=f1+1
				v1=v1+20
				counter1=3
			elif(counter1==3):
				t1=t1+3
				f1=f1+1
				v1=v1+20
				counter1=4
			elif(counter1==4):
				t1=t1+2
				f1=f1+1
				v1=v1+10
				counter1=5
			elif(counter1==5):
				t1=t1+4
				f1=f1+1
				v1=v1+9
				counter1=6
			elif(counter1==6):
				t1=t1+1
				f1=f1+1
				v1=v1+11
				counter1=7
			elif(counter1==7):
				t1=t1+3
				f1=f1+1
				v1=v1+20
				counter1=8
			elif(counter1==8):
				t1=t1+3
				f1=f1+1
				v1=v1+20
				counter1=9
			elif(counter1==9):
				t1=t1+2
				f1=f1+1
				v1=v1+20
				counter1=10
			elif(counter1==10):
				t1=t1+10
				f1=f1+6
				v1=v1+40
				counter1=11
			elif(counter1==11):
				t1=t1+2
				f1=f1+1
				v1=v1+20
				counter1=12
			elif(counter1==12):
				t1=t1-2
				f1=f1-1
				v1=v1-20
				counter1=11
	
			
			machine_name = m1
			temp_val = str(t1)
			freq_val = str(f1)
			volt_val = str(v1)
			loop =2 
		elif(loop==2):
			if(counter2==1):
				t2=t2+1
				f2=f2+1
				v2=v2+11
				counter2=2
			elif(counter2==2):
				t2=t2+3
				f2=f2+1
				v2=v2+20
				counter2=3
			elif(counter2==3):
				t2=t2
				f2=f2
				v2=v2
				counter2=4
			elif(counter2==4):
				t2=t2-1
				f2=f2-1
				v2=v2-11
				counter2=5
			elif(counter2==5):
				t2=t2+2
				f2=f2+1
				v2=v2+10
				counter2=6
			elif(counter2==6):
				t2=t2-3
				f2=f2-1
				v2=v2-20
				counter2=7
			elif(counter2==7):
				t2=t2
				f2=f2
				v2=v2
				counter2=8
			elif(counter2==8):
				t2=t2-2
				f2=f2-1
				v2=v2-20
				counter2=9
			elif(counter2==9):
				t2=t2+3
				f2=f2+1
				v2=v2+20
				counter2=10
			elif(counter2==10):
				t2=t2-3
				f2=f2-1
				v2=v2-10
				counter2=11
			elif(counter2==11):
				t2=t2
				f2=f2
				v2=v2
				counter2=1
																																				
	
		
			machine_name = m2
			temp_val = str(t2)
			freq_val = str(f2)
			volt_val = str(v2)
			loop=3
		elif(loop==3):
		
			if(counter3==1):
				t3=t3+3
				f3=f3+2
				v3=v3+25
				counter3=2
			elif(counter3==2):
				t3=t3+2
				f3=f3+1
				v3=v3+15
				counter3=3
			elif(counter3==3):
				t3=t3
				f3=f3
				v3=v3
				counter3=4
			elif(counter3==4):
				t3=t3-2
				f3=f3-1
				v3=v3-15
				counter3=5
			elif(counter3==5):
				t3=t3-3
				f3=f3-2
				v3=v3-25
				counter3=1
				
			machine_name = m3
			temp_val = str(t3)
			freq_val = str(f3)
			volt_val = str(v3)
			loop=1
				
		data = [{"mname":machine_name,"temperature":temp_val,"frequency":freq_val,"voltage":volt_val,"timestamp":timeIn}]
		
		json = demjson.encode(data)
		print ("sending"+json)
		sbs.send_event(inputEventHubName,json)
		counter = counter +1
		sleep(2)
		print ("sent"+str(counter))
		
			
