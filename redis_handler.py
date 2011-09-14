import logging
import redis

class RedisHandler(logging.Handler):
  def __init__(self, host='localhost'):
    logging.Handler.__init__(self)
    
    self.r_server = redis.Redis(host)
    self.formatter = logging.Formatter("%(asctime)s - %(message)s")
    
  def emit(self, record):
    self.r_server.rpush(record.name, self.format(record))