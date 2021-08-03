import re

TESTER = re.compile(
    r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$")

n = int(input())
creditCardNumbers = []
for _ in range(n):
    creditCardNumbers.append(input())

for creditCardNumber in creditCardNumbers:
    print("Valid" if TESTER.search(creditCardNumber) else "Invalid")