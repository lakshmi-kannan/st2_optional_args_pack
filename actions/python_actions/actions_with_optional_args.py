from st2common.runners.base_action import Action


class ActionWithOptionalArgs(Action):

    def run(self, arg1, arg2='default'):
        return (True, ('%s:%s' % (arg1, arg2))
