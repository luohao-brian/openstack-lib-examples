#-*-coding:utf-8-*-
# test_olso_config.py
# Author: H. Luo
 
from oslo_config import cfg
from sys import argv

# 单个配置项模式
enabled_apis_opt = cfg.ListOpt(
        'enabled_apis',
        default=['ec2', 'osapi_compute'],
        help='List of APIs to enable by default.')

# 多个配置项组成一个模式
common_opts = [
        cfg.StrOpt('bind_host',
                   default='0.0.0.0',
                   help='IP address to listen on.'),
                
        cfg.IntOpt('bind_port',
                   default=9292,
                   help='Port number to listen on.')
]

# 配置组
rabbit_group = cfg.OptGroup(
    name='rabbit',
    title='RabbitMQ options'
)


# 配置组中的模式，通常以配置组的名称为前缀（非必须）
rabbit_ssl_opt = cfg.BoolOpt('use_ssl',
                             default=False,
                             help='use ssl for connection')

rabbit_opts = [
    cfg.StrOpt('host',
                  default='localhost',
                  help='IP/hostname to listen on.'),
    cfg.IntOpt('port',
                 default=5672,
                 help='Port number to listen on.')
]

CONF = cfg.CONF
CONF.register_opt(enabled_apis_opt)
CONF.register_cli_opt(enabled_apis_opt)
CONF.register_opts(common_opts)
CONF.register_cli_opts(common_opts)
CONF.register_group(rabbit_group)
CONF.register_opts(rabbit_opts, rabbit_group)
CONF.register_opt(rabbit_ssl_opt, rabbit_group)

if __name__ =="__main__":
    """
    :param args: command line arguments (defaults to sys.argv[1:])
    :param project: the toplevel project name, used to locate config files
    :param prog: the name of the program (defaults to sys.argv[0]
        basename, without extension .py)
    :param version: the program version (for --version)
    :param usage: a usage string (%prog will be expanded)
    :param description: A description of what the program does
    :param epilog: Text following the argument descriptions
    :param default_config_files: config files to use by default
    :param default_config_dirs: config dirs to use by default
    :param validate_default_values: whether to validate the default values
    :raises: SystemExit, ConfigFilesNotFoundError, ConfigFileParseError,
             ConfigFilesPermissionDeniedError,
             RequiredOptError, DuplicateOptError
    """
    CONF(args=argv[1:], default_config_files=['my.conf'])
     
    for i in CONF.enabled_apis:
        print ("DEFAULT.enabled_apis: " + i)
     
    print("DEFAULT.bind_host: " + CONF.bind_host)
    print ("DEFAULT.bind_port: " + str(CONF.bind_port))
    print("rabbit.use_ssl: "+ str(CONF.rabbit.use_ssl))
    print("rabbit.host: " + CONF.rabbit.host)
    print("rabbit.port: " + str(CONF.rabbit.port))
