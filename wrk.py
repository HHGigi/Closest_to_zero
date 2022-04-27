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
