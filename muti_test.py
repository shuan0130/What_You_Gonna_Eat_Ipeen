import concurrent.futures


list_queue = []


def func(x):
    return x * x

list = [1,2,3,4,5]

with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:

    for num in list:
        list_queue.append(executor.submit(func,num))


    for future in concurrent.futures.as_completed(list_queue):
        future.result()
        print(future.result())


    # print(list_queue)