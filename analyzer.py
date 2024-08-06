import analyzerHelpers
import coingeckoCalls
import coingeckoHelper


def run():
    # welcome text
    analyzerHelpers.welcomeText()

    # customer input
    customerInput = analyzerHelpers.inputBuilder()

    # continuation until quit
    while customerInput != "q":
        # continuation text
        analyzerHelpers.continuationText()

        # customer input
        customerInput = analyzerHelpers.inputBuilder()
