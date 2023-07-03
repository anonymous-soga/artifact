# Artifact

Artifact package for our paper "How do Developers Talk about GitHub Actions?". This repository includes our data and scripts. 

## Data
1. Data Collection
	* SO data, i.e., posts, from the official SO data dump (2018.10.1-2022.10.31)
	* GitHub data, i.e., issues, using the GitHub Search API
2. Data for manual classification: `SO post` and `GitHub issue`
	* This data includes: 
    	- 6,590 SO posts (Q\_S) with 2,471 accepted SO answers (A\_S)
    	- 315 GitHub issues (Q\_G) with 217 closed GitHub issues (A\_G)
    * The data for manual classification can be found in `post_issue.csv`
    * Data structure: (id, paper_no, type, title, url)
	    1. paper\_no: the number used in this paper. "P1" and "I1" represent the first SO post and the first GitHub question in our dataset, respectively.
	    2. type: "github issue" or "so post"
	    3. title: the title of a post or an issue
	    4. url: url of a post or an issue   
3. Data for characteristics analysis
	* The data for manual classification can be found in `post_popularity.csv` and `post_issue_difficulty.csv`
	* post\_popularity includes 6,590 SO posts' view number, favorite number, score and answer number
	* post\_issue\_difficulty includes the following matrixs of 6,590 SO posts
		1. ansRate,the percentage of questions of a category with at least one answer;
  		2. acceptRate, the percentage of questions of a category that have accepted answers;
       		3. timeFA, the median time needed for questions of a category to receive the first answers, in hours;
	 	4. timeAA, the median time needed for questions of a category to receive the accepted answer, in hours; 
   		5. textSize, the average number of description characters for questions of a category. 

## Script
We implement the prediction models using Python with the scipy package
* Spearman's rank correlation coefficient `correlations.py`

## Figure
* Figure 1: The trend of GHA discussed on Stack Overflow
* Table 1: Popularity of GHA problem categories
* Table 2: Difficulty of GHA problem categories
* Table 3: Correlation between Popularity and Difficulty of GHA problem categories
