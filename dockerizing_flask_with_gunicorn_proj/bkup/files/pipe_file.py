#!/usr/local/bin/python -u
  
import sys
import os

docker_host = os.environ.get("SD_DOCKER_HOSTNAME","unknown")

from dc.core.nsq.logger import Logger

topic = sys.argv[1]

logger = Logger(topic)

BLOCK_SIZE = 1<<16
def fast_generator(file):
    rem = ''
    block = file.read(BLOCK_SIZE)
    while block:
        lines = block.split('\n')
        lines[0] = rem+lines[0]
        for i in range(0,len(lines)-1):
            yield lines[i]
        rem = lines[-1]
        block = file.read(BLOCK_SIZE)

for line in fast_generator(sys.stdin):
  logger.log(docker_host + "\t" + line.rstrip())
