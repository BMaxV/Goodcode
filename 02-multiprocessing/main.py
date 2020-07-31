import multiprocessing
import time


def the_function(number1, number2):
    return number1 + number2


def this_main():
    data_in = [(1, 1), (2, 2), (3, 3)]
    data_out = this_pool_stuff(data_in, the_function, 2)
    return data_out

# note: this function solves the problem of,
# "I have a huge amount of data, let me spread that around
# on my hardware so it gets done quicker."
# You don't have to use with, you can create the handles and
# use them elsewhere to see if the result is ready, this is useful
# for gui programs.
# the entire purpose in that case is that the gui can be updated,
# e.g. with a progress bar or a waiting indicator without all
# results being ready.


def this_pool_stuff(data_in, my_function, number_of_processes):

    data_out = []

    # "with" deals with leftovers if necessary
    with multiprocessing.Pool(processes=number_of_processes) as my_pool:
        active_stuff = []

        # do this as long as we have either more input or are waiting
        # for things to finish

        not_finished = len(active_stuff) > 0
        input_left = (len(data_in) > 0)

        while input_left or not_finished:

            processes_are_idle = len(active_stuff) < number_of_processes
            input_left = len(data_in) > 0

            while processes_are_idle and input_left:

                args = data_in.pop(0)  #input_left makes sure this exists
                kwargs = {}
                handle = my_pool.apply_async(my_function, args, kwargs)

                active_stuff.append(handle)

            for handle in active_stuff:
                if handle.ready():
                    break
            # sleep a bit to wait for any result, then repeat.
            time.sleep(1)

            # if you have a progress bar, this is where you move it.
            active_stuff.remove(handle)
            data_out.append(handle.get())

    return data_out


if __name__ == "__main__":
    r = this_main()
    print(r)
