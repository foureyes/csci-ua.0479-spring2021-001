---
layout: tutorial
title: "d3 Overview"
---


# d3 Overview

This is a summary of the 3 parts of the tutorial, [Let's Make a Bar Chart](https://bost.ocks.org/mike/bar/), by Mike Bostock.

## Basics!

### Creating a Chart Manually With Divs and Styling

With some html and css, we can _hand code_ a bar chart:

<style class="show">
.manual-chart div {
text-align: right;
background-color: black;
color: white;
padding: 0.25em;
margin: 0.25em;
}
</style>

<div class="manual-chart show" markdown="block">
  <div style="width: 40px;">4</div>
  <div style="width: 80px;">8</div>
  <div style="width: 90px;">9</div>
  <div style="width: 140px;">14</div>
  <div style="width: 200px;">20</div>
</div>



### Installing d3

Include using script tags:

```
<script src="https://d3js.org/d3.v5.js"></script>
```
<script src="https://d3js.org/d3.v5.js"></script>


<!--
<div id="scratch">Scratch Pad</div>
-->

### Some Basics / Finding and Adding

Defintions for HTML Doc

* element
* attribute
* tree like structure: child/parent
* css selectors, class and id

Selections

* a __selection__ is a group of related elements
* with a __selection__, multiple elements can be manipulated as if they were a single entity

Finding elements... both return a _selection_

* `d3.select`: find element
* `d3.selectAll`: finding multiple  elements
* both of these can also be called on a specific element to find elements within a containing element

Some methods that can be called on a selection:

* `selection.append`: add child
* `selection.text`: add text

<script>
const body = d3.select('body');
const div = body.append('div')
div.attr('id', 'scratch')
div.text('END OF BODY')
</script>

### Chaining Methods

You can chain methods instead of constantly calling 

* selections returns selected elements
* methods can be called directly
* most methods will return the original selection that they were called on
* this allows chaining of method calls

<script>
d3.select('#scratch')
	.style('font-size', '2em')
	.style('font-color', 'green')
	.attr('className', 'foo');
</script>

Note that some methods return a new selection, tho!

(like `append`... where new selection is the element just added)

<div class="demo-append show">
I'm in a div!
</div>

<script>
d3.select('.demo-append')
	.append('h1')
	.style('font-color', 'red')
	.text('I AM ADDED!');
</script>


### Generating a Chart!

Here, have some data:

<script>
const nums = Array(10).fill(20).map(ele => Math.floor(Math.random() * ele)); 
console.log(nums);
</script>

Start with some styles and a container

```
<div class="auto-chart show"></div>
```

<div class="auto-chart show"></div>

<style class="show">
.auto-chart div {
text-align: right;
background-color: black;
color: white;
padding: 0.25em;
margin: 0.25em;
}
</style>


We'll use the `Array`, `nums` to create divs with an appropriate width

<script>
d3.select(".auto-chart")
	.selectAll("div")
		.data(nums)
	.enter().append('div')
		.style('width', d => d * 10 + 'px')
		.text(d => d);
</script>

* note the _selection_ where nothing exists (that is, trying to find a div in `.auto-chart`)
* this is the start of a __data join__ 
	* it's a _pattern_ for creating, updating or destroying elements whenever data changes
	* the initial selection isn't actually selecting elements, it's declaring the elements that you want to create
* the actual __joining__ of data occurs when you call `data` on the resulting `selection`
	* in this case, the argument passed to `data` is an array of values
	* we'll use these values to create divs!
	* it returns a new selection that from which we can retrieve:
		* new elements (elements not yet bound to data)
		* updated elements (elements with bound data, but updated)
		* removed elements (elements that no longer have corresponding data)
	* these selections can be retrieved with:
		* `enter` - represents new data, not yet bound to element
		* `update` - represents data to be updated
		* `exit` - 
	* calling `enter()` gives us the new unbound data
	* using `append` will create an element and bind datum to that element per datum in original data
	* of course, we know that append gives us the new element back as a selection
	* note that style and text can be called... with functions
	* instead of setting a static value
	* function will be called with datum bound to element


### Scaling 


Using nums from previous...

* get min and max of nums to use as __domain__
	* domain represents "data" space
* specify the dimensions of the displayed chart using __range__
	* "display" space

`scaleLinear` will give back a function (as specified by calls to domain and range) that will translate from "data" space to "display" space:

<script>
const x = d3.scaleLinear()
	.domain([0, d3.max(nums)])
	.range([0, 20 * d3.max(nums)])
</script>

This function will translate data into display (if domain is 0 to 10 and range is 0 to 100, then translating 2 would give 20)!

Now use this function in our chart

<style class="show">
.auto-chart-scale div {
text-align: right;
background-color: black;
color: white;
padding: 0.25em;
margin: 0.25em;
}
</style>

```
<div class="auto-chart-scale show"></div>
```

<div class="auto-chart-scale show"></div>

<script>
d3.select('.auto-chart-scale')
	.selectAll('div')
		.data(nums)
	.enter().append('div')
		.style('width', d => x(d) + 'px')
		.text(d => d);
		
</script>

## SVG

### Some definitions

* __Scalable Vector Graphics__ - XML format for specifying _vector graphics_
* __Vector Graphics__ - images that are defined by specifying 2d points and connecting those points with lines or curves (rather than having a _matrix_ of pixels / rater, for example)
	* smaller (size / space) than raster images
	* svg, pdf, eps

A bit clumsy drawing with HTML elements. SVG provides primitives like lines, curves, shapes... all through SVG elements and their attributes. BTW, you can use SVG in a page and inspect it as if it were HTML in your browser!

* it's a lot like html - elements, nesting, styles!
* however, you'll have a bunch of different elements
	* `g` a grouping of elements...
		* we'll use this attribute: `transform=translate(x, y)`
		* to move multiple elements
	* `rect` with `width` and `height`
	* `text` with `x`, `y` and `dy` attributes
		* note that text is an element and can have a `fill`
* and different properties for styling
	* `background-color` &rarr; `fill`
	* `text-align: left` &rarr; `text-anchor: end`
* coordinate system from upper left: 0, 0

### Drawing

<svg class="show" width="500" height="500">

<rect x="50" y="50" width="150" height="150" fill="red"></rect>
<rect x="175" y="100" width="75" height="75" fill="green"></rect>
<circle cx="150" cy="150" r="50" fill="yellow"></circle>

<g transform="translate(25, 200)">
<rect x="50" y="50" width="150" height="150" fill="red"></rect>
<rect x="175" y="100" width="75" height="75" fill="green"></rect>
<circle cx="150" cy="150" r="50" fill="yellow"></circle>
</g>


</svg>

### Drawing a Chart Manually With SVG

<style class="show">
.chart-svg rect {
	fill: #000;
}

.chart-svg text {
	fill: #fff;
	font-family: sans-serif;
	font-size: 15px;
	text-anchor: end;
}
</style>

<svg class="chart-svg show" width="500" height="120">
	<g transform="translate(0, 0)">
		<rect width="40" height="29"></rect>
		<text x="35" y="15" dy="0.35em">4</text>
	</g>
	<g transform="translate(0, 30)">
		<rect width="80" height="29"></rect>
		<text x="75" y="15" dy="0.35em">8</text>
	</g>
	<g transform="translate(0, 60)">
		<rect width="90" height="29"></rect>
		<text x="85" y="15" dy="0.35em">9</text>
	</g>
	<g transform="translate(0, 90)">
		<rect width="30" height="29"></rect>
		<text x="25" y="15" dy="0.35em">3</text>
	</g>
</svg>

* position with translate
* all positions are relative to origin on upper left
* `y` vs `dy`? ... `y` is absolute within element... `dy` shifts it from its current position

## Generating an SVG Chart

No problem! I mean, mostly. A couple of things:

* use `attr` to add arbitrary attributes.
	* first arg is attribute to add, second arg is value or function 
* functions usually have data passed to it... but also position (f(d, i))

Let's start with an empty `svg` container element:

```
<svg class="auto-chart-svg" width="500" height="500"></svg>
```

<style class="show">
.auto-chart-svg rect {
	fill: #000;
}

.auto-chart-svg text {
	fill: #fff;
	font-family: sans-serif;
	font-size: 20px;
	text-anchor: end;
}
</style>

<svg class="auto-chart-svg" width="500" height="500"></svg>

<script>
const scaleX = d3.scaleLinear()
	.domain([0, d3.max(nums)])
	.range([0, 500]);
</script>
<script>
const barHeight = 40;
const chart = d3.select('.auto-chart-svg');
chart.attr('height', barHeight * nums.length);
const bars = chart.selectAll('g')
	.data(nums)
		.enter()
	.append('g')
		.attr('transform', (d, i)  => `translate(0, ${i * barHeight})`);
bars.append('rect')
	.attr('width', (d, i) => scaleX(d) + 'px')
	.attr('height', barHeight - 1);

bars.append('text')
	.attr('x', d => scaleX(d) - 10)
	.attr('y', barHeight - 10)
	.text(d => d);
</script>

## Again but Rotated - Manually at First


<style class="show">
.bar-chart-manual rect {
	fill: #000;
}
.bar-chart-manual text {
	fill: #fff;
	font-family: sans-serif;
	font-size: 10px;
	text-anchor: end;
}

</style>

```
<svg class="auto-chart-svg" width="500" height="500"></svg>
```

<style class="show">
.bar-chart rect {
	fill: #000;
}

.bar-chart text {
	fill: #fff;
	font-family: sans-serif;
	font-size: 20px;
	text-anchor: middle;
}
</style>

<svg class="bar-chart show" width="500" height="200">
	<g transform="translate(0, 0)">
		<rect y="70" width="19" height="30"></rect>
		<text x="10" y="90">3</text>
	</g>
	<g transform="translate(20, 0)">
		<rect y="30" width="19" height="70"></rect>
		<text x="10" y="50">7</text>
	</g>
	<g transform="translate(40, 0)">
		<rect y="10" width="19" height="90"></rect>
		<text x="10" y="30">9</text>
	</g>
	<g transform="translate(60, 0)">
		<rect y="50" width="19" height="50"></rect>
		<text x="10" y="70">5</text>
	</g>
</svg>

### Automatically

Using:

```
<svg class="bar-chart-auto"></svg>
```

<style class="show">
.bar-chart-auto rect {
	fill: #000;
}

.bar-chart-auto text {
	fill: #fff;
	font-family: sans-serif;
	font-size: 20px;
	text-anchor: middle;
}
</style>

Note that when we scale so that the display space is flipped....

We start from the other side (90 instead of 10)

```
const scaleY = d3.scaleLinear().domain([0, 10]).range([100, 0]);
console.log(scaleY(1));
// 90
```
<script>
const maxHeight = 200;
const scaleY = d3.scaleLinear()
	.domain([0, d3.max(nums)])
	.range([200, 0]);
</script>

<svg class="bar-chart-auto"></svg>

<script>
const barChart = d3.select('.bar-chart-auto');
barChart.attr('height', maxHeight);
const myBarWidth = 40;
const vBars = barChart.selectAll('g')
	.data(nums)
		.enter()
	.append('g')
		.attr('transform', (d, i) => `translate(${myBarWidth * i}, 0)`)

vBars.append('rect')
	.attr('y', d => scaleY(d))
	.attr('width', myBarWidth)
	.attr('height', d => maxHeight - scaleY(d));
vBars.append('text')
	.attr('x', 20)
	.attr('y', d => (scaleY(d) + 20))
	.text(d => d);

</script>


<!--
<style>
.chart rect {
  fill: steelblue;
}

.chart text {
  fill: white;
  font: 10px sans-serif;
  text-anchor: middle;
}

</style>
<svg class="chart"></svg>
<script>

var width = 960,
    height = 500;

var y = d3.scaleLinear()
	.domain([10, 42])
    .range([height, 0]);

var barchart = d3.select(".chart")
    .attr("width", width)
    .attr("height", height);

// d3.tsv("data.tsv", type, function(error, data) {
var data = [
  {name: "Locke",    value:  4},
  {name: "Reyes",    value:  8},
  {name: "Ford",     value: 15},
  {name: "Jarrah",   value: 16},
  {name: "Shephard", value: 23},
  {name: "Kwon",     value: 42}
];
  y.domain([0, d3.max(data, function(d) { return d.value; })]);

  var barWidth = width / data.length;

  var bar = barchart.selectAll("g")
      .data(data)
    .enter().append("g")
      .attr("transform", function(d, i) { return "translate(" + i * barWidth + ",0)"; });

  bar.append("rect")
      .attr("y", function(d) { return y(d.value); })
      .attr("height", function(d) { return height - y(d.value); })
      .attr("width", barWidth - 1);

  bar.append("text")
      .attr("x", barWidth / 2)
      .attr("y", function(d) { return y(d.value) + 3; })
      .attr("dy", ".75em")
      .text(function(d) { return d.value; });
// });

function type(d) {
  d.value = +d.value; // coerce to number
  return d;
}

</script>
-->






