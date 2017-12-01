import sys
import textwrap

commands_dict = {
    "commands": {

    }
}


def command(**kwargs):
    """Command decorator."""
    def wrapper(func):
        """Wrapper for the command decorator. It adds the command to the `commands_dict` dict."""
        name = kwargs.pop('name', func.__name__)
        args = kwargs.pop('args', 0)
        usage = kwargs.pop('usage', name)
        commands_dict['commands'][name] = {}
        commands_dict['commands'][name]['help'] = func.__doc__
        commands_dict['commands'][name]['function'] = func
        commands_dict['commands'][name]['args'] = args
        commands_dict['commands'][name]['usage'] = usage
    return wrapper


@command(name='help', args=1, usage='help <cmd=None>')
def _help(cmd=None):
    """Shows help for a command."""
    if cmd:
        try:
            help_doc = commands_dict['commands'][cmd]['help']
            usage = commands_dict['commands'][cmd]['usage']
            print(textwrap.dedent(f"""Command: {cmd}
            Information: {help_doc}
            Usage: {usage}"""))
        except Exception as e:
            print(e)
    else:
        print(f"""Commands:
        {', '.join(list(commands_dict['commands']))}""")


def exec_command():
    """Searches for commands called in stdin and attempts to execute it."""
    for line in sys.stdin:
        words = line.split()
        cmd = commands_dict["commands"][words[0]]
        func = cmd['function']
        args = cmd['args']
        arg_list = []
        count = 1
        for arg in range(args):
            try:
                arg_list.append(words[count])
                count += 1
            except IndexError:
                continue
        try:
            func = func(*arg_list)
        except TypeError as e:
            print(f'There was an error with that command.\n{e}')
        exec_command()
        return func
