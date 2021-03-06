# Analysis of Homework Submission Time (AnHoST)

This project takes CSVs of multiple class sections over many years to combine,
analyze, perform statistics on, and plot homework submissions.

## Purpose:

1. Analyze homework submission and impact of switching from classroom-and-LMS
   method to fully-online video-and-LMS method for the class "Data Science
   Fundamentals", a required general studies class at Kanazawa University,
   Japan.
2. Generate a *really* beautiful graph and statistics useful for both analysts
   and educators.
3. Maintain privacy of the students involved.
4. Make this tool compatible with other LMSes. For example, through the use of a
   preprocessor system for various LMSes (Moodle, etc.).

## Scope:

1. This work concerns only submission timing. It does not consider score at this
   moment because it was originally designed for a "submit or fail" class.
2. This work IS designed to work with multiple classes and years. It is designed
   for a long-standing and massive course.
3. The current preprocessing script works only with WebClass, specifically, the
   implementation at Kanazawa University. We plan to generalize this as we work
   with other institutions and LMSes.

## For researchers:

Original sample data is not available due to privacy reasons, but we have made
a sample table using [generatedata](https://github.com/benkeen/generatedata)
(names) and [random.org](https://random.org) (numbers and date/time).

If you need the original data for RDM or auditing purposes, please contact the
main author. (Also ensure that you're looking at the MAIN repo, not any fork.)

## Technical Requirements:

This work was created on/for:

* Python 3.8
* pandas 1.0.5
* numpy 1.19.0
* matplotlib 3.2.2
* seaborn 0.10.1
* Windows 10 (this is why I'm trying to stay away from awk/bash/shell stuff)

Python 2 support is not guaranteed. Other dependencies for the listed packages
may be required.

## About "SO::"

The main author uses SO::#### as a shorthand to refer to StackOverflow ANSWER
numbers. Replace SO:#### with https://stackoverflow/a/#### for answer URL.

## Copyright:

The main author retains copyright in the program. He does NOT own the original
datasets (not shown in current version). See the LICENSE file for details.

