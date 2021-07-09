<div align="center" markdown>
<img src=""/>

# Review labels side by side

<p align="center">
  <a href="#Overview">Overview</a>
  <a href="#How-To-Start">Overview</a>
  <a href="#How-To-Use">How To Use</a>
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

**Step 2**: Create new Labeling job: [Labeling as Scale](https://ecosystem.supervise.ly/labeling/jobs/list)

***SubStep 2.1***: Press `+NEW` button at top right corner
<img src="https://i.imgur.com/zyAQkYZ.png"/>
***SubStep 2.2***:Set Labeling Job: 
 - Title
 - Reviewer
 - Labelers
 - Data to Annotate (Workspace, Project, Dataset)
 - Annotation Settings(Classes, Tags, Labeler sees figures(recommended: Only own), Labeler sees tags (Only for projects with Multiple tags mode)(recommended: Only own))
 - Images Filtering (...)
<img src="https://i.imgur.com/zyAQkYZ.png"/>


# How To Use

**Step 1**: 
**Step 2**: Open context menu of images project -> `Run App` -> `Download via app` -> `Export to Supervisely format` 

<img src="https://i.imgur.com/6JNfu3g.png" width="600px"/>

**Step 3**: Define export settings in modal window

<img src="https://i.imgur.com/jXSSOTW.png" width="600px">

**Step 4**: Result archive will be available for download in `Tasks` list (image below) or from `Team Files` (path format is the following `Team Files`->`Export-to-Supervisely`->`<task_id>_<projectId>_<projectName>.tar`)

<img src="https://i.imgur.com/QjFHRtx.png">
