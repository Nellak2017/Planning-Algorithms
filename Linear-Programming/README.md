# Linear Programming

---

## Table of Contents

- [Linear Programming](#linear-programming)
  * [Overview](#overview)
    + [Usage of Programs in Repository Overview](#usage-of-programs-in-repository-overview)
    + [Linear Programming Overview](#linear-programming-overview)
    + [The general form of Objective Criterion in a Linear programming problem](#the-general-form-of-objective-criterion-in-a-linear-programming-problem)
    + [The general form of Constraints in a Linear programming problem](#the-general-form-of-constraints-in-a-linear-programming-problem)
    + [Terms](#terms)
  * [Linear Programming Problem Formulation](#linear-programming-problem-formulation)
    + [Computer Router Production Problem Example](#computer-router-production-problem-example)
      - [Computer Router Production Problem Example Statement](#computer-router-production-problem-example-statement)
      - [Computer Router Production Problem Example Formulation](#computer-router-production-problem-example-formulation)
        * [Objective Criterion](#objective-criterion)
        * [Constraints](#constraints)
          + [Materials Constraint](#materials-constraint)
          + [labor constraint](#labor-constraint)
    + [Space Agency Example](#space-agency-example)
      - [Space Agency Example Statement](#space-agency-example-statement)
      - [Space Agency Example Formulation](#space-agency-example-formulation)
        * [Objective Criterion](#objective-criterion-1)
        * [Constraints](#constraints-1)
          + [Available launches per Payload type](#available-launches-per-payload-type)
          + [Successful deployment quota](#successful-deployment-quota)
          + [Launch Prep time](#launch-prep-time)
    + [Minimizing Production and Inventory Example](#minimizing-production-and-inventory-example)
      - [Minimizing Production and Inventory Statement](#minimizing-production-and-inventory-statement)
      - [Minimizing Production and Inventory Formulation](#minimizing-production-and-inventory-formulation)
        * [Objective Criterion](#objective-criterion-2)
        * [Constraints](#constraints-2)
          + [Minimum Inventory](#minimum-inventory)
          + [Production capacities and minima](#production-capacities-and-minima)
  * [Solving Linear Programming Problems with the Simplex Method](#solving-linear-programming-problems-with-the-simplex-method)
    + [Simplex Method Overview](#simplex-method-overview)
      - [Example of Simplex Tableau](#example-of-simplex-tableau)
      - [Simplex Pseudo-Code](#simplex-pseudo-code)

## Overview

### Usage of Programs in Repository Overview

To use the software included in the repository, please be sure to have [Python 3](https://www.python.org/) installed on your Operating System, [Github CLI __(Gitbash)__ ](https://git-scm.com/downloads) installed, and enough memory to store the program on your local machine, then follow these steps to run the programs. 

1. On your local machine, navigate to an empty directory.
2. Inside the directory, right click and open a [__Gitbash__ ](https://git-scm.com/downloads) terminal here. 
3. With [__Gitbash__ ](https://git-scm.com/downloads) opened to the empty directory, run these command:
```bash
git init
git clone https://github.com/Nellak2017/Planning-Algorithms.git
```
4. Inside of the cloned github directory, or using the website interface, locate the desired [Planning Algorithm](https://github.com/Nellak2017/Planning-Algorithms) you want to use.
5. Once a desired [Planning Algorithm](https://github.com/Nellak2017/Planning-Algorithms) is chosen, navigate to your local copy of the file that contains the driver file for the Algorithm. 
6. Enter the desired input for the algorithm and press run. The results may appear in your terminal. 

### Linear Programming Overview

__Linear programming__ is a special class of mathematical programming models in which the __objective function__ and the __constraints__ can be expressed as _linear_ functions of the decision variables.

An __Objective Function__ represents some principal objective criterion or goal that measures the effectiveness of the system (such as maximizing profits or productivity).

__Constraints__ are practical limitations, such as lack of resources, time, or energy.

_Solving_ a linear programming problem means determining actual values of the decision variables that optimize the objective function, subject to the limitations imposed by the constraints.
  

### The general form of Objective Criterion in a Linear programming problem 


__z = c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + ... + c<sub>n</sub>x<sub>n</sub> = Σ c<sub>i</sub>x<sub>i</sub> | i=1 , i=n__
  

Where c<sub>i</sub> represents problem dependent constants.
  

### The general form of Constraints in a Linear programming problem
  
__a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> <= b__


### Terms

1. __Linear programming__ -  is a special class of mathematical programming models in which the __objective function__ and the __constraints__ can be expressed as _linear_ functions of the decision variables.
2. __Objective function__ - represents some principal objective criterion or goal that measures the effectiveness of the system (such as maximizing profits or productivity).
3. __Constraints__ - are practical limitations, such as lack of resources, time, or energy.
4. __Linear__ - any such equation of the form f(x) = Ax, where x may be a typical variable or a matrix of variables. 
5. __General Form of Linear Programming Objective Function__ - z = c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>2</sub> + ... + c<sub>n</sub>x<sub>n</sub> = Σ c<sub>i</sub>x<sub>i</sub> | i=1 , i=n
6. __General Form of  Linear Programming Constraint Functions__ - a<sub>1</sub>x<sub>1</sub> + a<sub>2</sub>x<sub>2</sub> + ... + a<sub>n</sub>x<sub>n</sub> <= b
7. __Feasible Space__ - The set of all points specified by , (x<sub>1</sub>,x<sub>2</sub>, ... , x<sub>n</sub>) , that satisfy the problem constraints.
8. __Optimal Feasible Solution__ - A point in __feasible space__ that is as effective as any other point in achieving the specified goal. 
9. __Extreme Points__ - A point in __feasible space__ that is at the edge of feasible space, at an intersection of 2 or more constraint lines. If there exists a Unique Optimal Solution, it lies on an Extreme Point. If there exists Multiple Unique Optimal Solutions, it exists on a Constraint Line.  
10. __Extreme Point Theorem__ - If a Unique Optimal Solution Exists for a Linear Programming Problem, then it lies on an Extreme Point in feasible space. 
11. __Possible Solutions to Linear Programming Problems__ - 1 Unique Solution, Multiple Unique Solutions, No Unique Solutions, or No Feasable Solutions.  
12. __Simplex Method__ - A method of finding solutions to a Linear Programming Problem by considering the objective function values at a subset of all the extreme points. 
13. __Standard Form of Linear Programming Problem__ - For a linear program with __n__ variables and __m__ constraints, 
__maximize z = cx__, 
__subject to Ax = b , x >= 0 , b >= 0__, 
where x is a column vector with all x<sub>i</sub> variables,
where A is a coefficient matrix with all a<sub>i</sub><sub>j</sub> coefficients,
where b is a requirement vector with all b<sub>i</sub> requirements; 
_Note: To minimize a function, multiply the objective function by -1 and maximize this._
_Note: No variable in standard form is allowed to be negative, convert all to positives somehow_
14. __Slack Variables__ - For inequalities, __<=__ , in Standard Form of Linear Programs, these variables are added into the standard form equation to convert it to an equality.
15. __Surplus Variables__ - For inequalites, __>=__, in Standard Form of Linear Programs, these variables are added into the standard form equation to convert it to an equality.
16. __Basic Solution__ - For a system of __m__ equations and __n__ unknowns, it is obtained by setting (n - m) of the variables to 0, and solving for the remaining __m__ variables. 
17. __Basic Variables__ - The __m__ variables that _are not_ set to 0 in a __Basic Solution__.
18.  __Non-Basic Variables__ - The __m__ variables that _are_ set to 0 in a __Basic Solution__.
19. __Number of Basic Solutions__ - Given by _n choose m_. Alternatively, _n! / (m!(n-m)!)_.
20. __Basic Feasible Solution__ - Basic solution that meets the non-negativity constraints. It corresponds to the _Extreme Points_ of the feasible region.
21. __Optimal Basic Feasible Solution__ - Basic solution that optimizes the objective function.  
22. __Adjacent Solution__ - 2 extreme points are adjacent if all but one of their _basic variables_ are the same. 
23. __Simplex Tableau__  - When performing the Simplex Algorithm, it is handy to have a Table to represent the values. 
  
--- 

## Linear Programming Problem Formulation

  
Not all problems are subject to Linear Programming, and as such it requires skill to figure out when and how to formulate a Linear Programming problem. Also sometimes, solving Linear Programming problems lead to non-integer solutions, when that is not allowed. Therefore, in those such cases, sophisticated methods are used to get the integer solutions. 

Provided below are a few examples of linear programming problems and their formulations.


### Computer Router Production Problem Example

#### Computer Router Production Problem Example Statement
  
A manufacturer of computer system components assembles two models of wireless routers,
model A and model B. The amounts of materials and labor required for each assembly,
and the total amounts available, are shown in the following table. The profits that
can be realized from the sale of each router are $22 and $28 for models A and B, respectively,
and we assume there is a market for as many routers as can be manufactured.

  

| |Resources Required per Unit| Resources Required per Unit | Resources Available | 
| --- | --- | --- | --- |
| | A | B | |
| Materials | 8 | 10 | 3400 |
| Labor | 2 | 3 | 960 |
| profit per sale | $22 | $28 | | 

The manufacturer would like to determine how many of each model to assemble in
order to maximize profits.


#### Computer Router Production Problem Example Formulation

##### Objective Criterion

Because the solution to this problem involves establishing the number of routers to be
assembled, we define the decision variables as follows:

Let x<sub>A</sub> = number of model A routers to be assembled

and

x<sub>B</sub> = number of model B routers to be assembled

In order to __Maximize profits__, we establish the __objective criterion__ as:

maximize z = $22x<sub>A</sub> + $28x<sub>B</sub>

To see why, see [[#The general form of Objective Criterion in a Linear programming problem]]. 

##### Constraints

###### Materials Constraint

8x<sub>A</sub> + 10x<sub>B</sub> <= 3400

###### labor constraint 

2x<sub>A</sub> + 3x<sub>B</sub> <= 960

To see why, see [[#The general form of Constraints in a Linear programming problem]].

Finally, all x<sub>i</sub> >= 0, because negative numbers of manufactured products is impossible.

### Space Agency Example

#### Space Agency Example Statement

A space agency planning team wishes to set up a schedule for launching satellites over a
period of three years. Experimental payloads are of two types (say, T1 and T2), and each
launch carries only one experiment. Externally negotiated agency policies dictate that at
most 88 of payload type T1 and 126 of type T2 can be supported. For each launch, type
T1 payloads will operate successfully with probability 0.85 and type T2 payloads with
probability 0.75. In order for the program to be viable, there must be a total of at least 60
successful deployments. The agency is paid $1.5 million for each successful T1 payload,
and $1.2 million for each successful T2 payload. The costs to the agency to prepare and
launch the two types of payloads are $1.05 million for each T1 and $0.7 million for each
T2. One week of time must be devoted to the preparation of each T2 launch payload and
two weeks are required for T1 launch payloads. The agency, while providing a public
service, wishes to maximize its expected net income from the satellite program.

| |Resources Required per Unit| Resources Required per Unit | Resources Available | 
| --- | --- | --- | --- |
| | T1 | T2 | |
| Price per launch | $1.05 million | $.7 million | _Agency Budget_ |
| Launches available | 88 | 126 | 214 |
| Prep Time | 2 weeks | 1 week | 156 weeks (3 years) |
| Expected Profit per launch | $1.5*.85 million | $1.2*.75 million | | 

#### Space Agency Example Formulation

Let x<sub>1</sub> = number of satellites launched carrying a type T1 payload, and x<sub>2</sub> = number of
satellites launched carrying a type T2 payload. Income is realized only when launches
are successful, but costs are incurred for all launches. 

__expected net income__  = (1.5)(.85)x<sub>1</sub> + (1.2)(.75)x<sub>2</sub> - (1.05)x<sub>1</sub> - (.7)x<sub>2</sub> million dollars

__expected net income__  = .225x<sub>1</sub> + .2x<sub>2</sub> million dollars

_Note:_ The expected net income is the __Expected profit per launch - the price per launch__

##### Objective Criterion

maximize z = .225x<sub>1</sub> + .2x<sub>2</sub> million dollars

##### Constraints

###### Available launches per Payload type
0 <= x<sub>1</sub> <= 88
0 <= x<sub>2</sub> <= 126

###### Successful deployment quota
.85x<sub>1</sub> + .75x<sub>2</sub> >= 60

###### Launch Prep time
2x<sub>1</sub> + 1x<sub>2</sub> <= 156

###  Minimizing Production and Inventory Example

#### Minimizing Production and Inventory Statement

A company wishes to minimize its combined costs of production and inventory over a
four-week time period. An item produced in a given week is available for consumption
during that week, or it may be kept in inventory for use in later weeks. Initial inventory
at the beginning of week 1 is 250 units. The minimum allowed inventory carried from
one week to the next is 50 units. Unit production cost is $15, and the cost of storing a unit
from one week to the next is $3. The following table shows production capacities and the
demands that must be met during each week.

| Period | Production Capacity | Demand  
| --- | --- | --- |
| 1 | 800 | 900 |
| 2 | 700 | 600 |
| 3 | 600 | 800 |
| 4 | 800 | 600 |

A minimum production of 500 items per week must be maintained. Inventory costs are
not applied to items remaining at the end of the fourth production period, nor is the
minimum inventory restriction applied after this final period.

#### Minimizing Production and Inventory Formulation

Let __x<sub>i</sub>__ be the number of units produced during the i-th week, for i = 1, …, 4. The formulation
is somewhat more manageable if we let __A<sub>i</sub>__ denote the number of items remaining
at the end of each week (accounting for those held over from previous weeks, those
produced during the current week, and those consumed during the current week). Note
that the __A<sub>i</sub>__ values are not decision variables, but merely serve to simplify our written
formulation. Thus,

A<sub>1</sub> = 250 + x<sub>1</sub> - 900
A<sub>2</sub> = A<sub>1</sub> + x<sub>2</sub> - 600
A<sub>3</sub> = A<sub>2</sub> + x<sub>3</sub> - 800
A<sub>4</sub> = A<sub>3</sub> + x<sub>4</sub> - 600

##### Objective Criterion

minimize z = $15(x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + x<sub>4</sub>) + $3(A<sub>1</sub> + A<sub>2</sub> + A<sub>3</sub>)

##### Constraints

###### Minimum Inventory

A<sub>i</sub> >= 50 for i = 1,2,3
A<sub>4</sub> >= 0

###### Production capacities and minima

500 <= x<sub>1</sub> <= 700
500 <= x<sub>2</sub> <= 700
500 <= x<sub>3</sub> <= 600

## Solving Linear Programming Problems with the Simplex Method

### Simplex Method Overview

The __Simplex method__ is an iterative algorithm that begins with an initial __feasible solution__,
repeatedly moves to a better solution, and stops when an __optimal solution__ has been
found and, therefore, no improvement can be made. From any __basic feasible solution__, we have the assurance that, if a better solution exists at all, then there is an __adjacent solution__ that is better than the current one. This is the principle on which the __Simplex method__ is based; thus, an __optimal solution__ is accessible from any starting __basic feasible solution__.

For help understanding terms in bold, see [[#Terms]]


#### Example of Simplex Tableau

Basis | z | x<sub>1</sub> | x<sub>2</sub> | s<sub>1</sub> | s<sub>2</sub> | s<sub>3</sub> | __Solution__
--- | --- | --- | --- | --- | --- | --- | --- | 
__Z__| 1 | -8  | -5  | 0  | 0 | 0 | 0 |
s<sub>1</sub>| 0 | 1 | 0 | 1 | 0 | 0 | 150 |
s<sub>2</sub>| 0 | 0 | 1 | 0 | 1 | 0 | 250 |
s<sub>3</sub>| 0 | 2 | 1 | 0 | 0 | 1 | 500 |

#### Simplex Pseudo-Code

1. Examine the elements in the top row (the objective function row). If all elements
are ≥0, then the current solution is optimal; stop. Otherwise go to Step 2.
2. Select as the non-basic variable to enter the basis that variable corresponding
to the most negative coefficient in the top row. This identifies the __pivot column.__
3. Examine the coefficients in the pivot column. If all elements are ≤0, then this problem
has an unbounded solution (no optimal solution); stop. Otherwise go to Step 4.
4. Calculate the ratios

θ<sub>i</sub> = b<sub>i</sub>/a<sub>ik</sub> for all i = 1, ... , m for which a<sub>ik</sub> > 0

where a<sub>ik</sub> is the i-th element in the pivot column k. Then select

θ =min { θ<sub>i</sub> }

5. To obtain the next tableau (which will represent the new basic feasible
solution), divide each element in the pivot row by the pivot element. Use this
row now to perform row operations on the other rows in order to obtain zeros
in the rest of the pivot column, including the z row. This constitutes a pivot
operation, performed on the pivot element, for the purpose of creating a unit
vector in the pivot column, with a coefficient of one for the variable chosen to
enter the basis.
