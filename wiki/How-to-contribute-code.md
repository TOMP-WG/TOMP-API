[home](https://github.com/TOMP-WG/TOMP-API/wiki/) > [Contribution](Contribution.md) > [How to contribute](How-to-contribute-code.md)  

# How to contribute code

## Quick start for anyone familiar with git, GitHub and git flow
We use a version of Git Flow with two develop branches, `develop-major` for breaking changes that need to go in the next major version and `develop-minor` for adding features and backward-compatible fixes.
Make sure there's an issue describing what you intend to work on and let us know that you assigned it to yourself. Create a fork if you're not a regular contributor and work in a `feature/short-title` branch off of one of the develop branches, depending on whether it constitutes a breaking change or not. Before creating a pull request, squash your commits into a small functional set and rebase it onto the latest develop commit. Usually this would be one commit, but in larger features readability for reviewers might benefit from splitting it into a few steps. 

## The tools we use
We use **Git** and in particular its concept of branches for the development of TOMP-API. If you're not familiar with git and using branches, read [this tutorial](https://backlog.com/git-tutorial/) or another like it. Learning all the terminal commands is not required, but understanding the underlying ideas is important. Apps like [SourceTree](https://www.sourcetreeapp.com) abstract away the actual commands, but you still should understand the ideas.

As part of collaborating on code we use **Pull Requests** (PR) so all contributions are reviewed by multiple people before being added. This results in fewer mistakes and higher quality code. As a regular contributor, you can create branches in the repository itself for your feature and create a PR to merge it, see [this tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow). Otherwise, you need to fork the repository first and work in a feature branch there, see [this tutorial](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow). 

Because we want to keep a clear versioning system for our users, changes should not simply be merged into a single centralised branch. Instead, we organise our branches along **Git Flow** principles, see [this description](https://nvie.com/posts/a-successful-git-branching-model/).

## Our branches
Our branches are organised in a Git Flow structure, resulting in the following branches and properties of each branch:
* `master` contains the released versions of the API
  - contains only two types of commits
    - release commits with a new semantic version
    - commits that do not change any file containing code (e.g. add a name to the README)
  - contains only working versions of the API
  - the API corresponds to one released with a version number
  - the latest commit contains the latest release of the API
* `develop-minor` contains all the completed changes for the next _minor_ version of the API. Please don't use this branch, but use the upcoming 'minor': e.g. when the upcoming version is 1.4.0 (1.3.0 is released), create changes on top of 1.3.0.
* `develop-major` contains all the completed changes for the next _major_ version of the API. Please don't use this branch, but use the upcoming 'major': e.g. when the current version is 1.3.0, use 2.0.0. Use this only when your proposal is a breaking one.
* zero or one `release-<x>.<y>` with a feature-frozen version from `develop` waiting to merge into `master`
  - branches off of one of the `develop` branches
  - only contains bug fix commits
  - is eventually merged into `master` as a new release and into the `develop` branch it came from to add the bug fixes there too
  - contains only working versions of the API
* zero or more `feature/<feature-name>` for developing a new feature for a `develop` branch
  - branches off of one of the `develop` branches
  - once finished, merged into its originating `develop` branch
  - can contain WIP commits while working on it, these should be squashed before merging
* zero or more `hotfix-<issue_number>` branches to work on or contain patch versions
  - branches off of one of the commits in `master` (the version for which the hotfix is intended)
  - contains only bug fixes
  - is merged into `master` and the `develop` branches _if_ it is a hotfix for the latest release, otherwise it might just live on its own branch as a patch version of a maintained release

## Workflows

### Workflow for a feature or bug fix
Before you start
a. Create an issue for your feature or bug if it isn't there already and describe it
b. Assign the issue to yourself so others know you're working on it
Making the changes
1. Fork the repository if you're not a regular contributor
2. `git clone` the repository to your local machine
3. `git checkout` a development (or release) branch (minor if your change is non-breaking, major if it is)
4. `git checkout -b feature/<your-feature-name>` to create a new branch
5. Make changes to the code
6. `git add` and `git commit` your changes (and push them for backup if doing this over a span of days)
Repeat 5 and 6 until the feature is complete
7. Squash the commits into a single commit or a few logical commits
8. `git push` your changes to the repo
9. Create a Pull Request to merge it into the develop/release branch you started from
10. Await reviews by (other) regular contributors and make any requested changes

### Other changes
In general, leave these to the regular contributors who understand the branching strategy well. Tell us in your issue if you think a bug fix should be in a hotfix branch so it can be in a patch release. Minor and major release branches are created after the working group decides to.

### Q&A <br>
**Q**: How do I synchronise a forked repository with the master?<br>
_A_: use this command:
<pre>
git pull upstream master
</pre>
If you get the message <pre>git pull upstream master
fatal: 'upstream' does not appear to be a git repository
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.</pre>
you can check if the original master (or feature branch) is the _upstream_ repository. You can add it using <pre>git remote add upstream https://github.com/TOMP-WG/TOMP-API.git</pre>