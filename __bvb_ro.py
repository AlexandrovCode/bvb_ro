import time
import json
from bvb_ro import *

if __name__ == '__main__':
    start_time = time.time()

    a = Handler()
    final_data = a.Execute('aHR0cHM6Ly9tLmJ2Yi5yby9GaW5hbmNpYWxJbnN0cnVtZW50cy9EZXRhaWxzL0ZpbmFuY2lhbEluc3RydW1lbnRzRGV0YWlscy5hc3B4P3M9REJL', 'Financial_Information', '', '')
    print(json.dumps(final_data, indent=4))

    elapsed_time = time.time() - start_time
    print('\nTask completed - Elapsed time: ' + str(round(elapsed_time, 2)) + ' seconds')
