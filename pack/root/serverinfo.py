import app

app.ServerName = None

LOGIN = ''
PASSWORD = ''
SERVER_IP = '77.111.154.20'
SERVER_ADI = 'Metin2 GF' 
PORT_AUTH = 11000
PORT_CH1 = 13000
PORT_CH2 = 13020
PORT_CH3 = 13040
PORT_CH4 = 13060
PORT_TEST = 13900
LOCALE = 'TAIWAN'

STATE_NONE = '...'
		
STATE_DICT = {
	0 : '....',
	1 : 'NORM',
	2 : 'BUSY',
	3 : 'FULL'	}

SERVER1_CHANNEL_DICT = {
	1:{'key':11,'name':'CH1   ','ip':SERVER_IP,'tcp_port':PORT_CH1,'udp_port':PORT_CH1,'state':STATE_NONE,},
	2:{'key':12,'name':'CH2   ','ip':SERVER_IP,'tcp_port':PORT_CH2,'udp_port':PORT_CH2,'state':STATE_NONE,},
	3:{'key':13,'name':'CH3   ','ip':SERVER_IP,'tcp_port':PORT_CH3,'udp_port':PORT_CH3,'state':STATE_NONE,},
	4:{'key':14,'name':'CH4   ','ip':SERVER_IP,'tcp_port':PORT_CH4,'udp_port':PORT_CH4,'state':STATE_NONE,},
}
REGION_NAME_DICT = {
	0 : LOCALE,
}

REGION_AUTH_SERVER_DICT = {
	0 : {
		1 : { 'ip':SERVER_IP, 'port':PORT_AUTH, }, 
		
		}	
}

REGION_DICT = {
	0 : {
		1 : { 'name' : SERVER_ADI, 'channel' : SERVER1_CHANNEL_DICT, },
		},
}

MARKADDR_DICT = {
	10 : { 'ip' : SERVER_IP, 'tcp_port' : PORT_CH1, 'mark' : '10.tga', 'symbol_path' : '10', },
	}

TESTADDR = { 'ip' : SERVER_IP, 'tcp_port' : PORT_TEST, 'udp_port' : PORT_TEST, }

#DONE