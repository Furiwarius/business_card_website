import logging
import logging.config


log_setting = 'app/setting/log.conf'

logging.config.fileConfig(fname=log_setting)

log = logging.getLogger('root')
