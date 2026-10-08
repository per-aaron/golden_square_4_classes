class GrammarStats:
    def __init__(self):
        self.total_checks = 0
        self.checks_passed = 0

    def check(self, text):
        terminal_punct = ".!?"
        self.total_checks += 1
        if text[0].islower() or text[-1] not in terminal_punct:
            return False
        else:
            self.checks_passed += 1
            return True

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.total_checks == 0:
            raise Exception("No checks have been run!")
        return self.checks_passed * 100 / self.total_checks
