import heapq
from collections import defaultdict



def huffman_code(frequencies):
    # Create a priority queue to store the nodes
    heap = [[weight, [symbol, ""]] for symbol, weight in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Extract the two nodes with the lowest frequencies
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)

        # Assign '0' and '1' as the prefix to the left and right subtrees
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]

        # Combine the two nodes and their frequencies
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    # Return the Huffman code as a dictionary
    huffman_code = dict(heapq.heappop(heap)[1:])
    return huffman_code


frequencies = {'a': 20*10**2, 'b': 15*10**2, 'c': 13*10**2, 
               'd': 40*10**2, 'e': 29*10**2, 'f': 6*10**2}

code = huffman_code(frequencies)
for symbol, huffman in code.items():
    print(f"Symbol: {symbol}, Huffman Code: {huffman}")


og_bits = sum(len(symbol) * weight for symbol, weight in frequencies.items())
compressed_bits = sum(len(huffman) * frequencies[symbol] for symbol, huffman in code.items())

compression_ratio = compressed_bits / og_bits

print(f"Compression Ratio: {compression_ratio}")
