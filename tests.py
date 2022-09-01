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
	assert s.size == 0
	s.push(1)
	assert s.size() ==1
	for i in range(1):
  		s.push(i)
	assert s.size() = 101
	raise NotImplementedError('Need to implement a simple test.')
