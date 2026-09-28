# def scan_taget():
#     print("Scanning target......")
#     time.sleep(2)

# import time
# start=time.perf_counter()
# print(start)
# scan_taget()
# end=time.perf_counter()
# print(end)
# print(f"Scan completed in {end-start:.2f} seconds.")


import time


def timer(function):
    def wrapper():
        start=time.perf_counter()
        function()
        end=time.perf_counter()
        print("Execution time:", end -start)
    return wrapper





@timer
def scan_target():
    print("Scanning target......")
    time.sleep(2)

scan_target()


