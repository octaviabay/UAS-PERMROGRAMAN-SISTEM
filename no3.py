import psutil

def get_size(bytes,suffix="8"):
    factor = 1024
    for unit in ["", "K", "M", "G", "I", "P"]:
        if bytes < factor :
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

svmem = psutil.virtual_memory()
print(f"total : {get_size(svmem.total)}")
print(f"available : {get_size(svmem.available)}")
print(f"used : {get_size(svmem.used)}")
print(f"percentage : {get_size(svmem.percent)}%")

swap = psutil.swap_memory()
print("\nSwap partition : ")
print(f"total : {get_size(swap.total)}")
print(f"free : {get_size(swap.free)}")
print(f"used : {get_size(swap.used)}")
print(f"percentage : {get_size(swap.percent)}%")