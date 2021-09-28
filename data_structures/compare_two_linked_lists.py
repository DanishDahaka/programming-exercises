def compare_lists(head1, head2):
    
    """Compares the elements of two linked lists and returns 1 if they have the same length and same elements, otherwise returns 0.

    Args:
    head1   (obj): head of the first linked list
    head2   (obj): head of the second linked list
    
    Returns:
    1 | 0   (int): 
    """
    
    equal = True
      
    while equal:
        
        # case we reach end of both lists
        if head1 == None and head2 == None:
            break
        
        # if list two happens to end before list one, potential issue for inverse case
        if head2 == None:
            return 0
        
        # continue if 
        elif head1.data == head2.data:
            pass

        # break as soon as the elements are different   
        else:
            equal = False
            break

        # get the following headers 
        head1 = head1.next
        head2 = head2.next

    # return conditions  
    if equal:
        return 1
    else:
        return 0