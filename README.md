# Artifact

Artifact package for our paper "How do Developers Talk about GitHub Actions?". This repository includes our data and scripts. 

## Data
1. Data Collection
	* SO data, i.e., posts, from the official SO data dump (as of October 2021)
	* GitHub data, i.e., issues, using the GitHub Search API
2. Data for manual classification: `SO post` and `GitHub issue`
	* This data includes: 
    	- 3,285 SO posts (Q\_S) with 1,224 accepted SO answers (A\_S)
    	- 130 GitHub issues (Q\_G) with 82 closed GitHub issues (A\_G)
    * The data for manual classification can be found in `post_issue.csv`
    * Data structure: (id, paper_no, type, title, url)
	    1. paper\_no: the number used in this paper. "P1" and "I1" represent the first SO post and the first GitHub question in our dataset, respectively.
	    2. type: "github issue" or "so post"
	    3. title: the title of a post or an issue
	    4. url: url of a post or an issue   
3. Data for characteristics analysis
	* The data for manual classification can be found in `post_popularity.csv` and `post_issue_difficulty.csv`
	* post\_popularity includes 3,285 SO posts' view number, favorite number, score and answer number
	* post\_issue\_difficulty includes the following matrixs of 3,285 SO posts and 130 issues:
		1. interval\_fir\_ans: median time interval to the first answer (issue comment), in second
		2. interval\_acc\_ans: median time interval to the accepted answer (issue closure), in second
		3. body\_len: the sum of character numbers of the question (issue) description

## Script
We implement the prediction models using Python with the scipy package
* Spearman's rank correlation coefficient `correlations.py`

## Figure
* Figure 1: The trend of GHA discussed on Stack Overflow
* Table 1: Popularity of GHA-related discussion categories
* Table 2: Difficulty of GHA-related discussion categories
* Table 3: Correlation between Popularity and Difficulty of GHA-related discussion categories (on SO)
