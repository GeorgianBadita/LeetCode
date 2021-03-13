import math


class MRUQueue:

    def __init__(self, n: int):
        self.__bucket_size = math.sqrt(n)
        self.__num_buckets = math.ceil(n/self.__bucket_size)
        self.nums = self.__create_buckets(
            n, self.__num_buckets, self.__bucket_size)

    def fetch(self, k: int) -> int:
        bucket = int((k - 1) / self.__bucket_size)
        idx_in_bucket = (k - 1) % self.__bucket_size

        elem = self.nums[bucket][idx_in_bucket]

        for i in range(idx_in_bucket, len(self.nums[bucket]) - 1):
            self.nums[bucket][i] = self.nums[bucket][i + 1]

        self.nums[bucket].pop()

        bucket_count = len(self.nums)
        for i in range(bucket + 1, bucket_count):
            self.nums[i - 1].append(self.nums[i][0])
            self.nums[i].pop(0)

        self.nums[bucket_count - 1].append(elem)
        return elem

    def __create_buckets(self, elems, num_buckets, bucket_size):
        buckets = [[] for _ in range(num_buckets)]
        for i in range(elems):
            bucket = int(i / bucket_size)
            buckets[bucket].append(i + 1)
        return buckets


queue = MRUQueue(5)

print(queue.nums)
