---
layout: default
title: {{ site.name }}
pdf: true
permalink: /
---

<div style="float:right; margin-bottom:50px; color:#666">
Version: {{ site.version }}<br>
</div>

<div>
    <img src="img/expfactoryticketyellow.png" style="float:left">
</div><br><br>

> Nobody ever comes in... and nobody ever comes out...

<p>And that's the way that reproducible behavioral experiments should be: designed, captured, and used again with assurance of running the same thing.
The Experiment Factory software will help you create a reproducible container to deploy behavioral experiments. Want to jump right in? Choose one of our demo containers, and browse to localhost:</p>


```
docker run -p 80:80 vanessa/expfactory-games start
docker run -p 80:80 vanessa/expfactory-surveys start
docker run -p 80:80 vanessa/expfactory-experiments start
```

Next, read more about [generation](pages/1-generate.md) of your own experiment container. Please [give feedback](https://www.github.com/expfactory/expfactory/issues) about your needs to further develop the software. The [library](https://expfactory.github.io/experiments/) will show you a selection to choose from, including all experiments, surveys, and games migrated from [the legacy Expfactory](https://www.github.com/expfactory/expfactory-experiments). If you have web-based experiments to contribute, please [reach out](https://www.github.com/expfactory/expfactory/issues)! Your contributions and feedback are greatly appreciated!


## User Guide

 - [Building](pages/1-generate.md) your battery means creating and configuring your image.
 - [Using](pages/2-usage.md) an experiment factory container.
 - [Contribute](pages/3-contribute.md) an experiment to the [library](https://www.github.com/expfactory/experiments) for others to use.

## Library

 - [Browse](https://expfactory.github.io/experiments/) our available experiments [[json]](https://expfactory.github.io/experiments/library.json).
 - [Generate](https://expfactory.github.io/experiments/generate) a custom container from our Library, or
 - [Recipes](https://expfactory.github.io/experiments/recipes) view a pre-generated recipe based on tags in the library.


<div>
    <a href="/expfactory/generate"><button class="next-button btn btn-primary"><i class="fa fa-chevron-right"></i> </button></a>
</div><br>
