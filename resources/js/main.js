function highlightCode() {
	hljs.configure({languages:['python']});
	document.querySelectorAll('pre code')
		.forEach((ele) => {hljs.highlightBlock(ele)});
}

function init() {
	if( window.location.search.match( /\?print$/gi ) ) {
		const link = document.createElement('link');
		link.rel = 'stylesheet';
		link.type = 'text/css';
		link.href = '../../resources/css/print.css';
		document.querySelector('head').appendChild(link);
	} else {
        const slideShow = new SlideShow(document.querySelector('#slides'));
        slideShow.start();
		const printLink = document.createElement('a');
		printLink.href = "?print";
		printLink.textContent = 'print version';
		printLink.classList.add('printLink');
		document.body.appendChild(printLink);
	}
	highlightCode(); 

}
document.addEventListener('DOMContentLoaded', init);
