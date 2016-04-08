from mrjob.job import MRJob

INTERVAL_SIZE = 1000


# Calculates the value of Gregory-Leibniz series for a given interval
def partial_pi(interval):
    acc = 0.0
    for i in interval:
        ivalue = 4 * (-1.0)**i/(2*i + 1)
        acc += ivalue
    return acc


class MRPi(MRJob):

    def mapper(self, _, interval_number):
        range_start = INTERVAL_SIZE * int(float(interval_number))
        range_end = range_start + INTERVAL_SIZE
        interval = range(range_start, range_end)
        yield "pi", partial_pi(interval)

    def reducer(self, key, values):
        yield key, sum(values)

if __name__ == '__main__':
    MRPi.run()
