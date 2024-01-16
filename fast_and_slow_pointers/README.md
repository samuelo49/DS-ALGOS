Fast and Slow Pointers Pattern
    - Use two pointers to traverse an iterable datastructure at different speeds.
    - The pointers usually traverse an iterable datastructure(array/list, linkedlist) 
        in either direction.
    - The slow pointer moves forward by one factor and the fast pointer moves by a factor
        or two in each step. Speed can be tailored according to the problem.
    - Two pointer approach is often used to identify patterns, cycles or specific properties
        within the data structure without directly examing the values of the elements.

Conditions to consider when to apply the Fast and slow pointer.
    - solving problems that requires detecting the presence of a cycle in a linked list.
    - solving the problem requires detecting the presence of a cycle in a sequence of symbols.
    - if the problem requires identifying:
        -  the nth last element in a linked list
        - the element at the k-way point in a linked list, for example middle element, or the element at the start of the second quartile.

Real-world problems that use the fast and slow pointers pattern.
    - Symlink(symbolic link) verification(a file that points to anther file)
        Symlinks can easily create loops or cycles where shortcuts point to each other.
        So we can apply the knowledge of fast and slow pointers to detect occurrences(cycles/loops)
        in a symlink by using the fast and slow pointers along the connected files or directories at
        different speeds.

    - Identify and remove cycles that come up as a result of cyclic dependencies during the compilation of an object-oriented program.
           