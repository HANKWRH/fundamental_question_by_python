a = int(input())
# This handles negative numbers automatically using two's complement in 8 bits
bin_string = format(a & 0xFF, '08b')
bin_list = [int(bit) for bit in bin_string]

print(*bin_list, end='', sep='')

