import re
import return_optimiser

def movement_and_date(line):
    m = re.match(r'\s*(\S+)\s*(\S+)', line)
    return (float(m.group(1)), m.group(2))

def ticks_from_file(file):
    return (movement_and_date(line) for line in file)

def find_optimal_return(in_filename, out_filename):
    with open(in_filename, 'r') as inf:
        start_date = inf.readline()
        best = return_optimiser.find_best_return(
            ticks_from_file(inf), start_date)

        profit = (best.roi-1.0) * 100.0
        with open(out_filename, 'w') as outf:
            outf.write('%s\n%s\n%.1f\n' %
                       (best.low_date, best.high_date, profit))

if __name__=='__main__':
    find_optimal_return('prices.txt', 'output.txt')
