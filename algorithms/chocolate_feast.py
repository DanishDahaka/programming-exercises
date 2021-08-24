def calc_number_chocs(money, cost, promotion) -> int:

    """ determines amount of chocolate bars to receive with money 
    given through promotion of turning in wrappers.


    args:
    money       (int): amount of money to spend
    cost        (int): cost per chocolate bar
    promotion   (int): number of wrappers to turn into a new chocholate bar
    """
    
    # initialize number of bars which are bought
    bars = money // cost

    # set amount of wrappers we receive from bars
    wrapper = bars

    # run as long as we still have wrappers
    while wrapper > 1:

        # new bars only evenly divide through the promotion
        new_bars = wrapper // promotion

        # exit condition when there is not more wrappers to be turned in
        if wrapper < promotion:
            break
        # amount of wrappers leftover
        wrapper = wrapper % promotion

        bars += new_bars

        wrapper += new_bars

    return bars


if __name__ == '__main__':

    print(calc_number_chocs(12,4,4))