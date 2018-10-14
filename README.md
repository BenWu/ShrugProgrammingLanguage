# ShrugProgrammingLanguage [![Build Status](https://travis-ci.org/Ben-Wu/ShrugProgrammingLanguage.svg?branch=master)](https://travis-ci.org/Ben-Wu/ShrugProgrammingLanguage) [![Coverage Status](https://coveralls.io/repos/github/Ben-Wu/ShrugProgrammingLanguage/badge.svg)](https://coveralls.io/github/Ben-Wu/ShrugProgrammingLanguage)

##### WORK IN PROGRESS

Interpreter for the Shrug Programming Language

Shrug is a imperative, dynamically-typed, very very high-level, general-purpose programming language

## Example

```sh
>> a 10
>> b 11
>>
>> # Arithmetic operations
>> ¯\_(ツ)_/¯ a 3
13
>> ¯\_(ツ)_/¯ "str" "ing"
string
>> ¯\_(ツ)_/¯ a ¯\_(ツ)_/¯ 3
7
>> ¯\_(ツ)_/¯ a ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ b
110
>> ¯\_(ツ)_/¯ a ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ 3
3
>> ¯\_(ツ)_/¯ b ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ 4
3
>>
>> # Comparisons
>> ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ a b
False
>> ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ a ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ b
False
>> ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ a ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ b
True
>>
>> # Conditional statements
>> ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ True
>>  "printed"
printed
>> ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ False
>>  "not printed"
>> ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ a ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ b
>>  "a is less than b"
a is less than b
```

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

To run a file:

```sh
cat program.shrug | shruglang
```

## Language spec

#### Comments start with \#; no inline comments

`# comment`

#### print

`n`

#### assignment

`n 1`


### math operators start with ¯\\\_(ツ)\_/¯

#### addition

`¯\_(ツ)_/¯ n 3`

#### subtraction

`¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ 3`

#### multiplication

`¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ 4`

#### division

`¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ 4`

#### modulus

`¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ 4`

### comparators start with ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯

#### equality

`¯\_(ツ)_/¯ ¯\_(ツ)_/¯ n m`

#### inequality

`¯\_(ツ)_/¯ ¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ m`

#### greater than

`¯\_(ツ)_/¯ ¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ m`

#### greater than or equal

`¯\_(ツ)_/¯ ¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ m`

#### less than

`¯\_(ツ)_/¯ ¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ m`

#### less than or equal

`¯\_(ツ)_/¯ ¯\_(ツ)_/¯ n ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ m`

### conditional statements start with ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯ ¯\\\_(ツ)\_/¯

```
¯\_(ツ)_/¯ ¯\_(ツ)_/¯ ¯\_(ツ)_/¯ condition
 statement
```

Statement is indented by one more than conditional line. 
No alternate conditions (elif/else)
