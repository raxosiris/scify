#because python does not have REBL or any interactive development environment we have to log vars like a caveman
#give me live vars...
def skip_and_print(*args):
    """ Act like print(), but skip a line before printing. """
    print('\n' + str(args[0]), *args[1:])