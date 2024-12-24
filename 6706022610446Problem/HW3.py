import time
def numbers(N):
   total = N * (N + 1)//2
   even = N // 2 * ((N // 2) + 1)

   odd = total - even
   return odd,even

N = int(input('Enter the number: '))

start_time = time.time()
odd,even = numbers(N)
end_time = time.time()

print(f"Sum of even numbers: {even}")
print(f"Sum of odd numbers: {odd}")
print(f'Execution time: {(end_time - start_time) * 1000:.3f} ms')