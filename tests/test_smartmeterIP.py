import logging

from datetime import datetime

from meter import SmartMeterIP



log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,filename='test.log',format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

meter = SmartMeterIP("192.168.1.1",3001)

packet = meter.read_one_packet()
meter.disconnect()

print(packet)

data = [
    ('Time', datetime.now()),
    ('Total kWh High consumed', packet['kwh']['high']['consumed']),
    ('Total kWh Low consumed', packet['kwh']['low']['consumed']),
    ('Total gas consumed', packet['gas']['total']),
    ('Current kWh tariff', packet['kwh']['tariff'])
]

print('\n'.join(['%-25s %s' % (k,d) for k,d in data]))
