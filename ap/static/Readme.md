## An Introduction to Front End Development

Front end development and organization can get very messy without conventions in place. Please refer back to this guide and update this guide to prevent that.

## Front end goals:

### Have a standardized way to add libraries and new files.
``` 
It is very easy to have 3 jquery libraries, 5 boostrap libraries and 10 ways to load in bootstrap / jquery and your own js/css. 
To prevent this, we rely on conventions - there is one standard way of doing things, and everything should follow this standard
```

### Don't copy paste code. Modularize
```
Programming is about creating blocks of code that you can reuse and build upon. It may be tempting to copy paste code for the sake of time, but that is a big mistake. There are very good tools (gulp, sass, BEM) to help front end work stay organized and well engineered, and for the sake of future developers, you should use learn them and use them.
```

### Organize, maintain, and update libraries 
```
Front-end libraries should be located in predictable. Libraries that we don't modify should be installed via bower. Libraries that we do modify should go into the libraries folder. This allows us to know which files we have modified and what libraries we can upgrade.

Django serves all static files in ap/static. If there are too many files in there, django can slow down substantially. To prevent this, we keep our bower_components and node_modules in the root directory, and copy them over as needed using 'gulp bower-move'.

Read more about moving bower files using bower-main-files here: 
http://clubmate.fi/bower-and-gulp-match-made-in-heaven-also/
```

### Use a build system to minimize and combine files
```

Using a build system gives a lot of advantages.
First, a build system allows you to develop with unminified code and then minify during production. This is very useful for debugging.
Second, a build system allows you to add many libraries and files while keeping your load times small. 
Third, a build system standardizes the process in which you load files, ensuring that there is only one way to add files into the pipeline.

```

## Front end tooling

Front end tooling is really important to accomplish the above goals. These are the tools that we are currently using:

### Bower
```
A front end package manager. It makes sure your front end files (jquery, libraries, plugins) are localized, versioned, and can be updated in one place.
```

### Gulp
```
A front end build tool. It takes source files and compiles them in real time. This is really useful for sass and to a lesser extend javascript. 
```

### SASS
```
Upgraded CSS. Allows nesting, variables, mixins and lots of other really important functionality that promote clean code and reusability. 

```

### BEM
```
BEM is not a tool, but rather a convention for writing your html and css classes. It stands for block__element--modifier, and it forces you to think of things in these ways. 

BEM is extremely important in keeping your CSS reusable and maintainable. Read more about it here: _____________.

```

## Navigating around the front end AP

```
Folder Structure:

|modules/templates
|static
|--bower_components # copied bower managed libraries
|--libraries # CUSTOM LIBRARIES that build on top of existing libraries or are internally modified
|--css # css stylesheets that pertain to a particular page
|----compiled # compiled sass stylesheets. Put here so everyone knows to modify scss instead of these files
|--scss # sass stylesheets that output to css/compiled
|--js # javascript that pertains to a particular page
|--images # ALL IMAGES GO HERE
|--fonts 
|--react-gulp # old react build - to be refactored into the new front end management
|templates # where all your html files are stored
```


Q: What is the difference between /libraries/ and /bower_components/? When should I put a library in one or the other?

A: /libraries/ is for custom libraries. These are libraries that don't support bower, need to be modified or have a custom build. bower_components should hold standard libraries that don't need customization.


Q: I want to install a library. How do I do it?

```
bower install --save <library-name>
gulp bower-move

# then in your module's layout:

{% static bower_components/<library-name>/bin/<library-file.js/css>}

```

Q: I want to install a library and then heavily modify it.

A: For minor modifications, you can add it to static/libraries/. If you are going to rewrite major parts of the library, you should fork the library and then clone it from there. Then you can commit, pull and push changes to it.
