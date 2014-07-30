# ss warnings.py

class Warning:
    """ abstract """

    def issue(self):
        pass

class ExceptionViolatedWarning:

    def issue(self):
        return "exception was violated!!"


class WorkloadCeilingWarning:

    def issue(self):
        return "too much work!!"