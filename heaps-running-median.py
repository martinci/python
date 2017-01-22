#!/bin/python3

import sys

# A min heap is a binary tree where each node's data is smaller than all
# the data in its subtree. Analogously, we have max heaps.
class MinHeap:
    size = 0
    # A heap can be implement as an array where a node with index i
    # has (left and right) children 2*i + 1 and 2*i + 2.
    def __init__(self):
        self.items = []
        
    # To insert an element we put at the end of the array and then
    # we make sure to restore the min heap property.
    def insert(self,data):
        self.items.append(data)
        self.size+=1
        self.bubble_up()
        
    # To remove the root of the min heap we replace it with the last
    # element that was inserted and then we restore the min heap property.
    def pop(self):
        if not self.items:
            raise EmptyHeap
        popped = self.items[0]
        temp = self.items.pop()
        self.items[0] = temp
        self.size-= 1
        self.bubble_down()
        return popped
        
    # To restore the min heap property after an insertion.    
    def bubble_up(self):
        idx = self.size - 1
        parent_idx = self.get_parent(self.size-1)
        while idx != 0 and self.items[idx] < self.items[parent_idx]:
            self.swap(idx,parent_idx)
            idx = parent_idx
            parent_idx = self.get_parent(idx)
            
    # To restore the min heap property after poping the root.
    def bubble_down(self):
        idx = 0
        # If size is 1, we already satisfy the min heap property.
        if self.size == 1: 
            return
        left_child = 1
        # As long as we have left children, we can go down the heap.
        while  left_child < self.size:
            left_data = self.items[left_child]
            # Check for right child.
            right_child = 2*idx + 2
            if right_child < self.size:
                right_data = self.items[right_child]
                # When we have both children, we compare and swap with
                # the smallest one if needed.
                if self.items[idx] <= min([left_data,right_data]):
                    break
                if left_data < right_data:
                    self.swap(idx, left_child)
                    idx = left_child
                else:
                    self.swap(idx, right_child)
                    idx = right_child
                # Update the left child
                left_child = 2*idx + 1
            else:
                # If there is no right child, we are at the end of the
                # heap and we only need to swap if needed and break.
                if self.items[idx] > left_data:
                    self.swap(idx, left_child)
                break
                
    def get_parent(self, idx):
        return (idx-1)//2
    
    def swap(self, i, j):
        temp = self.items[i]
        self.items[i] = self.items[j]
        self.items[j] = temp 


##################### MAX HEAP ###################
class MaxHeap:
    size = 0
    
    # A heap can be implement as an array where a node with index i
    # has (left and right) children 2*i + 1 and 2*i + 2.
    def __init__(self):
        self.items = []
        
    # To insert an element we put at the end of the array and then
    # we make sure to restore the max heap property.
    def insert(self, data):
        self.items.append(data)
        self.size+=1
        self.bubble_up()
        
    # To remove the root of the max heap we replace it with the last
    # element that was inserted and then we restore the max heap property.
    def pop(self):
        if not self.items:
            raise EmptyHeap
        popped = self.items[0]
        temp = self.items.pop()
        self.items[0] = temp
        self.size-= 1
        self.bubble_down()
        return popped
        
    # To restore the max heap property after an insertion.    
    def bubble_up(self):
        idx = self.size - 1
        parent_idx = self.get_parent(self.size-1)
        while idx !=0 and self.items[idx] > self.items[parent_idx]:
            self.swap(idx,parent_idx)
            idx = parent_idx
            parent_idx = self.get_parent(idx)
            
    # To restore the max heap property after poping the root.
    def bubble_down(self):
        idx = 0
        # If size is 1, we already satisfy the max heap property.
        if self.size == 1: 
            return
        left_child = 1
        # As long as we have left children, we can go down the heap.
        while  left_child < self.size:
            left_data = self.items[left_child]
            # Check for right child.
            right_child = 2*idx + 2
            if right_child < self.size:
                right_data = self.items[right_child]
                # When we have both children, we compare and swap with
                # the smallest one if needed.
                if self.items[idx] >= max([left_data,right_data]):
                    break
                if left_data > right_data:
                    self.swap(idx, left_child)
                    idx = left_child
                else:
                    self.swap(idx, right_child)
                    idx = right_child
                left_child = 2*idx + 1
            else:
                # If there is no right child, we are at the end of the
                # heap and we only need to swap if needed and break.
                if self.items[idx] < left_data:
                    self.swap(idx, left_child)
                break
                
    def get_parent(self, idx):
        return (idx-1)//2
    
    def swap(self, i, j):
        temp = self.items[i]
        self.items[i] = self.items[j]
        self.items[j] = temp 
        
        
# The goal is to keep track of a left MaxHeap and a right MinHeap such that
# at every time each contains the bottom and upper half of the data.
class RunMedian:
    def __init__(self):
        self.empty = True
        self.left = MaxHeap()
        self.right = MinHeap()
        
    def insert(self, data):
        if self.empty:
            self.left.insert(data)
            self.median = data
            self.empty = False
        else:
            if data >= self.median:
                self.right.insert(data)
            else:
                self.left.insert(data)
            self.recalibrate()
            
    def recalibrate(self):         
        # We balance the heaps depending on their sizes each hold.
        # Then we recompute the median
        l = self.left.size
        r = self.right.size
        if r - l > 1:
            temp = self.right.pop()
            self.left.insert(temp)
        elif l - r > 1:
            temp = self.left.pop()
            self.right.insert(temp)
        self.recompute_median()
            
    def recompute_median(self):
        l = self.left.size
        r = self.right.size
        if l == r:
            self.median = (self.left.items[0] + self.right.items[0])/2
        elif l < r:
            self.median = self.right.items[0]
        else:
            self.median = self.left.items[0]
            
            
if __name__ == '__main__':
    n = int(input().strip())
    runMedian = RunMedian()
    for _ in range(n):
        temp = int(input().strip())
        runMedian.insert(temp)
        print('{:.1f}'.format(runMedian.median))
        
