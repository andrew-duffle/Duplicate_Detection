# Duplicate_Detection
A simple duplicate detection for text based on similarities
Theory:
To start I built the program only use the diff command in bash the results were just not great when I went to read the highest ranked comments. This lead me down the path of a hybrid approach of using diff and comm. 

Diff is used to compare the differences between the two documents resulting back in a list of edits to make the two documents the same. I decided that if this was the edits to make the documents the same then 1 – this is the degree to with they are the same. I initially build a shingling process but quick discovered there were very few comments that shared common patterns. I quickly changed my approach to word comparison. 

Comm is used to identify the common words between the two comments verse the total words. This seemed to be the better performer of the two processes.

In the end I ended up with a hybrid where the degree of likeness is a formula with a weighting of importance of Comm 60% Diff 40%.
((Number of same words / U of doc1 words and doc 2 words)*.6)+(1-(edits to be the match / length doc1 + doc2)*.4) = the likeness score.


Code:
Instead of creating 41 different documents in the bash code (made that mistake the first time) and per the comment board I Python as the document manager. First the discussion document is parsed into a python dictionary. Then as we are compare the results we move them into the comparison documents to use the command line (diff and comm). This ensured easy management of the documents. The first document created will be for the first comment and the second one created is used repeatedly for the comment we are comparing to. Each of these have capitalization and punctuation removed.   Since I selected to compare comments based on words and I wanted to keep each comment intact I went ahead and created a second version of these documents that are the word lists we actually compare. I used the original comment docs to stop the code and read the comments when I found like ones. 

Once I had the word lists I changed over to the Linux Bash and used the os.system to call both diff and comm and return results and convert each to a likeness score.

Instead of keeping all the results in memory I created a simple database to hold the results as the code ran. Finally I return all the results in the database ordered by the likeness score. 

To my surprise the results appeared very go. I was able to read the top ~10 results and certainly see the common element of them.  It appeared they all referred to encryption and external off network storage. I felt pretty good at this point. The top likeness scores were as follows 6 22, 6 20, 2 6, 14 18, 6 15, 3 6, 13 15, 6 18, 20 22, 3 22. All of these had pretty good likeness scores. 

One thing noted that I will address in future iteration is stop words. I have always removed them in R when working with text analytics. I believe that would help here also.

Run Code:
There is not much to know about running the code. Two things to note if you want to run it on a different document on line 18 the discussions.thorn doc will need to be replaced with whatever document you want to use. On line 21 the delimiter might need to be changed to match the new document. Currently it is set as a thorn. 
