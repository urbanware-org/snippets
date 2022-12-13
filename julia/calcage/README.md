# calcage

Simple *Julia* method to to either calculate a person's age in years or year of birth.

This module is also available for the *Python* programming language [here](https://github.com/urbanware-org/snippets/tree/master/python/calcage).

## Usage

For using the method, there are three parameters required in the following order:

*   Day
*   Month
*   Year or age

Notice that the following examples have been created on February 19<sup>th</sup>, 2018.

### Age in years

What is the age from a person that is born on January 4<sup>th</sup>, 1990?

Calling the method with the corresponing year of birth as third argument

```julia
calcage(4, 1, 1990)
```

it returns the value `28`.

*   Date of birth: `1990-01-04`
*   Age in years: `28`

### Year of birth

What is the year of birth from a person with the age of 31 that was born on February 22<sup>nd</sup>?

Calling the method with the age in years as third argument

```julia
calcage(22, 2, 31)
```

it returns the value `1986`.

*   Date of birth: `1986-02-22`
*   Age in years: `31`
