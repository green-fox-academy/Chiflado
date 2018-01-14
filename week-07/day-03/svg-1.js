'use strict';

window.onload=function() {
	var a = document.querySelector('svg');
	// Get the SVG document inside the Object tag
	var svgDoc = a.contentDocument;
	// Get one of the SVG items by ID;
	var svgItem = svgDoc.querySelector("#very-rectangle");
	// Set the colour to something else
	svgItem.fill = "lime";
};