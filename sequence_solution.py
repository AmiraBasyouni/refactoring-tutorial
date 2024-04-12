# *****************************************************************************/
# *    Title: Refactoring Exercise
# *    Author: Josiah Wang and Robert Chatley
# *    Date: 2020/2021
# *    Availability: https://python.pages.doc.ic.ac.uk/2020/modules/lab-refactoring/exercise  
# ****************************************************************************/

class NumberSequence:
    def __init__(self, length=10):
        self.length = length
        self.index = 0

    def term(self, n):
        if n < 0:
            raise Exception("Not defined for indices < 0")
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < self.length:
            n = self.term(self.index)
            self.index += 1
            return n
        else:
            raise StopIteration
    

class FibonacciSequence(NumberSequence):
    def term(self, n):
        if n < 2:
            return 1

        return self.term(n - 1) + self.term(n - 2)

         

class TriangleNumberSequence(NumberSequence):
    def term(self, n):
        if n < 1:
            return 1

        return round(0.5 * (n + 1) * (n + 2))



def generate_sequence(FibonacciSequence):
    fib_seq = FibonacciSequence(10)    
    fib_seq_list = [i for i in fib_seq]
    return fib_seq_list

if __name__ == "__main__":
    fib_seq_list = generate_sequence(FibonacciSequence)
    print("Fibonacci: ", fib_seq_list)
    assert(fib_seq_list == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) 
       
    tri_seq_list = generate_sequence(TriangleNumberSequence)
    print("Triangle Numbers: ", tri_seq_list)
    assert(tri_seq_list == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]) 
