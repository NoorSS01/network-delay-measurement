from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected!")

def _handle_PacketIn(event):
    packet = event.parsed
    log.info("Packet received: %s -> %s", packet.src, packet.dst)

    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)