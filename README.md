# Demo of Genetic Algorithm

Implement a simple genetic algorithm (GA) to evolve a string that matches a given target string. 
```
TARGET_STRING = "Everything Apple announced today: Apple Watch 8 and SE, Apple One, new iPad Air.

The Apple Store went down this morning, heralding another Apple launch day. At the company's virtual event, Tim Cook started out by telling us that the Apple Watch and new additions to the iPad family of tablets would be the highlights -- and we got an Apple Watch Series 8, Apple Watch SE, a redesigned iPad Air debuting the A14 Bionic chip and a new eighth-gen iPad."
```

The target string is everything within the "" quotations, and the goal is to evolve a string that matches the target string exactly (every character, even the invisible newline one).

## High level algorithm

- Define what the chromosome (candidate solution) would be. 
- Create a population of random chromosomes
- Evaluate chromosomes
- Check if we get the solution
- Select chromosomes
- Perform crossover and mutation over selected chromosomes
- Repeat

At the end, the program will output

- `done:`, follows by
- the number of chromesomes evaluated
- the number of generation
- the best fit string
- the fitness score of the best string
- the total runtime in seconds

Also, the program will output at every X generations some statistic such as generation number, average fitness score, and the best fitness score and individual

```
$ ./ga.exe
generation 0, average fit X, best fit Y
'your best chromosome at this generation 0'
generation 50, average fit X, best fit Y 
'your best chromosome at this generation 50'
generation 100, average fit X, best fit Y 
'your best chromosome at this generation 100'
generation 150, average fit X, best fit Y
'your best chromosome at this generation 150'
....
done: X evaluated chromosomes, Y generations, best fit 0 (perfect sol)
"Everything Apple announced today: Apple Watch 6 and SE, Apple One, new iPad Air.

The Apple Store went down this morning, heralding another Apple launch day. At the company's virtual event, Tim Cook started out by telling us that the Apple Watch and new additions to the iPad family of tablets would be the highlights -- and we got an Apple Watch Series 6, Apple Watch SE, a redesigned iPad Air debuting the A14 Bionic chip and a new eighth-gen iPad."
```

## How to run
```
$ gcc ga.c -o ga.exe
$ ./ga.exe
....
```
