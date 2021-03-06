from utilities.result import Status


class Steps:
    """
    Class manage list of step.
    """

    def __init__(self):
        self.__steps = []

    def get_last_step(self):
        """
        :return the last item of step.
        """
        if len(self.__steps) != 0:
            return self.__steps[-1]
        else:
            return None

    def get_list_step(self):
        """
        :return the list of step.
        """
        return self.__steps

    def add_step(self, name):
        """
        Add a new step to list step.
        :param name: variable hold the step name. Using to report.
        """
        from utilities import utils
        step_id = len(self.__steps)
        utils.print_header("\n{0}. {1}\n".format(step_id + 1, name))
        new_step = Step(step_id + 1, name)
        self.__steps.append(new_step)


class Step:
    """
    Class manage information of a test step.
    """

    def __init__(self, step_id, name, status=Status.FAILED, message=""):
        self.__id = step_id
        self.__name = name
        self.__status = status
        self.__message = message
        self.__freeze = False

    def get_id(self):
        """
        :return: step's id.
        """
        return self.__id

    def get_name(self):
        """
        :return: step's name.
        """
        return self.__name

    def get_status(self):
        """
        :return: step's status.
        """
        return self.__status

    def get_message(self):
        """
        :return: return step's message.
        """
        return self.__message

    def set_status(self, status, message=""):
        if not self.__freeze:
            self.__status = status
            if status == Status.FAILED:
                if message != "":
                    self.set_message(message)
                self.__freeze = True

    def set_message(self, message):
        self.__message = message
