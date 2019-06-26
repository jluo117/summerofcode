def removeZeroSums(head):
	myStk = []
	while (head is not None):
		stackTol = head.val
		popLoc = -1
		for i in range(len(myStk) - 1, -1):
			stackTol += myStk[i].val
			if stackTol == 0:
				popLoc = i
				break
		if popLoc is not -1:
			for _ in range(popLoc,len(myStk)):
				myStk.pop()
		else:
			myStk.append(head)
		head = head.next
	head = None
	myList = head
	for i in myStk:
		head = i
		head.next = None
		head = head.next
	return myList
