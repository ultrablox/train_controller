import logging


class Runnable:
  def onMessageReceived(self, msg):
    pass

  def isFinished(self):
    return True

  def description(self):
    return 'Unnamed Runnable'

class ThreadRunner:
  def __init__(self):
    self.__runnables = []

  def add(self, runnable):
    assert runnable not in self.__runnables, 'Runnable {} already in threadRunner'.format(runnable.description())
    logging.info('Adding to threadRunner {}...'.format(runnable.description()))
    self.__runnables += [runnable]

  def run(self):
    while True:
      runnableCount = len(self.__runnables)
      # logging.info('Iterating {} runnables'.format(runnableCount))
      i = 0
      while i < runnableCount:
        runnable = self.__runnables[i]
        runnable.doWork()
        if runnable.isFinished():
          logging.info('Runnable "{}" is finished'.format(runnable.description()))
          self.__runnables.remove(runnable)
          runnableCount = runnableCount - 1
        else:
          i = i + 1

  def onMessageReceived(self, msg):
    for runnable in self.__runnables:
      runnable.onMessageReceived(msg)

