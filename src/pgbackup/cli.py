from argparse import Action, ArgumentParser

known_drivers = ['local', 's3']

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver,destination = values
        if driver.lower() not in known_drivers:
            parser.error("Unknown driver")
        namespace.driver = driver.lower()
        namespace.destination = destination.lower()

def create_parser():
    parser = ArgumentParser()
    parser.add_argument('url', help="url of postgresql")
    parser.add_argument('--driver',
            help="how & where to store backup",
            nargs=2,
            action=DriverAction,
            required=True)
    return parser
