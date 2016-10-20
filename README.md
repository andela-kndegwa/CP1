[![Build Status](https://travis-ci.org/andela-kndegwa/CP1.svg?branch=develop)](https://travis-ci.org/andela-kndegwa/CP1)
[![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)]()
[![Kimani Ndegwa](https://img.shields.io/badge/Kimani%20Ndegwa-FirstCheckpoint-green.svg)]()
[![Coverage Status](https://coveralls.io/repos/github/andela-kndegwa/CP1/badge.svg?branch=staging)](https://coveralls.io/github/andela-kndegwa/CP1?branch=staging)

# AMITY ROOM ALLOCATION SYSTEM.

>A project done in fulfillment of the first checkpoint of the Andela training program.

#1. Problem definition / statement.

The main objective of this project is to model a room allocation system for one of Andela’s facilities called Amity.

**Who? Fellows and staff at one of Andela's facilities alias Amity.**

Fellows and staff at Andela's Amity facility are the immediate consumers of the system.

**What? A room allocation system**

The goal is to model and build a room allocation system that smoothens the problem of keeping track of office ad living spaces at Amity, providing a scalable and usable solution.

>An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

**Where? Office spaces and living spaces.**

The system manages office spaces as well as living spaces and ensures they are allocated effectively.

**When? On request to occupy a space.**

The spaces mentioned above need to be allocated when vacant or occupied and/or reallocated as well as give status on their status when required.
The system serves to also tell how many people are in a given space at any given time.

**Why? To ensure smooth and seamless allocation and transfer of rooms amongst fellow and staff.**

The criteria set to solve the problem is to ensure the rooms can and will be allocated on request to get a new space whether office space or living space.
There is also the need to have a way of determing how many people are at a particular space from time to time.


#2. Commands.

Command | Argument | Example
--- | --- | ---
create_room | L or O | create_room O Krypton
add_person | (first_name) (last_name) (person_type) [--accomodate] |add_person Jermaine Cole Fellow --accomodate=Y
reallocate_person | (identifier) (new_room_name) | reallocate_person F1 Dreameville
load_people | (filename) | load_people samplefile.txt
print_allocations| [--o=filename] | print_allocations --o=allocations
print_unallocated| [--o=filename] | print_unallocated --o=allocations
print_room | (room_name) | print_room Fayetteville
save_state | [--db=sqlite_database]| save_state --db=carolina
load_state |(sqlite_database)|load_state my_newdatabase

#3. Installation and set up.

1. First clone this repository to your local machine using `git clone https://github.com/andela-kndegwa/CP1.git`

2. Checkout into the **develop** branch using 'git checkout develop'

3. Create a *virtualenv* on your machine and install the dependencies via `pip install -r requirements.txt` and activate it.

4. cd into the *amity* folder and run `python app.py`

#4. Usage
The following screencast shows how to run the different commands. Check it out:

[![asciicast](https://asciinema.org/a/ecendttdj3a4lrp89n8luus30.png)](https://asciinema.org/a/ecendttdj3a4lrp89n8luus30)

## Credits

1. [Kimani Ndegwa](https://github.com/andela-kndegwa)

2. The amazing [Andela](https://www.andela.com) community.

## License

### The MIT License (MIT)

Copyright (c) 2016 [Kimani Ndegwa](https://www.kimanindegwa.co.ke).

> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in
> all copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
> THE SOFTWARE.
