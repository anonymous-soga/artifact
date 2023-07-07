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
	- paper\_no: the number used in this paper. "P1" and "I1" represent the first SO post and the first GitHub question in our dataset, respectively.
	- type: "github issue" or "so post"
	- title: the title of a post or an issue
	- url: url of a post or an issue   
3. Data for characteristics analysis
    * The data for manual classification can be found in `post_popularity.csv` and `post_issue_difficulty.csv`
    * post\_popularity includes:
     	- avgView, the average number of views for all the questions of a category;
        - avgFav, the average number of favorites for all the questions of a category;
        - avgScore, the average score for all the questions of a categpru;
        - avgAns, the average number of answers for all the questions of a category. 
    * post\_issue\_difficulty includes:
	- ansRate, the percentage of questions of a category with at least one answer;
  	- acceptRate, the percentage of questions of a category that have accepted answers;
       	- timeFA, the median time needed for questions of a category to receive the first answers, in hours;
	- timeAA, the median time needed for questions of a category to receive the accepted answer, in hours; 
   	- textSize, the average number of description characters for questions of a category.
4. The accepted answer examples and detailed discussion of each solution strategy can be found in `solution_strategies.md`

## Script
We seek to analyze the characteristics of the identified problem categories in terms of popularity and difficulty. 
* Spearman's rank correlation coefficient `cor.R`

## Figure
* Figure 1: The trend of GHA discussed on Stack Overflow
* Figure 2: The taxonomy of GHA problems
* Table 1: Popularity of GHA problem categories
* Table 2: Difficulty of GHA problem categories
* Table 3: Correlation between Popularity and Difficulty of GHA problem categories
* Table 4: Difficulty of GHA problem categories (GitHub issues)
