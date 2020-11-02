# Runoff

Implement a program that runs a runoff election, per the below.

```
python runoff.py Alice Bob Charlie
Number of voters: 5
Rank 1: Alice
Rank 2: Bob
Rank 3: Charlie

Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob

Rank 1: Bob
Rank 2: Charlie
Rank 3: Alice

Rank 1: Bob
Rank 2: Alice
Rank 3: Charlie

Rank 1: Charlie
Rank 2: Alice
Rank 3: Bob

Alice
```


## Background

You already know about plurality elections, which follow a very simple algorithm for determining the winner of an election: every voter gets one vote, and the candidate with the most votes wins.

But the plurality vote does have some disadvantages. What happens, for instance, in an election with three candidates, and the ballots below are cast?

![Five ballots, tie betweeen Alice and Bob](fptp_ballot_1.png)

A plurality vote would here declare a tie between Alice and Bob, since each has two votes. But is that the right outcome?

There's another kind of voting system known as a ranked-choice voting system. In a ranked-choice system, voters can vote for more than one candidate. Instead of just voting for their top choice, they can rank the candidates in order of preference. The resulting ballots might therefore look like the below.

![Three ballots, with ranked preferences](ranked_ballot_1.png)

Here, each voter, in addition to specifying their first preference candidate, has also indicated their second and third choices. And now, what was previously a tied election could now have a winner. The race was originally tied between Alice and Bob, so Charlie was out of the running. But the voter who chose Charlie preferred Alice over Bob, so Alice could here be declared the winner.

Ranked choice voting can also solve yet another potential drawback of plurality voting. Take a look at the following ballots.

![Nine ballots, with ranked preferences](ranked_ballot_3.png)

Who should win this election? In a plurality vote where each voter chooses their first preference only, Charlie wins this election with four votes compared to only three for Bob and two for Alice. But a majority of the voters (5 out of the 9) would be happier with either Alice or Bob instead of Charlie. By considering ranked preferences, a voting system may be able to choose a winner that better reflects the preferences of the voters.

One such ranked choice voting system is the instant runoff system. In an instant runoff election, voters can rank as many candidates as they wish. If any candidate has a majority (more than 50%) of the first preference votes, that candidate is declared the winner of the election.

If no candidate has more than 50% of the vote, then an "instant runoff" occurrs. The candidate who received the fewest number of votes is eliminated from the election, and anyone who originally chose that candidate as their first preference now has their second preference considered. Why do it this way? Effectively, this simulates what would have happened if the least popular candidate had not been in the election to begin with.

The process repeats: if no candidate has a majority of the votes, the last place candidate is eliminated, and anyone who voted for them will instead vote for their next preference (who hasn't themselves already been eliminated). Once a candidate has a majority, that candidate is declared the winner.

Let's consider the nine ballots above and examine how a runoff election would take place.

Alice has two votes, Bob has three votes, and Charlie has four votes. To win an election with nine people, a majority (five votes) is required. Since nobody has a majority, a runoff needs to be held. Alice has the fewest number of votes (with only two), so Alice is eliminated. The voters who originally voted for Alice listed Bob as second preference, so Bob gets the extra two vote. Bob now has five votes, and Charlie still has four votes. Bob now has a majority, and Bob is declared the winner.

What corner cases do we need to consider here?

One possibility is that there's a tie for who should get eliminated. We can handle that scenario by saying all candidates who are tied for last place will be eliminated. If every remaining candidate has the exact same number of votes, though, eliminating the tied last place candidates means eliminating everyone! So in that case, we'll have to be careful not to eliminate everyone, and just declare the election a tie between all remaining candidates.

Some instant runoff elections don't require voters to rank all of their preferences — so there might be five candidates in an election, but a voter might only choose two. For this problem's purposes, though, we'll ignore that particular corner case, and assume that all voters will rank all of the candidates in their preferred order.

Sounds a bit more complicated than a plurality vote, doesn't it? But it arguably has the benefit of being an election system where the winner of the election more accurately represents the preferences of the voters.

## Getting Started

Here's how to download this problem's "distribution code" (i.e., starter code) into your own CS50 IDE. Log into [CS50 IDE](https://ide.cs50.io/) and then, in a terminal window, execute each of the below.

* Execute `cd` to ensure that you're in `~/` (i.e., your home directory).
* Execute `cd pset3` to change into (i.e., open) your `pset3` directory that should already exist.
* Execute `wget https://raw.githubusercontent.com/cs50nestm/web/master/distro/runoff.py` to download a (compressed) ZIP file with this problem's distribution.
* Execute `unzip runoff.zip` to uncompress that file.
* Execute `rm runoff.zip` followed by `yes` or `y` to delete that ZIP file.
* Execute `ls`. You should see a directory called `runoff`, which was inside of that ZIP file.
* Execute `cd runoff` to change into that directory.
* Execute `ls`. You should see this problem's distribution code, in a file called `runoff.py`.

## Understanding

Let's open up `runoff.py` to take a look at what's already there. We're defining two constants: `MAX_CANDIDATES` for the maximum number of candidates in the election, and `MAX_VOTERS` for the maximum number of voters in the election.

Next up is a Class called `Candidate`. Since Python is an [object oriented programming language](https://realpython.com/lessons/classes-python/), it usees classes to create custom objects. Here we create custom candidate objects with our `Candidate` class. Every candidate has a properties for their `name`, the number of `votes` they currently have, and `eliminate`, which has a value of eitehr True or False depending on whether the candidate is eliminated from the election. 

Next up is a list `candidates` which will eventually contain a `Candidate` object to keep track of all the candidates in the election.

Following is a two-dimensional list `preferences`. The list `preferences[i]` will represent all of the preferences for voter number `i`, and the integer `preferences[i][j]` here will store the index of the candidate who is the `j`th preference for voter `i`.

Now onto `main`. Notice that after determining the number of candidates and the number of voters (both as global variables), and initializing the list `candidates`, the main voting loop begins, giving every voter a chance to vote. As the voter enters their preferences, the `vote` function is called to keep track of all of the preferences. If at any point, the ballot is deemed to be invalid, the program exits.

Once all of the votes are in, another loop begins: this one's going to keep looping through the runoff process of checking for a winner and eliminating the last place candidate until there is a winner.

The first call here is to a function called `tabulate`, which should look at all of the voters' preferences and compute the current vote totals, by looking at each voter's top choice candidate who hasn't yet been eliminated. Next, the `print_winner` function should print out the winner if there is one; if there is, the program is over. But otherwise, the program needs to determine the fewest number of votes anyone still in the election received (via a call to `find_min`). If it turns out that everyone in the election is tied with the same number of votes (as determined by the `is_tie` function), the election is declared a tie; otherwise, the last-place candidate (or candidates) is eliminated from the election via a call to the `eliminate` function.

If you look a bit further down in the file, you'll see that these functions — `vote`, `tabulate`, `print_winner`, and `find_min`, `is_tie` and `eliminate` — are all left to up to you to complete!

## Specification

Complete the implementation of `runoff.py` in such a way that it simulates a runoff election. You should complete the implementations of the `vote`, `tabulate`, `print_winner`, `find_min`, `is_tie`, and `eliminate` functions, and you should not modify anything else in `plurality.py`.

### `vote`

* Complete the `vote` function.
  * The function takes arguments `voter`, `rank`, and `name`. If `name` is a match for the name of a valid candidate, then you should update the preferences list to indicate that the voter `voter` has that candidate as their `rank` preference (where `0` is the first preference, `1` is the second preference, etc.).
  
  * If the preference is successfully recorded, the function should return `true`; the function should return `false` otherwise (if, for instance, `name` is not the name of one of the candidates).
  <br/>
  
  <details>
    <summary>Hints</summary>
    <ul>
    <li data-marker="*">Recall that candidate_count stores the number of candidates in the election.</li>
    <li data-marker="*">Recall that `preferences[i][j]` stores the index of the candidate who is the `j`th ranked preference for the `i`th voter.</li>
  </ul>
</details>

### `tabulate`
  
* Complete the `tabulate` function.
  * The function should update the number of `votes` each candidate has at this stage in the runoff.
  * Recall that at each stage in the runoff, every voter effectively votes for their top-preferred candidate who has not already been eliminated.
  <br/>
  
  <details>
    <summary>Hints</summary>
    <ul>
  <li data-marker="*">Recall that <code class="highlighter-rouge">voter_count</code> stores the number of voters in the election.</li>
  <li data-marker="*">Recall that for a voter <code class="highlighter-rouge">i</code>, their top choice candidate is represented by <code class="highlighter-rouge">preferences[i][0]</code>, their second choice candidate by <code class="highlighter-rouge">preferences[i][1]</code>, etc.</li>
  <li data-marker="*">Recall that the <code class="highlighter-rouge">candidate</code> <code class="highlighter-rouge">struct</code> has a field called <code class="highlighter-rouge">eliminated</code>, which will be <code class="highlighter-rouge">true</code> if the candidate has been eliminated from the election.</li>
  <li data-marker="*">Recall that the <code class="highlighter-rouge">candidate</code> <code class="highlighter-rouge">struct</code> has a field called <code class="highlighter-rouge">votes</code>, which you’ll likely want to update for each voter’s preferred candidate.</li>
</ul>
</details>

### `print_winner`

* Complete the `print_winner` function.
  * If any candidate has more than half of the vote, their name should be printed to `stdout` and the function should return `true`.
  * If nobody has won the election yet, the function should return `false`.
* Complete the `eliminate` function.
  * The function should eliminate the candidate (or candidates) who are still in the race and have the fewest number of votes.
  * If all remaining candidates are tied at the same number of votes, then the function should not eliminate anyone and return `false`.
  * Otherwise, the function should reset all candidates' vote counts back to `0` and return `true`.
  
### `find_min`

### `is_tie`

### `eliminate`

## Walkthrough

TODO

## Usage

Your program should behave per the example below:

```
./runoff Alice Bob Charlie
Number of voters: 5
Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob

Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob

Rank 1: Bob
Rank 2: Charlie
Rank 3: Alice

Rank 1: Bob
Rank 2: Charlie
Rank 3: Alice

Rank 1: Charlie
Rank 2: Alice
Rank 3: Bob

Alice
```

## Testing

Be sure to test your code to make sure it handles...

* An election with any number of candidate (up to the `MAX` of `9`)
* Voting for a candidate by name
* Invalid votes for candidates who are not on the ballot
* Printing the winner of the election if there is only one
* Not eliminating anyone in the case of a tie between all remaining candidates

Execute the below to evaluate the correctness of your code using check50. But be sure to compile and test it yourself as well!

```
check50 cs50nestm/checks/2020/runoff
```

Execute the below to evaluate the style of your code using style50.

```
style50 runoff.py
```

## How to Submit

### Step 1 of 2
Ensure that your terminal is positioned in the correct directory.

### Step 2 of 2
Execute the below, logging in with your GitHub username and password when prompted. For security, you’ll see asterisks (*) instead of the actual characters in your password.

```
submit50 cs50nestm/checks/2020/runoff
```
