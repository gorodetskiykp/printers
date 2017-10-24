from pysnmp.hlapi import *

community_string = 'public'

port_snmp = 161

OID_sysNames = [
    '1.3.6.1.2.1.43.5.1.1.17.1',    # sn
    '1.3.6.1.2.1.25.3.2.1.3.1',     # name
]


def get_snmp_value(printer_name, oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(community_string, mpModel=0),
               UdpTransportTarget((printer_name, port_snmp)),
               ContextData(),
               ObjectType(ObjectIdentity(oid)))
    )
    return(varBinds)

# if errorIndication:
#     print(errorIndication)
# elif errorStatus:
#     print('%s at %s' % (errorStatus.prettyPrint(),
#                         errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
# else:
#     for varBind in varBinds:
#         print(' = '.join([x.prettyPrint() for x in varBind]))

for printer_name in printers:
    # for oid in OID_sysNames:
    with open('oids.txt', 'r') as f:
        for oid in f:
            # print(oid)
            print(get_snmp_value(printer_name, oid))

