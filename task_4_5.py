import utils
import sys
args = sys.argv[1:]
for cod in args:
    out = utils.currency_rates(cod)
    print(out)

