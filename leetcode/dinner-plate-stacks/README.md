# Notes on Dinner Plate Stacks

- 1172. Dinner Plate Stacks, https://leetcode.com/problems/dinner-plate-stacks/

Plain solution first to mind was record capacity, and keep a list of lists for the stacks.  Search for the insertion
point.  Remove a stack that is empty, making the pop point the the last list in the list of lists.  Added a `__repr__`
to use in tests (where I asserted the state of the solution by checking state of the `repr`)

In initial optimization steps (since the solution was too slow) I had forgotten about the search for insertion point,
and was worried that the memory allocation and reallocation for the list of lists was the problem.

When this didn't work came back to optimizing the search for insertion point, tried I heap but since I didn't observe
a key invariant (that I still can't formulate well; but essentially when popping a lot there are possible insertion
points on the heap that are past where there still are stacks, emptying the heap when you first have to create a new
stack for the insertion point provided by the heap solves this).

That same (or similar) invariant should be able to work when you just keep the list sorted using the bisect module (I
came to heaps through the bisect module; in the docs it is the module just before).

But the solution that is simpler and fast enough is to just keep track of the current insertion point, shrink it when
you popAtStack for a smaller stack, and search upward when that stack is full.

# Notes

1. setting up an invariant that checks things that should be true, that can be slow but easily turned off, helps
   greatly with debugging.
2. I didn't have a timing solution available, hence started working on optimizing the wrong thing.  Generate long
   runs and profile

# TODOs

1. be able to generate long runs and profile them.
    --> profiling is function level; would not have (directly) indicated that the problem was with the search
2. better test runner for inputs as provided in the problem.
    --> since other problems don't use same scheme, skip on this
3. come up with the right invariant that makes it obvious the heap solution works.
    --> if exists i in H i > len(stacks), then len(stacks) in H
    --> after working with that invariant, noticed can simplify the code a bit more by no longer using it
4. in browsing other peoples solution, using a set in place of a heap also made it fast enough.  Learn the timing
   properties of sets as well.
    --> separate project
5. testing if index would work before inserting, versus trying it and catching the error.  What is the speed difference?
    --> difference seems minimal
