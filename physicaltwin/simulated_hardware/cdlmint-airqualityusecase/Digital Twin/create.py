import test
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

test.create_schema()
test.create_instances()