# Outline of the class, functions are implemented as studs
class Box:
    # Constructs an empty bag.
    def __init__ (self):
        self.theItems = list()
    # Returns the number of items in the bag.
    def __len__(self):
        return len(self._theItems)
    # Adds a new item tj the bag.
    def add(self,item):
        self._theItems.append(item)
    # Removes the item from the bag.
    def remove(self,item):
        assert item in self._theItems # precondition
        idx = self.theItems.index(item)
        return self._theItems.pop(idx)
    # Determines if an item is contained in the bag.
    def __contains__(self,item):
        return item in self._theItems

    # Returns an iterator for traversing the list of items.
    def __iter__(self,item):
        return MyBoxIterator(self._theItems)
