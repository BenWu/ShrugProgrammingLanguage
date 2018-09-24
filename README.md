# ShrugProgrammingLanguage [![Build Status](https://travis-ci.org/Ben-Wu/ShrugProgrammingLanguage.svg?branch=master)](https://travis-ci.org/Ben-Wu/ShrugProgrammingLanguage) [![Coverage Status](https://coveralls.io/repos/github/Ben-Wu/ShrugProgrammingLanguage/badge.svg)](https://coveralls.io/github/Ben-Wu/ShrugProgrammingLanguage)

##### WORK IN PROGRESS

Interpreter for the Shrug Programming Language

Shrug is a imperative, dynamically-typed, very very high-level, general-purpose programming language

## Usage

##### Requires Python 3.6+

#### Install

```sh
pip install shrug-lang
```

#### Start interpreter

```sh
shruglang
```

## Language spec

#### print

n

#### assignment

n 1


### math operators start with ¯\\\_(ツ)\_/¯

#### addition

¯\\\_(ツ)\_/¯ n 3

#### subtraction

¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ 3

#### multiplication

¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ 4

#### division

¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ 4

#### modulus

¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ 4

### comparators start with ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯

#### equality

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ n m

#### inequality

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ m

#### greater than

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ m

#### less than

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ n ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ m

### logical operators follow a comparator

#### AND

¯\\\_(ツ)\_/¯

#### OR

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯


### conditional statements start with ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ comparator 
	statement1
¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ comparator2
	statement2
¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ <- optional default statement
	statement2
¯\\\_(ツ)\_/¯ <- end conditional

### iteration starts with ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ n <- run statement n times
	statement
¯\\\_(ツ)\_/¯ <- end iteration

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ x arr <- for each x in arr
	statement
¯\\\_(ツ)\_/¯ <- end iteration

¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ cond <- run statement while cond is true
	statement
¯\\\_(ツ)\_/¯ <- end iteration

