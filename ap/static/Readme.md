## An Introduction to Front End Development

Front end development and organization can get very messy without conventions in place. Please refer back to this guide and update this guide to prevent that.

## Front end goals:

### Have a standardized way to add libraries and new files.
It is very easy to have 3 jquery libraries, 5 boostrap libraries and 10 ways to load in bootstrap / jquery and your own js/css.
To prevent this, we rely on conventions - there is one standard way of doing things, and everything should follow this standard

### Don't copy paste code. Modularize
Programming is about creating blocks of code that you can reuse and build upon.
It may be tempting to copy paste code for the sake of time, but that is a big mistake.
There are very good tools (webpack, BEM) to help front end work stay organized and well engineered, and for the sake of future developers, you should use learn them and use them.

### Organize, maintain, and update libraries
Please also look around on this site before installing or implementing functionality.
(See below for where to find out where our static js and css files are located.
For Django, the Django REST API and its framework, Viewsets, and the templating system reduce code/complexity dramatically.)

### Use a build system to minimize and combine files
Run `npm run start` from the root directory to start the webpack build system.

Using a build system gives a lot of advantages.
* First, a build system allows you to develop with unminified code and then minify during production. This is very useful for debugging.
* Second, a build system allows you to add many libraries and files while keeping your load times small.
* Third, a build system standardizes the process in which you load files, ensuring that there is only one way to add files into the pipeline.

## Front end tooling

### Webpack
Bundle and pre-process assets.

### SASS
Upgraded CSS. Allows nesting, variables, mixins and lots of other really important functionality that promote clean code and reusability.

### BEM
BEM is not a tool, but rather a convention for writing your html and css classes. It stands for block__element--modifier, and it forces you to think of things in these ways.

BEM is extremely important in keeping your CSS reusable and maintainable. Read more about it here: http://getbem.com/introduction/.

## Navigating around the front end AP


### Djattendance Folder Structure
```
|webpack # contains webpack configuration and stats files
|package.json # add dependencies from npm.js/github here, or run npm i --save [package-name]
|ap
|--[module-name]
|----static/[module-name] # good place to add module-specific css and js
|----templates # module-specific templates
|--static
|----css # css used in several modules, but not site-wide
|----js # js used in several modules, but not site-wide
|----images # ALL IMAGES GO HERE
|--templates # templates used in several modules
|----index.js # require site-wide js and css from node_modules and libraries in here
|libraries # custom AP code that doesn't go in package.json
|--ap # js and css used site-wide
|--bootflat-ftta # custom site theming
|--react # react code
```
