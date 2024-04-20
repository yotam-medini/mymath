#!/usr/bin/env python
import itertools
import sys

def vlog(msg):
    sys.stdout.write(f"{msg}\n")
    
def cycle_down(cycle):
    return list(map(lambda i: i - 1, cycle))

def cycle_up(n, cycle):
    return list(map(lambda i: (i + 1) % n, cycle))

def cycles_down(cycles):
    return list(map(cycle_down, cycles))
    
def cycles_up(n, cycles):
    return list(map(lambda c: cycle_up(n, c), cycles))
    
def cycles_to_perm(n, cycles):
    # vlog(f"n={n}, cycles={cycles}")
    # cycles0 = list(map(lambda c: cycle_down(c), cycles))
    perm = list(range(n))
    for ci in range(len(cycles) - 1, -1, -1):
        # vlog(f"ci={ci}, perm={perm}")
        cycle = cycles[ci]
        # vlog(f"cycle={cycle}")
        sz = len(cycle)
        d = dict(map(lambda i: (cycle[i], cycle[(i + 1) % sz]), range(sz)))
        # vlog(f"d={d}")
        next_perm = perm
        for i in range(n):
            v = perm[i]
            next_perm[i] = d.get(v, v)
        perm = next_perm
        # vlog(f" ==> perm={perm}")
    return perm

def perm_to_cycles(perm):
    n = len(perm)
    cycles = []
    used = set()
    for i in range(n):
        if not i in used:
            i0 = i
            cycle = [(i0 + n - 1) % n]
            used.add(i0)
            while perm[i] != i0:
                i = perm[i]
                cycle.append((i + n - 1) % n)
                used.add(i)
            cycles.append(cycle)
    # cycles = list(map(lambda c: cycle_up(n, c), cycles))
    return cycles

    
def args_to_perm(args):
    n = int(args[0])
    vlog(f"args_to_perm: n={n}")
    cycles = []
    cycle = []
    for ai in range(1, len(args)):
        try:
            v = int(args[ai])
            cycle.append(v)
        except:
            cycles.append(cycle)
            # vlog(f"append: cycle={cycle}")
            cycle = []
    if len(cycle) > 0:
        cycles.append(cycle)
    vlog(f"cycles={cycles}")
    cycles = cycles_down(cycles)
    vlog(f"down: cycles={cycles}")
    perm = cycles_to_perm(n, cycles)
    return perm

def get_alternate_n(n):
    Sn = itertools.permutations(list(range(n)))
    An = []
    for p in Sn:
        even = True
        for i in range(n):
            for j in range(i + 1, n):
                if p[i] > p[j]:
                    even = not even
        if even:
            An.append(p)
    return An

def ex40():
    S4 = itertools.permutations([0, 1, 2, 3])
    A4 = get_alternate_n(4)
    vlog(f"#(A4)={len(A4)}")
    e = [0, 1, 2, 3]
    h = [1, 2, 0, 3]
    h2 = [2, 1, 0, 3]
    H = set([e, h, h2])
    cosets = [H]
    taus = [e]
    for i in range(len(A4)):
        p = A4[i]
        p_cycles = perm_to_cycles(p)
        coset = []
        for h in H:
            h_cycles = perm_to_cycles(h)
            cycles = p_cycles + h_cycles
            p_coset = cycles_to_perm(cycles)
    
if __name__ == "__main__":
    rc = 0
    # sys.stdout.write(f"perm: %s\n" % cycles_to_perm(4, [[1, 2, 3]]))
    perm = args_to_perm(sys.argv[1:])
    vlog(f"perm={perm}")
    cycles = perm_to_cycles(perm)
    vlog(f"cycles = {cycles}")
    cycles = cycles_up(len(perm), cycles)
    vlog(f"up: cycles = {cycles}")
    sys.exit(rc)


if __name__ == "__main__":
    rc = 0
    ex40()
    sys.exit(rc)
