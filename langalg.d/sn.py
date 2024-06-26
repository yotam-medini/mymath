#!/usr/bin/env python
import itertools
import sys

def vlog(msg):
    sys.stdout.write(f"{msg}\n")
    
def cycle_down(cycle):
    return list(map(lambda i: i - 1, cycle))

def cycle_up(n, cycle):
    return list(map(lambda i: (i + 1) % n, cycle))

def cycle_plus1(cycle):
    return list(map(lambda i: i + 1, cycle))

def cycles_down(cycles):
    return list(map(cycle_down, cycles))
    
def cycles_up(n, cycles):
    return list(map(lambda c: cycle_up(n, c), cycles))
    
def cycles_plus1(cycles):
    return list(map(lambda c: cycle_plus1(c), cycles))
    
def cycles_to_perm(n, cycles):
    # vlog(f"n={n}, cycles={cycles}")
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
        if perm[i] != i and i not in used:
            i0 = i
            cycle = [i0]
            used.add(i0)
            while perm[i] != i0:
                i = perm[i]
                cycle.append(i)
                used.add(i)
            cycles.append(cycle)
    # vlog(f"perm={perm}, cycles={cycles}")
    return cycles

def perm_to_cycles_p1(perm):
    return cycles_plus1(perm_to_cycles(perm))
    
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
    h2 = [2, 0, 1, 3]
    H = [e, h, h2];
    vlog(f"H={H}")
    H.sort()
    vlog(f"sorted: H={H}")
    cosets = [H]
    taus = [e]
    for i in range(len(A4)):
        p = A4[i]
        p_cycles = perm_to_cycles(p)
        # vlog(f"p_cycles={p_cycles}")
        coset = []
        for h in H:
            h_cycles = perm_to_cycles(h)
            cycles = p_cycles + h_cycles
            # vlog(f"cycles={cycles}")
            p_coset = cycles_to_perm(4, cycles)
            coset.append(p_coset)
        coset.sort()
        if coset in cosets:
            vlog(f"p[i={i}] = {p}, pH already in cosets")
        else:
            vlog(f"adding: tau={p} coset={coset}")
            taus.append(p)
            cosets.append(coset)
    vlog(f"taus={taus}")
    # vlog(f"cosets={cosets}")
    for ci, coset in enumerate(cosets):
        vlog(f"coset[{ci}] permutations: ={coset}")
    for ci, coset in enumerate(cosets):
        cycles_s = list(map(perm_to_cycles, coset))
        cycles_s1 = list(map(cycles_plus1, cycles_s))
        # vlog(f"coset0[{ci}] = {cycles_s}")
        tau1 = cycles_plus1(perm_to_cycles(taus[ci]))
        stau1 = f"{tau1}"
        vlog(f"tau[{ci}]={stau1:11s}  coset[{ci}] = {cycles_s1}")
    for pi, p in enumerate(A4):
        # ps = f"{p}"; ps = f"{ps:11s}"
        p_cycles = perm_to_cycles(p)
        # vlog(f"pi={pi} p={p} p_cycles={p_cycles}")
        Hperm = []
        for hi in range(4):
            coset = cosets[hi]
            p_coset = []
            for perm in coset:
                pc_cycles = p_cycles + perm_to_cycles(perm)
                p_perm = cycles_to_perm(4, pc_cycles)
                p_coset.append(p_perm)
                # vlog(f"hi={hi} perm={perm} p_perm={p_perm}")
            p_coset.sort()
            nhi = None
            for k in range(4):
                if p_coset == cosets[k]:
                    if nhi is not None:
                        vlog("Error: dup\n"); sys.exit(1)
                    nhi = k
            if nhi is None:
                vlog("Error: not found\n"); sys.exit(1)
            Hperm.append(nhi + 1)
        p1 = list(map(lambda k: k + 1, p))
        vlog(f"{pi+1:2d} {p1}(Hs)={Hperm}")
        
    
if __name__ == "__main__Debug":
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
