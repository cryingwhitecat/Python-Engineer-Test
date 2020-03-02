def linear_fib(n):
  fn = f1 = f2 = 1
  for x in range(2, n-1):
    fn = f1 + f2
    f2, f1 = f1, fn
  return fn

if __name__ == "__main__":
    nthfib = linear_fib(6)
    print(nthfib)