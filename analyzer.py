import os
import analyzerHelpers

import time


def run():
    # welcome text
    analyzerHelpers.welcomeText()

    time.sleep(12)

    # welcome choices
    analyzerHelpers.welcomeChoicesText()

    time.sleep(8)

    # customer input
    customerInput = analyzerHelpers.inputBuilder()

    # continuation until quit
    while customerInput != "q":
        # continuation text
        analyzerHelpers.continuationText()

        # customer input
        customerInput = analyzerHelpers.inputBuilder()
