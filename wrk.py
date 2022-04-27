def closest_to_zero(a):
        """
          Please implement this method to
          return the number in the array that is closest to zero.
          If there are two equally close to zero elements like 2 and -2
          - consider the positive element to be "closer" to zero.
          
          
        :param a: list of numbers
        :returns: number

        closest_to_zero([2,-2,1, 3])
        1
        closest_to_zero([8,6,4,-4])
        4
        closest_to_zero ([7,8,-2,2,5])
        2
       """

        return abs(min(a, key=abs))
        



def count_chunks(array):
        """
         Please implement this method to return count of chunks in given array.
         Chunk is defined as continous sequence of one or more numbers separated 
         by one or more zeroes.
         Array can contain leading and trailing zeroes.
         Example: array [5, 4, 0, 0, -1, 0, 2, 0, 0] contains 3 chunks
        
        
        :param array: list of numbers
        :returns: number
        
        count_chunks([5, 4, 0, 0, -1, 0, 2, 0, 0]) 
        3
        count_chunks([3,4,6,0,0,0,0,-6,7,6,9,0,0,5,9,-7,0,0,5,3])
        4
        
        """

        previous_digit=0
        total=0
        for digit in array:
            if previous_digit == 0 and digit !=0:
                total += 1
            previous_digit=digit    
    
        return total
