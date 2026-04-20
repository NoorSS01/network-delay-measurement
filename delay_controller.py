#importing these libraries to control the switch
from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger() #used to display in terminal

#triggers when the Swtich is connected to Controller
def _handle_ConnectionUp(event):
    log.info("Switch connected!")

#This is core logic where it handles a situation when the switch does not know what to do with packets
def _handle_PacketIn(event):
    #getting packet info
    packet = event.parsed 
    log.info("Packet received: %s -> %s", packet.src, packet.dst)#prints the packet info in terminal

    #stores the flow rules in the switch
    msg = of.ofp_packet_out() 
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

#To Launch
def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)