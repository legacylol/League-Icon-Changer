from lcu_driver import Connector
import sys

try:
    code_icon = int(input('Enter the icon code:'))
except ValueError:
    print('Enter the icon code!')
    sys.exit()
    

connector = Connector()
async def icon(connection):
      request = await connection.request('put', '/lol-chat/v1/me/', data={"icon": code_icon})
      if request.status == 201:
          print('Icon updated!')
      else:
          print('Try again.')
    
      
      
@connector.ready
async def connect(connection):
    print("Connected")
    await icon(connection)
    
    
@connector.close
async def closed(_):
    print('Exit Program')
    

connector.start()