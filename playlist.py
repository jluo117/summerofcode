def possible_playList(N,M,B):
	if M > N:
		result = 1
		for i in range(1, N + 1):
			result *= i
		return result
	if B > M:
		return 0
	result = 1
	stkLen = 0
	for _ in range(0,N):
		result *= M - stkLen
		stkLen += 1
		if stkLen > B:
			stkLen -= 1
	return result
