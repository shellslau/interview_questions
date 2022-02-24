
class Histogram:
    def __init__(self, lower, upper, buckets):
        self.lower = lower
        self.upper = upper
        self.buckets = buckets

        self.histogram = []
        for i in range(buckets):
            self.histogram.append(0)

    def find_bucket(self, number):
        if number < self.lower:
            return

        lowerBound = self.lower

        increment = (self.upper - self.lower) / self.buckets

        for i in range(self.buckets):
            if number < lowerBound + increment:
                return i
            lowerBound = lowerBound + increment

    def add_data_point(self,number):
        bucket = self.find_bucket(number)

        if bucket is None:
            return

        self.histogram[bucket] = self.histogram[bucket] + 1

    def bucket_value(self, bucket_index):
        return self.histogram[bucket_index]

    def find_max_count(self):
        max_val = self.histogram[0]
        for count in self.histogram:
            if max_val < count:
                max_val = count
        return max_val

    def display(self):
        return self.display_with_divisor(1)

    def display_with_divisor(self, divisor):
        displayString = ""
        lowerBound = self.lower

        increment = (self.upper - self.lower) / self.buckets

        for i in range(self.buckets):
            upperBound = lowerBound + increment
            count = int(self.histogram[i]/divisor) * "x"
            displayString = displayString + "[" + str(lowerBound) + "," + str(upperBound) + ")" + "  " + count + "\n"
            lowerBound = upperBound

        return displayString

    def display_scale(self, scale):
        divisor = self.find_max_count()/scale

        return self.display_with_divisor(divisor)



histogram = Histogram(0, 100, 5)
histogram.add_data_point(-1)
histogram.add_data_point(100)
histogram.add_data_point(10)
histogram.add_data_point(20)

for i in range(5):
    histogram.add_data_point(10)

for i in range(14):
    histogram.add_data_point(25)

for i in range(30):
    histogram.add_data_point(42)

for i in range(3):
    histogram.add_data_point(70)

for i in range(20):
    histogram.add_data_point(99)


print(histogram.bucket_value(0))

print(histogram.display_scale(100))
