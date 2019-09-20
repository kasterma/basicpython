# multithreaded FizzBuzz

Two issues arose in solving this

1. how to read the problem to understand what gets called how,
2. everything inside the lock b/c otherwise still could get some extra outputs before all breaks executed (releasing
  the lock seemed to lead to extra swapping giving rise to multiple extra outputs when the break was outside the
  lock and last)

Solution off course is silly b/c everything is in the one lock.
