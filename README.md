<div align="center" markdown>
<img src="https://i.imgur.com/kXDrJcK.png"/>

# Review labels side by side

<p align="center">
  <a href="#Overview">Overview</a>
  <a href="#How-To-Start">Overview</a>
  <a href="#How-To-Use">How To Use</a>
  <a href="#Extra-options">How To Use</a>
</p>


[![](https://img.shields.io/badge/supervisely-ecosystem-brightgreen)](https://ecosystem.supervise.ly/apps/supervisely-ecosystem/review-labels-side-by-side)
[![](https://img.shields.io/badge/slack-chat-green.svg?logo=slack)](https://supervise.ly/slack)
![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/supervisely-ecosystem/review-labels-side-by-side)
[![views](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/review-labels-side-by-side&counter=views&label=views)](https://supervise.ly)
[![used by teams](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/review-labels-side-by-side&counter=downloads&label=used%20by%20teams)](https://supervise.ly)
[![runs](https://app.supervise.ly/public/api/v3/ecosystem.counters?repo=supervisely-ecosystem/review-labels-side-by-side&counter=runs&label=runs)](https://supervise.ly)

</div>

# Overview
Application allows to review pre-marked by annotators image projects, choose the best markups and tags. Also, these markup and tags can be transferred to the original image for your own futher corrections.

# How To Start

**Step 1**: Add app to your team from [Ecosystem](https://ecosystem.supervise.ly/apps/review-labels-side-by-side) if it is not there.
    
   - select `Ecosystem` in Main Menue
   - put `Review labels side-by-side` in the search bar
   - open app page by clicking on it
   - add app to your team by pressing `Get` button

<img src="https://i.imgur.com/tl60QE4.png"/>

**Step 2**: Create new [Labeling job](https://docs.supervise.ly/labeling/jobs) and open it. Look for project's extra options below.

<img src="https://i.imgur.com/simXGmk.png"/>

**Step 3**: Open newly created Labeling job -> Run app by clicking `Run` button. Open it. 

<img src="https://i.imgur.com/d5PHeMZ.png"/>

   **Note**: You can replace `Apps` area to the left/right by managing `Panel settings` (step 3 on the picture)

# How To Use

**Step 1**: In opened window there are 2 avalible tabs: `Objects` and `Tags`. Each tab consists of 3 sections: 

For Objects:
 - `Filter by users`, `Filter by classes` and `Filtered objects` 

For `Tags`:
 - `Filter by users`, `Filter by tags` and `Filtered tags`

<img src="https://i.imgur.com/ohkTWR6.png"/>

**Step 2**: Select target users, classes, tags and copy them to annotation area(right section). 
   
 - Select enabl/disable target checkboxes for each section. 
 - Press `Filter` to preview results. Also, for `objects` tab, you can preview each object in a gallery.    
 - To copy objects and tags press `Copy selected objects` for objects and `Copy selected tags` for tags respectively. 
   
   Corresponding data will appear at annotation area a few moments later.

<img src="https://i.imgur.com/IwYpP4c.png">

# Extra options

**Step 1**:Set recommended options for target Project:

<img src="https://i.imgur.com/zlWukS5.png" height="1000px"/>

**Step 2**: Create Labeling Job: set following options
 - Title
 - Reviewer(s)
 - Labeler(s)
 - Data to Annotate: 
   - Required Workspace
   - Required Project(s)
   - Required Dataset(s)
 - Annotation Settings:
   - Required Class(es)
   - Required Tag(s) 
   - Labeler sees figures(recommended: Only own)
   - Labeler sees tags(recommended: Only own))
 - Images Filtering options
