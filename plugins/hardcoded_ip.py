"""
ddupdate plugin providing an ip address to use a from an interface option.

See: ddupdate(8)
"""

import sys

from ddupdate.ddplugin import IpPlugin, IpAddr, dict_of_opts


class HardcodedIfPlugin(IpPlugin):
    """
    Use address given in configuration options.

    Options:
        ip = ipv4 address
        ip6 = ipv6 address
    """

    _name = 'hardcoded-ip'
    _oneliner = 'Get address from configuration options'

    def get_ip(self, log, options):
        """Implement IpPlugin.get_ip()."""
        addr = IpAddr()
        opts = dict_of_opts(options)
        if 'ip' not in opts and 'ip6' not in opts:
            log.error("Required option ip= or ip6= missing, giving up.")
            sys.exit(2)
        if 'ip' in opts:
            addr.v4 = opts['ip']
        if 'ip6' in opts:
            addr.v6 = opts['ip6']
        return addr
