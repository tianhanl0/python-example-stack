from Stack import Stack

def test_empty():
	s = Stack()
	assert s.isEmpty()
	assert s.size() == 0

def test_it():
	'''
	Write a simple test.
	'''
	s = Stack()
	s.push(1)
	assert s.size() == 1
