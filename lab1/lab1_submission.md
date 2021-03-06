**CSDA1040: Advanced Methods of Data Analysis**

**Lab 1 -Recommender System**

**Recommender System for The Movies Database**

**Submitted By Group 8**

Michaela Hrabetova (ID: 217590209)

Lu Han (ID: 217618638)

Tony Chan (ID: 217635038)

Cristina Endara (ID: 217625567)

Sangeeta Khanna (ID: 217638719)

**Date of Submission:** May 25, 2020


# GIT

- We share work on github.com. Link is [here](https://github.com/todatech/csda-lab.git)

# Introduction
During the last few decades, with the rise of Amazon, Youtube, Netflix and many other such web services, recommender systems becomes more and more common in our lives. Recommendation systems help users find and select items (e.g., books, movies, restaurants) from the huge number available on the web. In general, recommender systems are algorithms aimed at suggesting relevant items to users (items being movies to watch, text to read, products to buy etc.). Providing an effective and personalized movie recommender system to the users was our primary motivation in project. In this project, we will go through 4 different movie recommender systems. For each of them, we will present how they work, describe their theoretical basis and discuss their strengths and weaknesses.

# Description of Dataset

The current project is based on a dataset from The Movie Database obtained from Kaggle (https://www.kaggle.com/rounakbanik/movie-recommender-systems/data). It contains data for 45,000 movies released between 1874 and 2017, including genre, budget/revenue, production country/company, runtime, popularity, vote count/rating from individual users, etc.

The final dataset includes only movies that have been realeased. Features such as revenue, id and realease date have been removed as they are irrelevant to the analysis and given the high amount of null values they show. Numeric and date type conversions have been performed as well. This final dataset was saved as a separate csv file to be to loaded onto the server and to be used to carry out the modeling of the recommender system.


# Data Exploration

The purpose of this project is to develop a recommender system utilizing this dataset. Within this context, we will have a closer look at the popularity rating, vote rating and vote count of the different tittles in order to undertand futher their behaviour.

Popularity and vote count show a preference towards newer movies, having the Top 10 movies within these categories a release date after 2009 (with one exception in 1999). Top movies based on vote rating average show earlier release dates.

Most popular movies include Minions (2015), Wonder Woman (2017), Beauty and the Beast (2017), Baby Driver (2017) and Big Hero 6 (2014).

All movies have been categorized into 32 different genres, of which drama and comedy represent 74% of the dataset.

### Performance, Analysis and Machine Learning Models of Movies Recommender Systems

This project includes four different recommender systems for the movies dataset: simple recommender, content based recommender, collaborative filtering recommender and hybrid recommender.

1. Simple recommender

    This system recommends movies that are "highly acclaimed" based on high number of votes (vote count in the upper 0.05% quantile) and presents a list to the end user ranked by the highest vote average rating. The table below shows the results for the Top Ten Movies:

        Top Movies Overall:
                id                     title release_date
        0     862                 Toy Story   1995-10-30
        46    807                     Se7en   1995-09-22
        255    11                 Star Wars   1977-05-25
        288   101    Leon: The Professional   1994-09-14
        291   680              Pulp Fiction   1994-09-10
        313   278  The Shawshank Redemption   1994-09-23
        350    13              Forrest Gump   1994-07-06
        358  8587             The Lion King   1994-06-23
        474   329             Jurassic Park   1993-06-11
        521   424          Schindler's List   1993-11-29

    The same has been applied to the different genres. The following table includes the Top Ten Movies in the Romance category:

        Top Movies in Romance:
             id                                  title release_date
        350        13                           Forrest Gump   1994-07-06
        580       812                                Aladdin   1992-11-25
        1628      597                                Titanic   1997-11-18
        2165      162                    Edward Scissorhands   1990-12-05
        7168       38  Eternal Sunshine of the Spotless Mind   2004-03-19
        13071    8966                               Twilight   2008-11-20
        19598   82693                Silver Linings Playbook   2012-09-08
        20762   64682                       The Great Gatsby   2013-05-10
        22003  152601                                    Her   2013-12-18
        23262  102651                             Maleficent   2014-05-28

    This method only shows top rated movies for all voters. The following sections explore different ways to recommend movies tailored to our end users based on user preferences.

2. Content Based Recommender

    This system relies on text mining techinques to mine keywords for individual movies titles. Utilizing Term Frequency - Inverse Data Frequency for the overview and the tagline features of the all the movies, it identifies keywords that are "unique" to each title. Next, a cosine similarity matrix finds similiarity amoung the 45,000 different movie titles. When end user of the system provides a movie title of his/her choice, the recommender system will recommend a list of movies that are highly related to this choice based on the keywords frequencies found in the description for all movies.

    The two tables below present a list of the top ten movies recommender to the user if they like "The Godfather" and the "Dark Night Rises".  

        Recommended these movies if you like : The Godfather
                   id                             title release_date
        1171      240            The Godfather: Part II   1974-12-20
        4300    15745                              Made   2001-07-13
        10764   18747                          Election   2005-05-14
        11239  119907                  Household Saints   1993-09-15
        18206   48153                   The Outside Man   1972-12-21
        21458  112205                        The Family   2013-09-13
        22952  190955                        Blood Ties   2013-08-22
        31693   95892                  Honor Thy Father   1973-03-01
        37660  135335          A Mother Should Be Loved   1934-05-11
        43540  364150  The Godfather Trilogy: 1972-1990   1992-10-17

        Recommended these movies if you like : The Dark Knight Rises
                  id                                              title release_date
        150      414                                     Batman Forever   1995-06-16
        584      268                                             Batman   1989-06-23
        1321     364                                     Batman Returns   1992-06-19
        3079   14919                       Batman: Mask of the Phantasm   1993-12-25
        9181   16234                 Batman Beyond: Return of the Joker   2000-12-12
        12421    155                                    The Dark Knight   2008-07-16
        15433  40662                         Batman: Under the Red Hood   2010-07-27
        21042  29751  Batman Unmasked: The Psychology of the Dark Kn...   2008-07-15
        21247  21683                    Batman: Mystery of the Batwoman   2003-10-21
        25074  20077                                  Batman vs Dracula   2005-10-18
    
    The content based engine recommender has some limitations. It can only suggest movies which are close to a certain movie. That is, it is not capable of capturing personal tastes and providing recommendations across genres. Anyone use our system for recommendations based on a movie will receive the same recommendations for that movie.

3. Collaborative Filtering Recommender
    
    Collaborative filtering for recommender systems are methods that are based solely on the past interactions recorded between users and items in order to produce new recommendations. In the dataset, "rating.csv" contained a series of movie rating records (rating from 1-5) by individual users. By leveraging a python package called "scikit-surprise", we are able to build a collaborative filtering recommender system with ease. In a simplier term, we used SVD algorithm to train a model with sets of rating records, that consisted of userid, movieid, and rating information. We further used this model to predict what the end user will rate for a given movie id. We validated our prediction in our analysis and it gives roughly ~0.9 RSME accuracy for 5-fold cross-validations.

        For User:  1
        Movies that this user rated before:
                id                           title release_date
        2284   1371                       Rocky III   1982-05-28
        2577   2105                    American Pie   1999-07-09
        3197   2193                        My Tutor   1983-03-04
        4580   2294  Jay and Silent Bob Strike Back   2001-08-22
        8265   1405                           Greed   1924-12-04
        10664  2455            Confidentially Yours   1983-08-10

        Moives that this user may like:
                 id                               title release_date
        333    2064             While You Were Sleeping   1995-04-21
        3042    926                        Galaxy Quest   1999-12-23
        4000    318            The Million Dollar Hotel   2000-02-09
        6108   6016                      The Good Thief   2003-04-03
        6351    296  Terminator 3: Rise of the Machines   2003-07-02
        11407  1247                   The Good Shepherd   2006-12-11

4. Hybrid Recommender

    For Hybrid Recommender, we combine the best of CB Recommender and CF Recommender to give better recommendation. First, we obtain a list of high-related movies based on end user's input, and then we evaluate each of the title to see which has higher predicted rating. Then, we present this list to our end user in a descending order list. By using our hybrid recommender, people can get different recommendations for different users although the movie is the same. Hence, this recommender system is more personalized and tailored towards particular users.

        Based on your ranking history and that you are watching this movie: 
        Avatar

        We think you might like these: 
                 id                                       title release_date
        602    8766                       Hellraiser: Bloodline   1996-03-08
        2444    603                                  The Matrix   1999-03-30
        3057  10384                                   Supernova   2000-01-14
        3517  38688             Pandora and the Flying Dutchman   1951-02-15
        3633  16096                               House Party 2   1991-10-23
        3638  26270                           Project Moon Base   1953-09-04
        4590   8922                            Jeepers Creepers   2001-07-01
        044   9567                            Tears of the Sun   2003-03-07
        6378   1996  Lara Croft Tomb Raider: The Cradle of Life   2003-07-21
        9028  63054                                    Fetishes   1996-09-12
  
# Conclusion

In this project, we have built 4 different recommender systems based on different ideas and algorithms. They are as follows:

1. Simple Recommender: This system used overall Vote Count and Vote Averages to build Top Movies Charts, in general and for a specific movie category.
2. Content Based Recommender: We built two content based engines; one that took movie overview and taglines as input and the other which took metadata such as cast, crew, genre and keywords to come up with predictions. We also deviced a simple filter to give greater preference to movies with more votes and higher ratings.
3. Collaborative Filtering: We used the Surprise Library to build a collaborative filter based on single value decomposition. The RMSE obtained was less than 1 and the engine gave estimated ratings for a given user and movie.
4. Hybrid Engine: We combine the idea from content and collaborative filterting to build an engine that gave movie suggestions to a particular user based on the estimated ratings that it had internally calculated for that user.

# Deployment

These movie recommender systems are useful for the streaming companies such as Crave or Netflix in order to engage the viewers and keep them on the website for longer period of time and more often while increasing customer’s satisfaction with the services. 

These models can be improved by including the following information to complement the existing dataset:
1.	Provide gender and other related information about individual customer
2.	Provide geographical location on watching movies
3.	Provide time-variant of this dataset, such as holiday movie watching

This model should be reviewed and updated every 3-5 years, as we wish to find out whether there is a change of consumer behaviors. This might be due to changes in external factors that are not depicted in our model.
