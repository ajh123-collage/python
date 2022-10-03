a = 5
b = 3
c = 4

print(f"a={a}")
print(f"b={b}")
print(f"c={c}")

#% Modulo operater, returns remender of devision
m_sum = (a%b) + (a%c) + (b%a) + (b%c) + (c%a) + (c%b)

print("Maths operators")
print(f"  m_sum = (a%b) + (a%c) + (b%a) + (b%c) + (c%a) + (c%b) ={m_sum}")
print(f"  m_sum//a {m_sum//a}") #Integer devision, returns whole number part of devision.
print(f"  m_sum//v {m_sum//b}")
print(f"  m_sum//c {m_sum//c}")

print("Relational operators")
print(f"  a>b {a > b}")
print(f"  b>c {b > c}")
print(f"  c<=b {c <= b}")
print(f"  b==a {b == a}")
print(f"  c!=b {c != b}")

print("  String comparing")
fname = "sam"
lname = "h"
print(f"    fname={fname}")
print(f"    lname={lname}")
print(f"    fname != lname {fname != lname}")

print("Logical operators")
d = 6
print(f"  d={d}")
print(f"  d > 4 and d < 10 {d > 4 and d < 10}")
print(f"  a > c and a < b {a > c and a < b}")
print(f"  c > a and c > b {c > a and c > b}")
print(f"  a > b and a > c {a > b and a > c}")
print(f"  not b > c {not b > c}")