from stdin_cmd.commands import command, exec_command


@command(args=2, usage='add <arg1: Integer or Float> <arg2: Integer or Float>')
def add(arg1, arg2):
    """Adds two numbers together."""
    arg1 = float(arg1)
    arg2 = float(arg2)
    print(f"Your answer is {arg1 + arg2}.")


@command(args=2, usage='minus <arg1: Integer or Float> <arg2: Integer or Float>')
def minus(arg1, arg2):
    """Subtracts one number from another number."""
    arg1 = float(arg1)
    arg2 = float(arg2)
    print(f"Your answer is {arg1 - arg2}.")


@command(args=2, usage='multiply <arg1: Integer or Float> <arg2: Integer or Float>')
def multiply(arg1, arg2):
    """Multiplies two numbers by each other."""
    arg1 = float(arg1)
    arg2 = float(arg2)
    print(f"Your answer is {arg1 * arg2}.")


@command(args=2, usage='divide <arg1: Integer or Float> <arg2: Integer or Float>')
def divide(arg1, arg2):
    """Divides one number by another."""
    arg1 = float(arg1)
    arg2 = float(arg2)
    print(f"Your answer is {arg1 / arg2}.")


if __name__ == '__main__':
    exec_command()
