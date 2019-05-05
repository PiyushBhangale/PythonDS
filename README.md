
The repository consists of various DS implementations with its uses in python.
## Stacks
  - Basic Stack
      
      
      The following methods have been implemented in the stack code:
      
      1. push :_Push element to top of stack_
      2. pop: _Remove element from the top of the stack_
      3. peek : _Return the topmost element_
      4. is_empty : _To check if stack is empty_
      5. get_stack : _Get the entire stack_
      
   - Balanced Parenthesis using Stack
      
      Use a stack to check whether or not a string has balanced usage of parenthesis.
      
          Example:
                (), ()(), (({[]}))  <- Balanced.
                ((), {{{)}], [][]]] <- Not Balanced.
          
          Balanced Example: {[]}
          Non-Balanced Example: (()
          Non-Balanced Example: ))
    
   - Int to binary using Stack
    
      Use a stack data structure to convert integer values to their corresponding binary representation. 
          
          Example : 242
          242 / 2 = 121 -> 0
          121 / 2 = 60  -> 1
          60 / 2  = 30  -> 0
          30 / 2  = 15  -> 0
          15 / 2  = 7   -> 1
          7 / 2 = 3     -> 1
          3 / 2 = 1     -> 1
          1 / 2 = 0	  -> 1
