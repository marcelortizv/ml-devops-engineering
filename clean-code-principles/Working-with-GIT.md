### Working with others with Using Version Control

#### Scenario 1

When you need to work on multiple features at once and switch between them. For instance,
suppose you are working in a feature, and a stakeholder comes to you and he says to
prioritize another feature, so you need to stop the current work and move to work on
another feature.

Step 1: You have a local version of this repository on your laptop, and to get
the latest stable version, you pull from the develop branch.

Switch to the develop branch

`git checkout develop`

Pull the latest changes in the develop branch

`git pull`

Step 2: When you start working on this demographic feature, you create a new branch
called demographic, and start working on your code in this branch.

Create and switch to a new branch called demographic from the develop branch

`git checkout -b demographic`

Work on this new feature and commit as you go

`git commit -m 'added gender recommendations'`

`git commit -m 'added location specific recommendations'`
...

Step 3: However, in the middle of your work, you need to work on another feature.
So you commit your changes on this demographic branch, and switch back to
the develop branch.

Commit your changes before switching

`git commit -m 'refactored demographic gender and location recommendations'`

Switch to the develop branch

`git checkout develop`

Step 4: From this stable develop branch, you create another branch for a new feature
called friend_groups.

Create and switch to a new branch called friend_groups from the develop branch

`git checkout -b friend_groups`

Step 5: After you finish your work on the friend_groups branch, 
you commit your changes, switch back to the development branch, merge 
it back to the develop branch, and push this to the remote repository’s develop branch.

Commit your changes before switching

`git commit -m 'finalized friend_groups recommendations'`

Switch to the develop branch

`git checkout develop`

Merge the friend_groups branch into the develop branch

`git merge --no-ff friends_groups`

Push to the remote repository

`git push origin develop`

Step 6: Now, you can switch back to the demographic branch to continue your 
progress on that feature.

Switch to the demographic branch

`git checkout demographic`


#### Scenario 2

You are working with a teammate in different branches.

Step 1: Andrew commits his changes to the documentation branch, 
switches to the development branch, and pulls down the latest changes 
from the cloud on this development branch, including the change
I merged previously for the friends group feature.

Commit the changes on the documentation branch

`git commit -m "standardized all docstrings in process.py"`

Switch to the develop branch

`git checkout develop`

Pull the latest changes on the develop branch down

`git pull`

Step 2: Andrew merges his documentation branch into the develop branch on 
his local repository, and then pushes his changes up to update the develop 
branch on the remote repository.

Merge the documentation branch into the develop branch

`git merge --no-ff documentation`

Push the changes up to the remote repository

`git push origin develop`

Step 3: After the team reviews your work and Andrew's work, they merge the 
updates from the development branch into the master branch. Then, they push 
the changes to the master branch on the remote repository. These changes are 
now in production.
Merge the develop branch into the master branch

`git merge --no-ff develop`

Push the changes up to the remote repository

`git push origin master`

#### Version Control Workflow
* Creating a new branch
* Adding new features and code
* add , commit, and push your changes to the remote
* Open a pull request
* Have another team member review your changes and merge them in
* Delete the remote branch
* Delete the local branch
* Pull the new code on the remote master to your local machine

#### Scenario 3

When you are experimenting with ML models, you should commit any experiment and
put a significant message to track experiments. For instance, you can say something like:

    'adding behavioral features, train 0.80, cv 0.70'

Step 1: You check your commit history, seeing messages about the changes you 
made and how well the code performed.

View the log history

`git log`

Step 2: The model at this commit seemed to score the highest, so you decide to take a look.

Check out a commit

`git checkout bc90f2cbc9dc4e802b46e7a153aa106dc9a88560`

After inspecting your code, you realize what modifications made it perform well,
and use those for your model.

Step 3: Now, you're confident merging your changes back into the development
branch and pushing the updated recommendation engine.

Switch to the develop branch

`git checkout develop`

Merge the friend_groups branch into the develop branch

`git merge --no-ff friend_groups`

Push your changes to the remote repository

`git push origin develop`

#### Code Reviews Benefits

* Catch Errors
* Ensure readability
* Check standards are met
* Share knowledge among teams

[Code Review Best Practices](https://www.kevinlondon.com/2015/05/05/code-review-best-practices)

[Guidelines for Code Reviews](https://github.com/lyst/MakingLyst/tree/master/code-reviews)


Questions to Ask Yourself when Conducting a Code Review

First, let's look over some of the questions we might ask ourselves while 
reviewing code. These are drawn from the concepts covered throughout this course.

Is the code clean and modular?
* Can I understand the code easily?
* Does it use meaningful names and whitespace?
* Is there duplicated code?
* Can I provide another layer of abstraction?
* Is each function and module necessary?
* Is each function or module too long?

Is the code efficient?
* Are there loops or other steps I can vectorize?
* Can I use better data structures to optimize any steps?
* Can I shorten the number of calculations needed for any steps?
* Can I use generators or multiprocessing to optimize any steps?

Is the documentation effective?
* Are inline comments concise and meaningful?
* Is there complex code that's missing documentation?
* Do functions use effective docstrings?
* Is the necessary project documentation provided?

Is the code well tested?
* Does the code high test coverage?
* Do tests check for interesting cases?
* Are the tests readable?
* Can the tests be made more efficient?

Is the logging effective?
* Are log messages clear, concise, and professional?
* Do they include all relevant and useful information?
* Do they use the appropriate logging level?

Tips for conducting a Code Review

* Use a code linter: Using a Python code linter like pylint can automatically 
  check for coding standards and PEP 8 guidelines for you.
  
* Explain issues and make suggestions: Rather than commanding people to change 
  their code a specific way because it's better, it will go a long way to explain 
  to them the consequences of the current code and suggest changes to improve it.
  They will be much more receptive to your feedback if they understand your 
  thought process and are accepting recommendations, rather than following commands
  
* Keep your comments objective: Try to avoid using the words "I" and "you" in your 
  comments. You want to avoid comments that sound personal to bring the attention 
  of the review to the code and not to themselves.
  
* Provide code examples: When providing a code review, you can save the author 
  time and make it easy for them to act on your feedback by writing out your 
  code suggestions. This shows you are willing to spend some extra time to review
  their code and help them out.