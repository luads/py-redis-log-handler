import logging
import redis_handler

if __name__ == '__main__':

  logger = logging.getLogger('my_app')
  logger.setLevel(logging.DEBUG)
  logger.addHandler(redis_handler.RedisHandler())
  
  logger.info('Testing my redis logger')