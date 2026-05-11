# review-predictions

## Folder and File Breakdown

- `data` - If you just want the raw data, you can find it here!
    - `reviews` - Folder with raw review data in multiple formats.
        - `all-reviews.txt` - Basically a CSV file, but tab-separated instead of comma-separated. Format is [username][tab][score][tab][review][newline]. Includes reviews with a score of NR.
        - `ReviewsSorted.zip` - Review and score data, NR scores/reviews excluded. When extracted, you get three subfolders, `low_50`, containing reviews with a score of under 50, `mid_50_80`, containing those between 50 and 79, inclusive, and `high_80`, containing those 80 and above. Within each of these folders is text files that just contain the raw text of the reviews.
        - `ReviewsMidExcludedEqualSamples.zip` - Same as above, but reviews with scores between 50 and 79, inclusive, have been excluded, and a number of positive reviews equal to the number of negative reviews have been randomly chosen so that there are an equal quantity of each.
        - `ReviewsMidExcludedEqualSamplesSplit.zip` - Same as above, but 20% of each of the positive and negative reviews have been chosen for training. The structure now consists of two subfolders: `train` and `test`, each of which contains two subfolders, `low_50` and `high_80`, each of which contains review text files.
        - `reviews.txt` - First half of all-reviews.txt. Vast majority are positive.
        - `reviews-low.txt` - Second half of reviews.txt. More negative reviews in this one.
    - `link-lists` - List of links to the albums that I collected reviews from.
        - `review-links.txt` - List of links to review pages for albums from the 2020s. Reviews sorted by recent.
        - `review-links-low.txt` - List of links to review pages for albums from the 2010s. Reviews sorted by worst.
- `scraping-scripts` - If you want to try collecting the data yourself!
    - `album-review-links.py` - Produces a text file containing a list of links to review pages on Album of The Year. 2020s albums, links sort reviews by most recent.
    - `album-review-links-low.py` - Same as above, except 2010s albums and links sort reviews by worst.
    - `album-reviews.py` - Produces a file containing many reviews of albums from the 2010s. **Takes several hours. This is on purpose, so that we don't send too many requests all at once.**
    - `album-reviews-low.py` - Same as above, but from the 2010s. **Takes several hours. This is on purpose, so that we don't send too many requests all at once.**
- `data-split-scripts` - To split CSV files into individual text files and make testing set.
    - `Sorting.py` - Reorganizes single text file of reviews into folders of individual review text files according to whether they correspond to a low, mid, or high score. NR reviews excluded.
    - `MakeTestingSet.py` - Extracts 20% of files to put into a new folder for a testing set.