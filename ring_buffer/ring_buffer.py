from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

	def append(self, item):
		if self.storage.length < self.capacity:
			self.storage.add_to_tail(item)
			self.current = self.storage.head
		else:

			if self.current.next == None:
				self.current.value = item
				self.current = self.storage.head

			else:
				self.current.value = item
				self.current = self.current.next

	def get(self):
		list_buffer_contents = []
		start_value = self.storage.head.value
		current = self.storage.head
		while current is not None:
			list_buffer_contents.append(current.value)
			current = current.next
		return list_buffer_contents
