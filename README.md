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
- `modeling` - Python notebooks to build review score prediction models.
    - `Hypermodel.ipynb` - Notebook which builds and tests my best found model.
    - `Hypertuning.ipynb` - Notebook which uses KerasTuner to search for hyperparameter combination which results in the best model.
- `baselines` - Where files that helped assess my baselines reside.
    - `LLMPrompt.txt` - The prompt structure that I used to assess the LLM. Just replace "[review]" with an actual review.
    - `human` - Files for assessing a human's prediction ability.
        - `MakeFilesForHumans.py` - Chooses 100 files from each of two folders, combines them, randomizes their order, and then produces two text files, a test and a key.
        - `reviews.txt` - The test, 200 reviews, 100 positive and 100 negative, in random order.
        - `key.txt` - The key, with each number corresponding the folder that it came from to the review in the test file.

## Extracted ZIP File Hierarchies

- `ReviewsSortedAgain.zip`
ReviewsSortedAgain
├── high_80
│   ├── 0_100.txt
│   ├── 5_95.txt
│   ├── . . .
│   └── 68688_80.txt
├── low_50
│   ├── 3_45.txt
│   ├── 26_48.txt
│   ├── . . .
│   └── 68669_14.txt
└── mid_50_80
    ├── 1_65.txt
    ├── 4_65.txt
    ├── . . .
    └── 68679_70.txt
- `ReviewsMidExcludedEqualSamples.zip`
ReviewsMidExcludedEqualSamples
├── high_80
│   ├── 0_100.txt
│   ├── 5_95.txt
│   ├── . . .
│   └── 16428_80.txt
└── low_50
    ├── 3_45.txt
    ├── 26_48.txt
    ├── . . .
    └── 68669_14.txt
- `ReviewsMidExcludedEqualSamplesSplit.zip`
ReviewsMidExcludedEqualSamplesSplit
├── test
│   ├── high_80
│   │   ├── 11_80.txt
│   │   ├── 31_98.txt
│   │   ├── . . .
│   │   └── 16426_92.txt
│   └── low_50
│       ├── 86_35.txt
│       ├── 222_10.txt
│       ├── . . .
│       └── 68669_14.txt
└── train
    ├── high_80
    │   ├── 0_100.txt
    │   ├── 5_95.txt
    │   ├── . . .
    │   └── 16428_80.txt
    └── low_50
        ├── 3_45.txt
        ├── 26_48.txt
        ├── . . .
        └── 68633_5.txt
