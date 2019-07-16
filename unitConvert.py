class Node:
	def __init__(prev,cost):
		self.Prev = prev
		self.Cost = cost
		self.Next = None
class unitCovert:
	def addNewUnit(prevUnit,unitCost):
		createUnit = Node(prevUnit,unitCost)
		prevUnit.next = createUnit
	def convertUp(amount,prevUnit,targetUnit):
		while prevUnit is not targetUnit:
			amount = amount/ prevUnit.Next.Cost
			prevUnit = prevUnit.next
		return amount
	def convertDown(amount,prevUnit,targetUnit):
		while prevUnit is not targetUnit:
			amount = amount * prevUnit.Cost
			prevUnit = prevUnit.Prev
		return amount