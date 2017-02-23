from st2common.runners.base_action import Action


class ActionWithOptionalArgs(Action):

    def run(self, arg1, arg2):
        if not arg2:
            arg2 = 'Not supplied'
        return (True, ('%s:%s' % (arg1, arg2)))
