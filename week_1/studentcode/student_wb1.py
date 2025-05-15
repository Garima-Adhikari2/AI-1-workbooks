from approvedimports import *

def exhaustive_search_4tumblers(puzzle: CombinationProblem) -> list:
    """simple brute-force search method that tries every combination until
    it finds the answer to a 4-digit combination lock puzzle.
    """

    # check that the lock has the expected number of digits
    assert puzzle.numdecisions == 4, "this code only works for 4 digits"

    # create an empty candidate solution
    my_attempt = CandidateSolution()
    
    # ====> insert your code below here
    '''
    for loop digit 1 range value set 
     for loop digit 2 range value set
      for loop digit 3  range value  set
       for loop digit 4 range value set
       list = [1,2,3,4]
       my_attempt.variable_values = list 
       result = puzzle.evaluate(my_attempt.variable_values)
       
        #  how long is the solution?
        N = len(attempt)
        if N is not self.numdecisions:
            raise ValueError( "Error:attempt is wrong length")

        # is the solution made up of valid choices?
        for pos in range(N):
            if attempt[pos] not in self.value_set:
                raise ValueError( "Error: invalid value found in solution")

        # have we found the right combination?
        if attempt == self.goal:
            return 1
        else:
            return 0
    ''' 
    for a in puzzle.value_set:
        for b in puzzle.value_set:
            for c in puzzle.value_set:
                for d in puzzle.value_set:
                    my_attempt.variable_values = [a,b,c,d]
                    try:
                        result = puzzle.evaluate(my_attempt.variable_values)
                        if result == 1:
                            return my_attempt.variable_values
                    except ValueError:
                        continue

           
    # <==== insert your code above here
    
    # should never get here
    return [-1, -1, -1, -1]

def get_names(namearray: np.ndarray) -> list:
    family_names = []
    # ====> insert your code below here
    '''
    split last names into array 
    turn last names from characters to string 
    append the strings into a list family_names after every join
    '''
    lastNameArray = namearray[:, -6:]
    for i in range(lastNameArray.shape[0]):
        string = ''.join(map(str,lastNameArray[i]))
        family_names.append(string)

    # <==== insert your code above here
    return family_names

def check_sudoku_array(attempt: np.ndarray) -> int:
    tests_passed = 0
    slices = []  # this will be a list of numpy arrays
    
    # ====> insert your code below here
    
    assert attempt.shape == (9, 9), "Sudoku grid must be 9x9"

    
    for i in range(9):
        slices.append(attempt[i, :])  

    for j in range(9):
        slices.append(attempt[:, j])  # Column j

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            slices.append(attempt[row:row+3, col:col+3].flatten())  

    # use assertions to check that the array has 2 dimensions each of size 9
    assert len(slices) == 27, "There should be 27 slices of the array"
    assert all(s.shape == (9,) for s in slices), "All slices should be 1D"# in 2 parts because this is a list   

    ## Remember all the examples of indexing above
    ## and use the append() method to add something to a list

    for slice in slices:  # easiest way to iterate over list
        pass
        # print(slice) - useful for debugging?
        print(slice)
        # get number of unique values in slice
        print (len(np.unique(slice)))
        # increment value of tests_passed as appropriate
        if len(np.unique(slice)) == 9:
            tests_passed += 1
    # <==== insert your code above here
    # return count of tests passed
    return tests_passed
