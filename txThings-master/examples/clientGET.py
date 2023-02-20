"""
Created on 08-09-2012

@author: Maciej Wasilak
"""

import sys
from ipaddress import ip_address
sys.path.append(r"C:\Users\hp\Desktop\Co-ap\txThings-master")
from twisted.internet import reactor
from twisted.python import log

import txthings.coap as coap
import txthings.resource as resource

port = 0
def call(x):
    global port
    port+=x
class Agent:
    """
    Example class which performs single GET request to coap.me
    port 5683 (official IANA assigned CoAP port), URI "test".
    Request is sent 1 second after initialization.

    Remote IP address is hardcoded - no DNS lookup is preformed.

    Method requestResource constructs the request message to
    remote endpoint. Then it sends the message using protocol.request().
    A deferred 'd' is returned from this operation.

    Deferred 'd' is fired internally by protocol, when complete response is received.

    Method printResponse is added as a callback to the deferred 'd'. This
    method's main purpose is to act upon received response (here it's simple print).
    """

    def __init__(self, protocol):
        self.protocol = protocol
        reactor.callLater(1, self.requestResource)

    def requestResource(self):
        request = coap.Message(code=coap.GET)
        request.opt.uri_path = (b'counter',)
        request.opt.observe = 0
        # request.remote = (ip_address("169.254.71.19"), coap.COAP_PORT)
        request.remote = (ip_address("127.0.0.1"), coap.COAP_PORT)

        d = protocol.request(request, observeCallback=self.printLaterResponse)
        d.addCallback(self.printResponse)
        d.addErrback(self.noResponse)

    def printResponse(self, response):
        print('First result: ' + str(response.payload, 'utf-8'))
    def printLaterResponse(self, response):
        print('Observe result: ' + str(response.payload, 'utf-8'))

    def noResponse(self, failure):
        print('Failed to fetch resource:')
        print(failure)
        # reactor.stop()


log.startLogging(sys.stdout)

# print(sys.argv)
endpoint = resource.Endpoint(None)
protocol = coap.Coap(endpoint)
client = Agent(protocol)

# reactor.listenUDP(61616+int(sys.argv[1]), protocol)  # , interface="::")
# reactor.listenUDP(61616, protocol)  # , interface="::")
reactor.listenUDP(port,protocol) # , interface=":"
reactor.run()
