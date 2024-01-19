import random

class RandomizedSet(object):

    def __init__(self):
        self.val_to_index = {}  # Dictionary to store {value: index} mapping
        self.values = []        # List to store the values

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # If the value is already in the set, return False
        if val in self.val_to_index:
            return False

        # Add the value to the list and update the dictionary
        self.values.append(val)
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        # If the value is not in the set, return False
        if val not in self.val_to_index:
            return False

        # Swap the value with the last element in the list
        last_val = self.values[-1]
        index_to_remove = self.val_to_index[val]

        # Update the list and dictionary
        self.values[index_to_remove] = last_val
        self.val_to_index[last_val] = index_to_remove

        # Remove the value from the dictionary and list
        del self.val_to_index[val]
        self.values.pop()

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        # Return a random element from the list
        return random.choice(self.values)
