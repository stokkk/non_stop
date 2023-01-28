from abc import ABC, abstractmethod
import sys


class IObserver(ABC):
	@abstractmethod
	def update(data):
		pass


class IPublisher(ABC):
	@abstractmethod
	def addSub(self, sub):
		pass

	@abstractmethod
	def removeSub(self, sub):
		pass

	@abstractmethod
	def notifyAllSubs(self, update_data=""):
		pass


class Forbec(IPublisher):
	def __init__(self, subs=[]):
		self._subs = subs

	def addSub(self, sub):
		self._subs.append(sub)

	def removeSub(self, sub):
		self._subs.remove(sub)

	def notifyAllSubs(self, update_data=""):
		for sub in self._subs:
			sub.update(update_data)


class Observer(IObserver):

	def __init__(self,id):
		self._id = id

	def update(self, data):
		print(data + " [Observer " + str(self._id) + "]")

if __name__ == "__main__":
	obs = [Observer(o) for o in range(10)]
	f = Forbec(obs)
	f.notifyAllSubs('Forbec: we opening!')
