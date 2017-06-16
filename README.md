# team04-Project

team04 members: [Ian Ferguson](https://github.com/Mr-Ian-Ferguson), [Marhababanu Chariwala](https://github.com/marhabac33), [Vladimir Efimov](https://github.com/efimovvl), [Mark Davydov](https://github.com/MarkDavydov), [Mu Xi (Lucy) Xing](https://github.com/LucyXMX)

Contains copy of Matplotlib for testing/demo purposes only, and claims no ownership of Matplotlib or related code.

## Building matplotlib on ubuntu/linux:
1. Install dependencies:
  * Easiest method is to run: "sudo apt-get build-dep python-matplotlib"
  * Otherwise go to [matplotlib installation guide](http://matplotlib.org/users/installing.html) and manually install dependencies.
2. Install pip dependencies:
  * Install necessary pip dependencies: "sudo pip install numpy pytest pytest-mock mock".
3. From team04-Project change into [matplotlib](https://github.com/CSCD01-Winter2017/team04-Project/tree/master/matplotlib) directory "cd matplotlib".
  * Copy "setup.cfg.template" to "setup.cfg".
  * In "setup.cfg" change "#local_freetype = False" to "local_freetype = True".
  * In "setup.cfg" change "#tests = False" to "tests = True".
4. Build/Install matplotlib:
  * From team04-Project change into matplotlib directory "cd matplotlib-dev/matplotlib".
  * Install "sudo pip install -v -e ./".
5. To test installation:
  * Run "python tests.py".


### Deliverable 1 files location:

1. Team Introduction:
  * content: Introduction of team and team members
  * location: [Deliverable 1/Team_Introduction.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%201/Team_Introduction.pdf)

2. Team Agreement:
  * content: Team's agree expectations and guideline
  * location: [Deliverable 1/Team Agreement.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%201/Team%20Agreement.pdf)

### Deliverable 2 files location:

1. Reverse Engineering Report:
  * content: The description of Matplotlib architecture and design.
  * location [Deliverable 2/ReverseEngineeringReport.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%202/ReverseEngineeringReport.pdf)

2. Diagrams:
  * content: A copy of all the diagrams in their full size
  * location [Deliverable 2/All Diagrams Used.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%202/All%20Diagrams%20Used.pdf)


### Deliverable 3 files location:

1. List of Potential bugs:
  * Content: List of 6 potential bugs that we could fix in Matplotlib. Each entry contains a link to the original github issue and a short description.
  * Location: [potential_bugs.md](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%203/potential_bugs.md).
2. Demo's showing behaviour of bug and in some cases desired behaviour   using work-arounds.
  * Content: code to reproduce the issues.
  * Location: [bug-fix_demos](https://github.com/CSCD01-Winter2017/team04-Project/tree/master/Deliverable%203/bug-fix_demos).
3. Bug Fixes Report
  * Content: Description of issues, solution to resolve issues, code snippets, acceptance testing details and design details
  * Location: [BugFixesReport.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%203/BugFixesReport.pdf) Note: links work when downloaded.
4. Acceptance Testing Files:
  * Content: Acceptance test suite for issues resolved in D3
  * Issue 8059 Acceptance Test Location: [test_BboxConnectorPatch.py](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%203/acceptanceTests/test_BboxConnectorPatch.py).
  * Issue 7460 Acceptance Test Location: [tests_xlim_ylim.py](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%203/acceptanceTests/tests_xlim_ylim.py).
### Deliverable 4 files location:

1. Issue Investigation and Planning report:
  * Content: Description of two chosen major issues. As well as plans of how to implement the bug fix and feature.
  * Location: [IssuePlanningReport.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%204/IssuePlanningReport.pdf).
2. Acceptance Testing File:
  * Content: Acceptance test suite for issue described in the report.
  * Issue 8283 Acceptance Test Location: [Issue8283_acceptance_tests.txt](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%204/Issue8283_acceptance_tests.txt).
3. Unit Testing File:
  * Content: Unit tests that test the chosen issue, implement in the Matplotlib testing libraries.
  * Issue 8283 Unit Test Location: [test_axes.py file starting on line 4947](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/matplotlib/lib/matplotlib/tests/test_axes.py#L4947-L5130).

### Deliverable 5 files location:

  1. Feature Implementation Report:
    * Content: User guide, design documentation, details about changes from deliverable 4.
    * Location: [FeatureImplementation Report.pdf](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%205/FeatureImplementationReport.pdf).
  2. Acceptance Testing File:
    * Content: Acceptance test suite for issue described in the report.
    * Issue 8283 Acceptance Test Location: [Deliverable 5/deliv_5_acceptance_tests.py](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/Deliverable%205/deliv_5_acceptance_tests.py).
  3. Unit Testing File:
    * Content: Unit tests that test the chosen issue, implement in the Matplotlib testing libraries.
    * Issue 8283 Unit Test Location: [test_axes.py file starting on line 4947](https://github.com/CSCD01-Winter2017/team04-Project/blob/master/matplotlib/lib/matplotlib/tests/test_axes.py/#L4947) and [Deliverable 5/tests/](https://github.com/CSCD01-Winter2017/team04-Project/tree/master/Deliverable%205/tests)
    * **Note:** Test added to the main test_axes.py and Deliverable 5/tests are same. Reason to add Deliverable 5/tests folder is that it can be run separately.
