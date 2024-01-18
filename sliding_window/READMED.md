Sliding Window Pattern
    - Used to process sequential data by maintaing a moving subset of elements(window).
    - A window is a a sublist of formed over a part of an iterable data structure.
    - This pattern allows us to process data in segments instead of the entire list.
    - Can be viewed as a variation of the two pointers pattern with the pointers being used to set
        window bounds.
    - This approach can be efficient when we focus on the element leaving and entering the window.

    Crux of the Pattern 
        - Maintain a window of a given size(k) within a list of n elements for example.
        - do some computation work on the current window of size k and store the result in a variable
        - Move the window one step forward by subtracting the element that is no longer in the window &
            add the new element so we can still maintain a window of size k.
        - Each time we move forward, we perform atleast 4 operations, 0(4n) -> 0(n)

    When is the pattern applicable:
        - When the problem requires repeated computations on a contagious set of elements(subarray or substring), such that the window moves across the input
        array from one end to the other. 
        
    Real-world Applications
        - Telecommunications: Find the maximum number of users connected to a cellular network's base station in every k-millisecond sliding window.
        - Ecommerce: Given a dataset of product IDs in the order they were viewed by the user and a list of products that are likely similar, find how many times these products occurr together in the dataset.
        Video steaming: Given a stream of numbers representing the number of buffering
        events in a given user session, calculate the median number of buffering events in each one-minute interval.
        Social media content mining: Given the lists of topics that two users have posted about, find the shortest sequence of posts by one user that includes all the topics that the other user has posted about.