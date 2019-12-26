from pymodbus.client.sync import ModbusTcpClient as ModbusClient

pi = ModbusClient('192.168.43.162',502)

message = raw_input("Enter message to encode: ")

   if ch=='A':
    pi.read_coils(0,2).bits
   elif ch=='B':
    pi.read_coils(0,3).bits
   elif ch=='C':
    pi.read_coils(0,4).bits
   elif ch=='D':
    pi.read_coils(0,5).bits
   elif ch=='E':
    pi.read_coils(0,6).bits
   elif ch=='F':
    pi.read_coils(0,7).bits
   elif ch=='G':
    pi.read_coils(0,8).bits
   elif ch=='H':
    pi.read_coils(0,9).bits
   elif ch=='I':
    pi.read_coils(1,2).bits
   elif ch=='J':
    pi.read_coils(1,3).bits
   elif ch=='K':
    pi.read_coils(1,4).bits
   elif ch=='L':
    pi.read_coils(1,5).bits
   elif ch=='M':
    pi.read_coils(1,6).bits
   elif ch=='N':
    pi.read_coils(1,7).bits
   elif ch=='O':
    pi.read_coils(1,8).bits
   elif ch=='P':
    pi.read_coils(2,2).bits
   elif ch=='Q':
    pi.read_coils(2,3).bits
   elif ch=='R':
    pi.read_coils(2,4).bits
   elif ch=='S':
    pi.read_coils(2,5).bits
   elif ch=='T':
    pi.read_coils(2,6).bits
   elif ch=='U':
    pi.read_coils(2,7).bits
   elif ch=='V':
    pi.read_coils(3,2).bits
   elif ch=='W':
    pi.read_coils(3,3).bits
   elif ch=='X':
    pi.read_coils(3,4).bits
   elif ch=='Y':
    pi.read_coils(3,5).bits
   elif ch=='Z':
    pi.read_coils(3,6).bits
   elif ch=='0':
    pi.read_coils(4,2).bits
   elif ch=='1':
    pi.read_coils(4,3).bits
   elif ch=='2':
    pi.read_coils(4,4).bits
   elif ch=='3':
    pi.read_coils(4,5).bits
   elif ch=='4':
    pi.read_coils(5,2).bits
   elif ch=='5':
    pi.read_coils(5,3).bits
   elif ch=='6':
    pi.read_coils(5,4).bits
   elif ch=='7':
    pi.read_coils(6,2).bits
   elif ch=='8':
    pi.read_coils(6,3).bits
   elif ch=='9':
    pi.read_coils(7,2).bits
   elif ch==' ':
    pi.read_coils(1,9).bits
   elif ch=='.':
    pi.read_coils(2,8).bits
   elif ch=='"':
    pi.read_coils(3,7).bits
	
