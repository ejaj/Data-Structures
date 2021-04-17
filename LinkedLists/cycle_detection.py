def has_cycle(head):
    first_step =second_step = head

    while second_step != None and second_step.next != None:
        first_step = first_step.next
        second_step = second_step.next.next
        if first_step == second_step:
            return True
    return False


