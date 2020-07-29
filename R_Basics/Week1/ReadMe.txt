Week 1 Task List

Download R and R Studio
Read the assigned material in R for Everyone.  
Familiarize with R Markdown format 
Create an rpubs account and learn to publish to it from R Markdown.
Go through the Week 1 ungraded quizzes, running your code in RStudio.

Setting up and configuring R and RStudio

	Download R here:  http://www.r-project.org/. 
	Then download RStudio here:  
	http://www.rstudio.com/products/RStudio/download/
	Why R?  The three primary statistical programming languages in use
	today are R, SAS, and SPSS.  R is the fastest growing, and is the
	preferred language among data scientists. The work that you put into
	mastering R in this course (and throughout the MSDA program) will
	help you in being able to more quickly build later fluency in other
	statistical languages as needed.

Why RStudio?  

	RStudio can be thought of us a next generation integrated development
	environment (IDE) for R.  Because of its support for RMarkdown,
	RStudio also better supports:

	Reproducible research (by keeping code and documentation together)
	Documenting data science workflows (and eliminating or at least 
	reducing "manualytics")
	Making more effective presentations

<Optional> “Using RStudio as a 'Front End' to the R Console,”
	http://www.youtube.com/watch?v=7sAmqkZ3Be8, 6 minute video.

Updating R

	R issues regular updates, here is a great overview of how to simply
	update your software: 

	https://www.r-bloggers.com/a-step-by-step-screenshots-tutorial-for-upgrading-r-on-windows/

Core reading:
	Please read the following material in R for Everyone:  Chapter 1-6, 
	8-10


Optional Reading

	For students with more programming background or some previous
	experience with R, you may find interesting the material in Hadley
	Wickham's book, Advanced R 
	(available on-line here: http://adv-r.had.co.nz/). 
	The material in chapter 2 ("Data Structures") and chapter 3 
	("subsetting") map roughly to this week's material. Another book
	aimed for developers (not freely available on-line) is Norman 
	Matloff's The Art of R Programming.

More on R Markdown and Reproducible Research:

	"Reproducible Research," 13-Aug-2014, 58 minute video from RStudio's
	Webinar Series:  Essential Tools for Data Science with R, http://pages.rstudio.net/Webinar-Reproducible-Reporting.html?aliId=352627, with knitr package author Yihui Xie and other presenters.  Please watch the first two parts (36 minutes).
	Familiarize yourself with the material on the R Markdown site here:
	http://rmarkdown.rstudio.com/ 
	RStudio has made some significant recent changes to how reproducible
	research is implemented, so you're encouraged to update your RStudio
	to a recent version. 

	Read R for Everyone, Chapter 23, "Reproducibility, Reports, 
	and Slide Shows with knitr."  
	Some of the information here may be obsolete when using R Markdown
	with RStudio.

	Here's documentation on Hadley Wickham's dplyr package, as an example
	of using R Markdown:  http://rpubs.com/justmarkham/dplyr-tutorial.
	We will use dplyr extensively in Data 607 your first semester.

R Markdown Cheatsheet

	Here is a helpful resource on R Markdown:
	https://www.rstudio.com/wp-content/uploads/2015/02/rmarkdown-cheatsheet.pdf


R Coding Style Guidelines

	Please read
	http://adv-r.had.co.nz/Style.html.
	From the on-line version of Hadley Wickham's book, Advanced R.

Make sure that your versions of both R and RStudio are current!

	You'll want to create an rpubs.com account in advance (free),
	and be logged on when you publish your R Markdown code,.

	Depending on your setup, you may need to install Latex into your
	environment.  RStudio will walk you through this process.

	If you have trouble publishing your code to rpubs.com, you may find
	this tech note helpful:

	http://stackoverflow.com/questions/22537180/error-while-publishing-in-r-pubs

	For me, on my Windows box this meant running notepad as an
	administrator, then adding these two lines to my RProfile.site file
	in my R folder [c:\Program Files\R\R-3.1.2\etc], then restarting R
	Studio (and R):

	options(rpubs.upload.method = "internal")

	options(RCurlOptions = list(verbose = FALSE, capath = system.file("CurlSSL", "cacert.pem", package = "RCurl"), ssl.verifypeer = FALSE))