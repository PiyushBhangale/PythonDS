
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


## Bloom Filter
  - Toy Example in Python
  
  
        In order to illustrate how a Bloom filter works let’s consider a toy example. 
        We start with a bit vector; a vector whose elements are $0$ or $1$. To start, 
        we initialize the bit vector to all zeros. For the purposes of this toy example,
        we will restrict our attention to a bit vector of size $20$.

        bit_vector = [0] * 20
        print(bit_vector)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        The next ingredient we require is the use of a couple hash functions, that is,
        a function that maps data of arbitrary size to data of a fixed size.
        The types of hash functions used in Bloom filters are generally not of the “cryptographic 
        variety”, for example, one usually wouldn’t use something like MD5. Non-cryptographic 
        hash functions like Murmur and FNV are mostly used, primarily for their speed over 
        most cryptographic hash functions.

        There is a nice module in Python called pyhash that consists solely of non-cryptographic hashes.

        import pyhash
        Let’s combine the bit vector and non-cryptographic hash functions to put together a toy 
        example of a Bloom filter. In our example, let’s say we’re using our Bloom filter as a 
        Pokedex; a device to keep track of the Pokemon we have caught.Each time we catch a Pokemon,
        we update our Pokedex by running the name of the Pokemon through two hash functions.
        The output of the hashes indicates which bits to flip in our bit vector.

        Hashing the strings “Pikachu” and “Charmander” using the FNV hash algorithm mod 20 
        (since 20 is the size of our bit vector in this example) results in 13 and 5. Likewise, 
        hashing the same strings using the Murmur hashing algorithm mod 20 results in 10 and 9, respectively.

        Feeding the Pokemon strings into the hash functions.
        We use the outputs of the above hash algorithms to flip the bits located at the respective indices.
