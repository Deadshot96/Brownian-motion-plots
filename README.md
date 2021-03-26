# Brownian Motion Functions

### I've given functions which generates and returns Brownian Motion Data
### Each functions returns the _spatial data_ of Brownian motion over a given.
### time period and **time delta** or **time steps**.

##
> ## Structure of the function
>
> ### The function format is similar in all the files.
> ### @ params:
> - t0 => Initial time value - Defaults to 0.0
> - t1 => Final time value - Defaults to 1.0
> - N  => Number of time steps - Defaults to 10_000
> - nums => Number of different instances of motions - Defaults to 3
> - mean => Mean of the Brownian motion - Defaults to 0.0
> - k => Only present in BrowniankD - Number of dimensions
>
> ### The function returns the spatial data in numpy array format.
