import time

def getTimestamp():
	timestamp = str(time.time()).replace('.', '') + '0'
        if len(timestamp) == 12:
                timestamp = timestamp + '0'
	return timestamp
