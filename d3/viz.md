---
layout: tutorial
title: "d3 basics"
---

# d3 Basics

## DOM / HTML

* element: some element in the page such as a p or a div
* attribute: a href="foo" 
* html document is like a tree...
	* parents
	* children

Elements will have one or both of these attributes:

* id
* class

css selector:

* `#id`
* `.class`

* `tagName#id`
* `tagName.class`

* `tagName #id`
* `tagName .class`


## Build a Bar Chart Manually With Divs

<style class="show">
.chart-manual div {
	background-color: #222;
	text-align: right;
	margin: 1px;
	color: #fff;
}
</style>

<div class="chart-manual show">
	<div style="width: 30px">3</div>
	<div style="width: 70px">7</div>
	<div style="width: 90px">9</div>
	<div style="width: 50px">5</div>
</div>


<div style="height: 200px">
</div>

## D3

### Overview

When we build a chart:

* made up of elements
* some data is matched to an element

### d3

* programmatically bind data to element
* create elements
* modify their attributes, etc.
* d3 provides a bunch of helper modules for creating charts and graphs
	* create an axis
	* scale this data from "data" space to "display" space
	* a bunch of primitives for building visualizations

1. source some data
2. create div elements
3. bind data to those div elements

#### installing

just include this script tag:

```
<script src="https://d3js.org/d3.v5.js"></script>
```

* codepen
* jsfiddle - tell them to use d3
* observablehq - jupyter notebook js/html 
* npm to install it and use grunt or gulp to include in project

<script src="https://d3js.org/d3.v5.js"></script>

#### finding / selecting elements

* `d3.select` return just one element
* `d3.selectAll` returns all elements

both return something called a _selection_
selections have methods can call:

* .style ... prop/val for a specific style for all elements in that selection
* .text ... set the text content for an element
* .attr ... set an arbitrary attribute on that element or all elements in selection
* .append // returns thing appended as the selection

^^^ these mostly return original selection

### Data Join

1. select (which can work from an element, not just `d3`) some elements that are not present
2. call a method called `data` on the result of that `select`
	* bind data (`Array`) to elements
	* if your selection has elements that are bound to some data already
	* ... then the data will be updated
	* if there are no elements, then the data will be bound to newly created elements
	* if there's no data, but elements with bound data, then elements will be removed
	* ...after data... to get at added /  updated elements / removed
		* `enter`
		* `update`
		* `exit`

<style class="show">
.chart-auto div {
	background-color: #222;
	text-align: right;
	margin: 1px;
	color: #fff;
}
</style>

<div class="chart-auto">
</div>

Map from domain (data) to range (display)

<script>
const x = d3.scaleLinear()
	.domain([0, 10])
	.range([0, 500])

console.log(x(1));
</script>

<script>

const chartAutoData = [3, 7, 9, 5];
const chartAuto = d3.select('.chart-auto');
chartAuto.selectAll('div')
	.data(chartAutoData)
	.enter() // all the newly created elements because we have more data than existing ele
	.append('div')
		.text((d, i) => d)
		.style('width', d => x(d) + 'px');

// console.log(chartAuto);
// const h1 = chartAuto.append('h1');
// h1.text('hello!');
// h1.attr('foo', 'bar');
</script>

## SVG

images are typically a matrix of pixels

these are called __raster__ images

vector graphics.... images are created by using points and connecting those points with lines or curves

Scalable Vector Graphics - SVG

* an XML format for images
* it's a markup language
* it can be used embedded directly in pages
* it can be examined via web inspector
* offers primitives like:
	* `rect`
	* `circle`
	* `g`
	* `svg`
* kind of like html.... but diff elements ^^^
* can be styled... but of course, diff props:
	* `background-color` &rarr; `fill`
* coordinate system is 0,0 at upper left
	* y increases as it goes down page

<!--

<svg class="show" width="1000" height="400">
<rect width="300" height="300" x="0" y="0" fill="red"></rect>
<rect width="200" height="400" x="100" y="50" fill="yellow"></rect>
<text x="100" y="100" fill="#000">hello!!!!!!!</text>
<circle cx="100" cy="250" r="50" fill="green"></circle>

<g transform="translate(300, 50)">
<rect width="300" height="300" x="0" y="0" fill="red"></rect>
<rect width="200" height="400" x="100" y="50" fill="yellow"></rect>
<circle cx="100" cy="250" r="50" fill="green"></circle>
</g>

<svg>
-->


<style class="show">
svg.auto-chart rect {
	fill: #000;
}
svg.auto-chart text {
	fill: #fff;
	font-size: 15px;
	text-anchor: end;
}
</style>


<!--
<svg class="auto-chart show" width="400" height="100">
<g transform="translate(0, 0)">
	<rect width="30" height="19"></rect>
	<text x="27" y="12">3</text>
</g>
<g transform="translate(0, 20)">
	<rect width="70" height="19"></rect>
	<text x="67" y="12">7</text>
</g>
</svg>
-->

<svg class="auto-chart show" width="400" height="100">
</svg>

<script>
const scaleX = d3.scaleLinear()
	.domain([0, 10])
	.range([0, 500])
const data = [3, 7, 9, 5];
const autoChartSVG = d3.select('.auto-chart');
const bars = autoChartSVG.selectAll('g')
	.data(data).enter().append('g')
	.attr('transform', (d, i) => `translate(0, ${i * 20})`)
bars.append('rect')
	.attr('width', d => scaleX(d))
	.attr('height', 19);
bars.append('text')
	.attr('x', d => scaleX(d) - 4)
	.attr('y', 12)
	.text(d => d);
</script>














<div style="height: 400px"></div>

















