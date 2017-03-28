from oslo_config import cfg
from oslo_log import log as logging
from sys import argv

LOG = logging.getLogger(__name__)
CONF = cfg.CONF
DOMAIN = "demo"

# register_options must be ahead of CONF.__init()
logging.register_options(CONF)


if __name__ =="__main__":
    CONF(args=argv[1:], default_config_files=['my.conf'])
    # setup() will setup logging from config file, which 
    # must follow CONF.__init()
    logging.setup(CONF, DOMAIN)

    LOG.debug("List of Oslo Logging config options and current values")
    LOG.debug("=" * 80)
    for c in CONF:
        LOG.info("%s = %s" % (c, CONF[c]))
    LOG.debug("=" * 80)

    LOG.info("Oslo Logging")
    LOG.warning("Oslo Logging")
    LOG.error("Oslo Logging")
